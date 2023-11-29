# Translations

If you need to publish data in multiple languages, you can publish full-file translations. That is, separate OCDS releases for each language.

You can publish the values of free-text fields – like titles and descriptions – in any language, but you need to ensure that the values of `id` fields are consistent across languages so that users can find the translations of objects. You ought to set the `language` field to the language used in free-text fields.

For example, for data published in English and Spanish:

`````{tab-set}

````{tab-item} English
```json
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
    "title": "Purchase of office supplies",
  }
}
```
````

````{tab-item} Spanish
```json
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
    "title": "Compra de material de oficina",
  }
}
```
````

`````

In order for your data to be interoperable and compatible with OCDS tools and methodologies, you cannot translate field names (keys) or codes from codelists. For example, the name of the `tag` field cannot be translated and its items need to be codes from the [release tag codelist](../../schema/codelists.md#release-tag), like 'tender':

`````{tab-set}

````{tab-item} Valid data
```json
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
    "title": "Compra de material de oficina",
  }
}
```
````

````{tab-item} Invalid data (translated field name)
```json
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
    "title": "Compra de material de oficina",
  }
}
```
````

````{tab-item} Invalid data (translated code)
```json
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
    "title": "Compra de material de oficina",
  }
}
```
````

`````

The fields whose values can be translated are listed in the [internationalization lookup table](#internationalization-lookup-table).

## Translating headers in spreadsheets/CSVs

In order to ease access for non-English speakers, instead of using field *names* as column headers (which are always in English), you can use field *titles*.

The titles are currently available in English, Spanish and French. If you would like to translate the titles to your own language, please [contact the OCDS Helpdesk](mailto:data@open-contracting.org).

For example, this CSV excerpt uses field titles from the Spanish translation of OCDS:

| ID de Entrega | Fecha de entrega     |
| ------------- | -------------------- |
| 1             | 2024-01-01T00:00:00Z |

You can use [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/) to generate files with translated field titles. For example, this command converts an OCDS release package to XLSX format, using field titles from the schema:

```bash
flatten-tool flatten -s release-schema.json -f xlsx --use-titles --root-id=id --root-list-path=releases release_package.json
```

## Internationalization lookup table

Use the following table to check whether a field can be translated. You can download the table as a [CSV spreadsheet](../../_static/i18n.csv).

```{csv-table}
:file: ../../_static/i18n.csv
:header-rows: 1
```
