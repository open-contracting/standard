# Open Contracting Data Standard

Visit [standard.open-contracting.org](https://standard.open-contracting.org) to read the standard's documentation.

Visit the [OCDS Standard Development Handbook](https://ocds-standard-development-handbook.readthedocs.io/en/latest/standard/) for developer documentation about the standard.

## Maintenance

Install [OCDS Kit](https://pypi.org/project/ocdskit/)

Update the examples in `docs/examples/merging`:

```shell
cat docs/examples/merging/updates/{tender*,award*}.json | ocdskit --pretty compile --published-date 2016-03-05T13:02:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json --package --linked-releases > docs/examples/merging/updates/merged.json
cat docs/examples/merging/updates/{tender*,award*}.json | ocdskit --pretty compile --published-date 2016-03-05T13:02:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json --package --linked-releases --versioned > docs/examples/merging/updates/versioned.json
```

```shell
cat docs/examples/merging/deletions/field-tender*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json --published-date 2013-07-30T09:00:10.000Z > docs/examples/merging/deletions/field-record.json
cat docs/examples/merging/deletions/object-tender*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json > docs/examples/merging/deletions/object-record.json
cat docs/examples/merging/deletions/array_award*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json > docs/examples/merging/deletions/array-record.json
```
