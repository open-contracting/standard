#!/usr/bin/env python
import csv
import gettext
import json
import logging
import os
import re
import sys
import warnings
from collections import defaultdict
from contextlib import contextmanager
from glob import glob
from io import StringIO
from pathlib import Path

import click
import json_merge_patch
import lxml.etree
import lxml.html
import requests
from babel.messages.pofile import read_po
from docutils.utils import relative_path
from lxml import etree
from ocdsextensionregistry import get_versioned_release_schema
from ocdsextensionregistry.util import replace_refs
from ocdskit.schema import get_schema_fields

basedir = Path(__file__).resolve().parent
schemadir = basedir / "schema"
localedir = basedir / "docs" / "locale"

sys.path.append(str(basedir / "docs"))

from conf import release  # noqa: E402


def custom_warning_formatter(message, category, filename, lineno, line=None):
    return str(message) + "\n"


warnings.formatwarning = custom_warning_formatter


def json_load(filename):
    """Load JSON data from the given filename."""
    with (schemadir / filename).open() as f:
        return json.load(f)


def json_dump(filename, data):
    """Write JSON data to the given filename."""
    with (schemadir / filename).open("w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def csv_load(url, delimiter=","):
    """Load CSV data into a ``csv.DictReader`` from the given URL."""
    return csv.DictReader(StringIO(get(url).text), delimiter=delimiter)


@contextmanager
def csv_dump(filename, fieldnames):
    """Write CSV headers to the given filename, and yield a ``csv.writer``."""
    f = (schemadir / "codelists" / filename).open("w")
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(fieldnames)
    try:
        yield writer
    finally:
        f.close()


def get(url):
    """GET a URL and returns the response. Raise an exception if the status code is not successful."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response


def get_metaschema():
    """Patches and returns the JSON Schema Draft 4 metaschema."""
    return json_merge_patch.merge(
        json_load("metaschema/json-schema-draft-4.json"), json_load("metaschema/meta-schema-patch.json")
    )


@click.group()
def cli():
    pass


@cli.command()
@click.argument("filename")
def unused_terms(filename):
    """
    Print terms in FILENAME that don't occur in the documentation.

    Can be used to remove unused terms from a glossary.
    """
    paths = []
    for extension in ("csv", "json", "md"):
        paths.extend(glob(str(basedir / "docs" / "**" / f"*.{extension}"), recursive=True))

    corpus = []
    for path in paths:
        with open(path) as f:
            # Replace punctuation with whitespace, except in abbreviations like "e.g.".
            corpus.append(re.sub(r'(?<!\b[a-z])[.,:"’[\]]', " ", f.read()).lower())
    corpus = " ".join(corpus)

    with open(filename) as f:
        for line in f:
            if f" {line.strip().lower()} " not in corpus:
                click.echo(line, nl=False)


@cli.command()
@click.option("--ignore-base", help="A base branch to ignore, e.g. 1.2-dev")
def missing_changelog(ignore_base):
    """Print pull requests not mentioned in the changelog."""
    # Ignore PRs to the ppp-extension branch, which became OCDS for PPPs.
    ignore = ["ppp-extension"]
    if ignore_base:
        ignore.append(ignore_base)

    # Ignore PRs to unmerged branches.
    url = "https://api.github.com/repos/open-contracting/standard/pulls?per_page=100&state=open"
    response = get(url)
    ignore.extend(pr["head"]["ref"] for pr in response.json())

    with open(basedir / "docs" / "history" / "changelog.md") as f:
        prs = [int(n) for n in re.findall(r"https://github.com/open-contracting/standard/pull/(\d+)", f.read())]

    prs.extend(
        [
            # Reverted
            971,
            977,
            # Obsoleted by the Primer
            1017,
        ]
    )

    # Ignore PRs that sync branches or that release versions/
    pattern = re.compile(r"^(?:Merge \S+ into \S+|\S+ Release)$")

    count = 0

    url = "https://api.github.com/repos/open-contracting/standard/pulls?per_page=100&state=closed"
    while url:
        response = get(url)
        url = response.links.get("next", {}).get("url")

        for pr in response.json():
            number = pr["number"]
            merged_at = pr["merged_at"]
            milestone = pr["milestone"] or {}
            milestone_number = milestone.get("number")
            milestone_title = milestone.get("title")
            title = pr["title"]
            base_ref = pr["base"]["ref"]

            # Include merged PRs, not in the "Minor:" or "1.0-RC" milestones, not syncing branches, and not ignored.
            if not merged_at or milestone_number in {26, 27, 28, 29, 2} or pattern.search(title) or base_ref in ignore:
                if number in prs:
                    click.echo(f"WARNING: #{number} should not be in changelog", file=sys.stderr)
                continue

            if number not in prs:
                count += 1
                click.echo(
                    f"[#{number}](https://github.com/open-contracting/standard/pull/{number}) "
                    f"({milestone_title}) {merged_at[:10]}: {title} ({base_ref}:{pr['head']['ref']})"
                )

    if count:
        click.echo(count)


@cli.command()
def pre_commit():
    """
    Update derivative schema files, and generate a CSV file of multilingual fields.

    \b
    - meta-schema.json
    - dereferenced-release-schema.json
    - versioned-release-validation-schema.json
    """
    nonmultilingual = {
        # Identifiers.
        "amendsReleaseID",
        "id",
        "identifier",
        "identifiers",
        "ocid",
        "relatedItems",
        "releaseID",
        # Missing format properties. https://github.com/open-contracting/standard/issues/881
        "email",
        # Published-defined formats.
        "faxNumber",
        "postalCode",
        "telephone",
        # Published-defined codelists.
        "code",
        "scheme",
    }

    release_schema = json_load("release-schema.json")
    jsonref_release_schema = replace_refs(json_load("release-schema.json"), keep_defs=True)

    counts = defaultdict(list)
    nonstring = ("boolean", "integer", "number", "object")
    for field in get_schema_fields(jsonref_release_schema):
        name = field.path_components[-1]
        # Skip definitions (output dereferenced properties only). Skip deprecated fields.
        if field.definition or field.deprecated:
            continue
        multilingual = (
            # If a field can be a non-string, it is not multilingual.
            not any(t in field.schema["type"] for t in nonstring)
            and ("array" not in field.schema["type"] or not any(t in field.schema["items"]["type"] for t in nonstring))
            # If a field's value is constrained to a codelist or format, it is not multilingual.
            and not any(prop in field.schema for prop in ("codelist", "format"))
            # If an array can contain non-strings, it is not multilingual.
            and not ("array" in field.schema["type"] and "object" in field.schema["items"]["type"])
            # Specific exceptions.
            and name not in nonmultilingual
        )
        field.sep = "/"
        if name in counts and bool(counts[name]) ^ multilingual:
            if not multilingual and field.schema["type"] == "object":
                click.secho(f'{field.path} is an object. {" & ".join(counts[name])} is/are multilingual.', fg="yellow")
            elif multilingual:
                raise click.ClickException(f"{name} is multilingual at {field.path}, but not elsewhere")
            else:
                raise click.ClickException(
                    f'{name} is multilingual at {" & ".join(counts[name])}, but not at {field.path}'
                )
        if multilingual:
            counts[name].append(field.path)
        else:
            counts[name] = counts[name]

    bulletlist = [
        "% STARTLIST",
        *sorted([f"- `{name}`, in any location" for name, paths in counts.items() if len(paths) > 1]),
        *sorted([f"- `{paths[0]}`" for _, paths in counts.items() if len(paths) == 1]),
        "% ENDLIST",
    ]

    path = basedir / "docs" / "guidance" / "map" / "translations.md"
    with path.open() as f:
        contents = f.read()
    with path.open("w") as f:
        f.write(re.sub(r"% STARTLIST.+% ENDLIST", "\n".join(bulletlist), contents, flags=re.DOTALL))

    json_dump("meta-schema.json", get_metaschema())
    json_dump("dereferenced-release-schema.json", jsonref_release_schema)
    json_dump(
        "versioned-release-validation-schema.json",
        get_versioned_release_schema(release_schema, release.replace(".", "__")),
    )


@cli.command()
@click.argument("file", type=click.File())
def update_country(file):
    """
    Update country.csv from ISO 3166-1 using FILE.

    To retrieve the file:

    \b
    1. Open https://www.iso.org/obp/ui/#search/code/
    2. Open the "Network" tab of the "Web Inspector" utility (Option-Cmd-I in Safari)
    3. Set "Results per page:" to 300
    4. Click the last "UIDL" entry in the "Network" tab
    5. Copy its contents, excluding the for-loop, into a file
    """
    # https://www.iso.org/iso-3166-country-codes.html
    # https://www.iso.org/obp/ui/#search

    codes = {
        # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#User-assigned_code_elements
        "XK": "Kosovo",
    }

    rpc = json.load(file)[0]["rpc"][0]
    offset = int(rpc[0])
    for entry in rpc[3][1]:
        d = entry["d"]
        # Clean "Western Sahara*", "United Arab Emirates (the)", etc.
        codes[d[str(offset + 9)]] = re.sub(r" \(the\)|\*", "", d[str(offset + 13)])
        # The country code appears at offsets 9 and 15. Check that they are always the same.
        if d[str(offset + 9)] != d[str(offset + 15)]:
            raise AssertionError

    with open(schemadir / "codelists" / "country.csv", "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["Code", "Title"])
        for code in sorted(codes):
            writer.writerow([code, codes[code]])


@cli.command()
def update_currency():
    """Update currency.csv from ISO 4217."""
    # https://www.iso.org/iso-4217-currency-codes.html
    # https://www.six-group.com/en/products-services/financial-information/data-standards.html#scrollTo=currency-codes

    # List One: Current Currency & Funds
    current_codes = {}
    url = "https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/lists/list_one.xml"
    tree = etree.fromstring(get(url).content)  # noqa: S320 # trusted external
    for node in tree.xpath("//CcyNtry"):
        # Entries like Antarctica have no universal currency.
        if node.xpath("./Ccy"):
            code = node.xpath("./Ccy")[0].text
            title = node.xpath("./CcyNm")[0].text.strip()
            if code not in current_codes:
                current_codes[code] = title
            # We should expect currency titles to be consistent across countries.
            elif current_codes[code] != title:
                raise click.ClickException(f"expected {current_codes[code]}, got {title}")

    # List Three: Historic Denominations (Currencies & Funds)
    historic_codes = {}
    url = "https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/amendments/lists/list_three.xml"
    tree = etree.fromstring(get(url).content)  # noqa: S320 # trusted external
    for node in tree.xpath("//HstrcCcyNtry"):
        code = node.xpath("./Ccy")[0].text
        title = node.xpath("./CcyNm")[0].text.strip()
        valid_until = node.xpath("./WthdrwlDt")[0].text
        # Use ISO8601 interval notation.
        valid_until = re.sub(r"^(\d{4})-(\d{4})$", r"\1/\2", valid_until.replace(" to ", "/"))
        if (
            code not in current_codes
            # Last condition: If the code is historical, use the most recent title and valid date.
            and (code not in historic_codes or valid_until > historic_codes[code]["Valid Until"])
        ):
            historic_codes[code] = {"Title": title, "Valid Until": valid_until}

    with csv_dump("currency.csv", ["Code", "Title", "Valid Until"]) as writer:
        for code in sorted(current_codes):
            writer.writerow([code, current_codes[code], None])
        for code in sorted(historic_codes):
            writer.writerow([code, historic_codes[code]["Title"], historic_codes[code]["Valid Until"]])

    release_schema = json_load("release-schema.json")
    codes = sorted([*current_codes, historic_codes])
    release_schema["definitions"]["Value"]["properties"]["currency"]["enum"] = [*codes, None]

    json_dump("release-schema.json", release_schema)


@cli.command()
def update_language():
    """Update language.csv from ISO 639-1."""
    # https://www.iso.org/iso-639-language-codes.html
    # https://id.loc.gov/vocabulary/iso639-1.html

    with csv_dump("language.csv", ["Code", "Title"]) as writer:
        for row in csv_load("https://id.loc.gov/vocabulary/iso639-1.tsv", delimiter="\t"):
            # Remove parentheses, like "Greek, Modern (1453-)", and split alternatives.
            titles = re.split(r" *\| *", re.sub(r" \(.+\)", "", row["Label (English)"]))
            # Remove duplication like "Ndebele, North |  North Ndebele" and join alternatives using a comma instead of
            # a pipe. To preserve order, a dict without values is used instead of a set.
            titles = ", ".join({" ".join(reversed(title.split(", "))): None for title in titles})
            writer.writerow([row["code"], titles])


@cli.command()
def update_media_type():
    """
    Update mediaType.csv from IANA.

    Ignores deprecated and obsolete media types.
    """
    # https://www.iana.org/assignments/media-types/media-types.xhtml

    # See "Registries included below".
    registries = [
        "application",
        "audio",
        "font",
        "image",
        "message",
        "model",
        "multipart",
        "text",
        "video",
    ]

    with csv_dump("mediaType.csv", ["Code", "Title"]) as writer:
        for registry in registries:
            # See "Available Formats" under each heading.
            for row in csv_load(f"https://www.iana.org/assignments/media-types/{registry}.csv"):
                if " " in row["Name"]:
                    name, message = row["Name"].split(" ", 1)
                else:
                    name, message = row["Name"], None
                code = f"{registry}/{name}"
                template = row["Template"]
                # All messages are expected to be about deprecation and obsoletion.
                if message:
                    logging.warning("%s: %s", message, code)
                # "x-emf" has "image/emf" in its "Template" value (but it is deprecated).
                elif template and template != code:
                    raise click.ClickException(f"expected {code}, got {template}")
                else:
                    writer.writerow([code, name])

        writer.writerow(["offline/print", "print"])


@cli.command()
@click.pass_context
def update(ctx):
    """Update codelists except country.csv."""
    ctx.invoke(update_currency)
    ctx.invoke(update_language)
    ctx.invoke(update_media_type)


@cli.command()
@click.pass_context
def check_iso_6523(ctx):
    def text(node, xpath):
        return re.sub(r"\s+", " ", node.xpath(xpath)[0])

    """
    Checks PEPPOL BIS Billing 3.0's ISO 6523 ICD codelist for new codes.
    """
    # We use this, because we don't know a better source for the ISO 6523 codelist.

    # As of 2022-04-19, the range is 0002-0213, skipping 0092 0103 0181 0182.
    minimum = 2
    maximum = 213
    skipped = {92, 103, 181, 182}

    response = get("https://docs.peppol.eu/poacc/billing/3.0/codelist/ICD/")

    divs = lxml.html.fromstring(response.content).xpath("//dd/div[@id]")
    if not divs:
        raise click.ClickException("The HTML markup of the data source has changed. Please update the script.")

    rows = []
    for div in divs:
        identifier = div.attrib["id"]
        number = int(identifier)
        if number < minimum or number > maximum or number in skipped:
            name = text(div, "./strong/text()")
            notes = text(div, "./p/text()")
            issuer = ""

            # "Issuing agency: " appears at the end of the paragraph. The rest of the paragraph contains either a
            # purpose ("Intended Purpose/App. Area") or notes ("Notes on Use of Code"), with or without the label.
            notes = re.sub(r"(Notes on Use of Code|Intended Purpose/App. Area)[: ]+", "", notes)
            if "Issuing agency: " in notes:
                notes, issuer = notes.split("Issuing agency: ")

            rows.append([identifier, name, issuer, notes])

    if rows:
        csv.writer(sys.stdout, delimiter="\t").writerows(rows)
    else:
        click.echo("No new codes found.")


def add_translation_note(path, language, domain):
    """Add a translation note to a file."""
    base_url = "https://standard.open-contracting.org/1.1"

    with open(path) as f:
        document = lxml.html.fromstring(f.read())

    translator = gettext.translation("theme", localedir, languages=[language])
    _ = translator.gettext

    pattern = f"{base_url}/{{}}/{domain}/"
    response = requests.get(pattern.format(language), timeout=10)

    # If it's a new page, add the note to the current version of the page.
    if response.status_code == requests.codes.not_found:
        message = _(
            'This page was recently added to the <a href="%(url)s">English documentation</a>. '
            "It has not yet been translated."
        )

    # If it's an existing page, add the note the last version of the page.
    else:
        response.raise_for_status()
        xpath = '//div[@itemprop="articleBody"]'

        replacement = lxml.html.fromstring(response.content).xpath(xpath)[0]
        replacement.make_links_absolute(f"{base_url}/{language}")

        # Remove any existing translation notes.
        parent = replacement.xpath("//h1")[0].getparent()
        for div in replacement.xpath('//h1/following-sibling::div[@class="admonition note"]'):
            parent.remove(div)

        element = document.xpath(xpath)[0]
        element.getparent().replace(element, replacement)

        message = _(
            'This page was recently changed in the <a href="%(url)s">English documentation</a>. '
            "The changes have not yet been translated."
        )

    template = (
        '<div class="admonition note"><p class="first admonition-title">%(note)s</p><p class="last">'
        "%(message)s</p></div>"
    )

    document.xpath("//h1")[0].addnext(
        lxml.etree.XML(template % {"note": _("Note"), "message": message % {"url": pattern.format("en")}})
    )

    with open(path, "wb") as f:
        f.write(lxml.html.tostring(document, encoding="utf-8"))


@cli.command()
def add_translation_notes():
    """
    Implement the localization policy.

    "Minor, non-normative, documentation updates will be translated promptly, but may not always be translated before
    the updates are released. The documentation will clearly display when the English documentation is 'ahead' of
    translations for a particular version."

    https://standard.open-contracting.org/latest/en/governance/translation/
    """
    excluded = (".doctrees", "_downloads", "_images", "_sources", "_static", "codelists", "genindex", "search")

    for language in ("es", "fr"):
        build_dir = basedir / "build" / language
        language_dir = localedir / language / "LC_MESSAGES"

        for root, dirs, files in os.walk(build_dir):
            # Skip Sphinx directories.
            for directory in excluded:
                if directory in dirs:
                    dirs.remove(directory)

            if root == str(build_dir):
                continue

            for name in files:
                # See `sphinx.transforms.i18n.Locale.apply()`.
                # https://github.com/sphinx-doc/sphinx/blob/v2.2.1/sphinx/transforms/i18n.py
                source = os.path.join(root, os.path.dirname(name))
                domain = relative_path(build_dir, source)

                path = language_dir / domain / "index.po"
                if not path.is_file():
                    path = language_dir / f"{domain}.po"
                if not path.is_file():
                    add_translation_note(os.path.join(root, name), language, domain)
                    continue

                # Check the PO files, because Babel sets the msgstr to the msgid if the msgstr is missing.
                with open(path) as f:
                    for message in read_po(f):
                        if not message.string:
                            add_translation_note(os.path.join(root, name), language, domain)
                            break


if __name__ == "__main__":
    cli()
