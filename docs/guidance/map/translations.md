# Translations

If your data sources have separate data elements for different language versions of the same content, you can publish each language as a separate OCDS dataset.

```{admonition} What does "same content" mean?
Two texts have the same content if they describe the same thing: for example, "United Kingdom" in English and "Royaume-Uni" in French. On the other hand, if your contracting process has different contact points for different language speakers, that content is *not* the same. Your OCDS data should therefore contain one contact point for each, using the [Additional Contact Points](https://extensions.open-contracting.org/en/extensions/additionalContactPoint/master/) extension.
```

## What you can translate

You can publish the values of these fields in any language:

% STARTLIST
- `coordinates`, in any location
- `description`, in any location
- `finalStatusDetails`, in any location
- `legalName`, in any location
- `locality`, in any location
- `name`, in any location
- `rationale`, in any location
- `region`, in any location
- `streetAddress`, in any location
- `title`, in any location
- `tender/awardCriteriaDetails`
- `tender/procurementMethodDetails`
- `tender/procurementMethodRationale`
- `tender/submissionMethodDetails`
% ENDLIST

When publishing OCDS data in different languages, remember to set the `language` field. For example:

`````{tab-set}

````{tab-item} English
```{code-block} json
:emphasize-lines: 8,11
{
  "ocid": "ocds-213czf-000-00001",
  "id": "1",
  "date": "2024-01-01T00:00:00Z",
  "tag": [
    "tender"
  ],
  "language": "en",
  "tender": {
    "id": "1",
    "title": "Purchase of office supplies"
  }
}
```
````

````{tab-item} Spanish
```{code-block} json
:emphasize-lines: 8,11
{
  "ocid": "ocds-213czf-000-00001",
  "id": "1",
  "date": "2024-01-01T00:00:00Z",
  "tag": [
    "tender"
  ],
  "language": "es",
  "tender": {
    "id": "1",
    "title": "Compra de material de oficina"
  }
}
```
````

`````

## What you cannot translate

The names of fields, and the values of all fields not listed above, need to be the same across your translated OCDS datasets, in order to support interoperability, which is the purpose of standardization. These cover:

- **Identifiers**, like `ocid`, `id`, etc.
- **Codes**, like release tags, identifier schemes and milestone codes
- **Formatted values**, like URLs, dates, email addresses, telephone numbers and postal codes
- **Non-text fields**, like numbers and booleans

For example, the name of the `tag` field needs to be "tag", and its value needs to be a list of codes from the [release tag codelist](../../schema/codelists.md#release-tag).

`````{tab-set}

````{tab-item} Valid
```{code-block} json
:emphasize-lines: 5-7
{
  "ocid": "ocds-213czf-000-00001",
  "id": "1",
  "date": "2024-01-01T00:00:00Z",
  "tag": [
    "tender"
  ],
  "language": "es",
  "tender": {
    "id": "1",
    "title": "Compra de material de oficina"
  }
}
```
````

````{tab-item} Invalid (incorrect name)
```{code-block} json
:emphasize-lines: 5
{
  "ocid": "ocds-213czf-000-00001",
  "id": "1",
  "date": "2024-01-01T00:00:00Z",
  "etiqueta": [
    "tender"
  ],
  "language": "es",
  "tender": {
    "id": "1",
    "title": "Compra de material de oficina"
  }
}
```
````

````{tab-item} Invalid (incorrect value)
```{code-block} json
:emphasize-lines: 6
{
  "ocid": "ocds-213czf-000-00001",
  "id": "1",
  "date": "2024-01-01T00:00:00Z",
  "tag": [
    "licitación"
  ],
  "language": "es",
  "tender": {
    "id": "1",
    "title": "Compra de material de oficina"
  }
}
```
````

`````

## Translating headers in spreadsheets

To ease access for non-English speakers, instead of using field *names* as column headers (which are always in English), you can use field *titles*, which are translated in [OCDS translations](localization.md#translating-the-standard).

For example, this CSV excerpt uses field titles from the Spanish translation:

| ID de Entrega | Fecha de entrega     |
| ------------- | -------------------- |
| 1             | 2024-01-01T00:00:00Z |

You can use [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/) to generate files with field titles. For example, this command converts an OCDS release package to XLSX format, using field titles from the release schema:

```bash
flatten-tool flatten release_package.json --output-format=xlsx --use-titles --schema=release-schema.json --root-id=ocid --root-list-path=releases
```

```{note}
Field titles are available in English, Spanish and French. To translate titles to another language, [contact the Data Support Team](mailto:data@open-contracting.org).
```
