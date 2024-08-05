# Open Contracting Data Standard

Visit [standard.open-contracting.org](https://standard.open-contracting.org) to read the standard's documentation.

Visit the [OCDS Standard Development Handbook](https://ocds-standard-development-handbook.readthedocs.io/en/latest/standard/) for developer documentation about the standard.

## Maintenance

Install [OCDS Kit](https://pypi.org/project/ocdskit/)

Update the examples in `docs/examples/merging`:

```shell
cat docs/examples/merging/deletions/field_tender*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json --published-date 2013-07-30T09:00:10.000Z > docs/examples/merging/deletions/field_record.json
cat docs/examples/merging/deletions/object_tender*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json > docs/examples/merging/deletions/object_record.json
cat docs/examples/merging/deletions/array_award*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json > docs/examples/merging/deletions/array_record.json
```
