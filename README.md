# Open Contracting Data Standard

Visit [standard.open-contracting.org](https://standard.open-contracting.org) to read the standard's documentation.

Visit the [OCDS Standard Development Handbook](https://ocds-standard-development-handbook.readthedocs.io/en/latest/standard/) for developer documentation about the standard.

## Maintenance

Install [OCDS Kit](https://pypi.org/project/ocdskit/)

Update the examples in `docs/examples/merging`:

```shell
cat docs/examples/merging/merge-*.json | ocdskit --pretty compile --published-date 2016-03-05T13:02:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json --package --linked-releases > docs/examples/merging/merged.json
cat docs/examples/merging/merge-*.json | ocdskit --pretty compile --published-date 2016-03-05T13:02:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json --package --linked-releases --versioned > docs/examples/merging/versioned.json
```

```shell
cat docs/examples/merging/example02-field-tender*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json --published-date 2013-07-30T09:00:10.000Z > docs/examples/merging/example02-field-record.json
cat docs/examples/merging/example02-object-tender*.json | ocdskit --pretty compile --package --versioned --schema schema/release-schema.json > docs/examples/merging/example02-object-record.json
```

Update the examples in `docs/examples/records`:

```shell
cat docs/examples/{tender}.json | ocdskit --pretty compile --published-date 2010-03-15T09:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/records/tender.json
cat docs/examples/{tender,tenderUpdate}.json | ocdskit --pretty compile --published-date 2010-03-20T09:45:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/records/tenderUpdate.json
cat docs/examples/{tender,tenderUpdate,award}.json | ocdskit --pretty compile --published-date 2010-05-10T09:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/records/award.json
cat docs/examples/{tender,tenderUpdate,award,contract}.json | ocdskit --pretty compile --published-date 2010-06-10T10:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/records/contract.json
cat docs/examples/{tender,tenderUpdate,award,contract,implementation}.json | ocdskit --pretty compile --published-date 2011-01-10T09:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/records/implementation.json
cat docs/examples/{tender,tenderUpdate,award,contract,implementation,contractAmendment}.json | ocdskit --pretty compile --published-date 2011-04-05T13:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/records/contractAmendment.json
```