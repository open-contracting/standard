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

Update the examples in `docs/examples/change_history`:

```shell
cat docs/examples/change_history/tender.json | ocdskit --pretty compile --published-date 2010-03-15T09:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/change_history/records/tender.json
cat docs/examples/change_history/{tender,tenderUpdate}.json | ocdskit --pretty compile --published-date 2010-03-20T09:45:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/change_history/records/tenderUpdate.json
cat docs/examples/change_history/{tender,tenderUpdate,award}.json | ocdskit --pretty compile --published-date 2010-05-10T09:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/change_history/records/award.json
cat docs/examples/change_history/{tender,tenderUpdate,award,contract}.json | ocdskit --pretty compile --published-date 2010-06-10T10:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/change_history/records/contract.json
cat docs/examples/change_history/{tender,tenderUpdate,award,contract,implementation}.json | ocdskit --pretty compile --published-date 2011-01-10T09:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/change_history/records/implementation.json
cat docs/examples/change_history/{tender,tenderUpdate,award,contract,implementation,contractAmendment}.json | ocdskit --pretty compile --published-date 2011-04-05T13:30:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00001.json --package --versioned --schema schema/release-schema.json > docs/examples/change_history/records/contractAmendment.json
```
