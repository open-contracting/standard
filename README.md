# Open Contracting Data Standard

Visit [standard.open-contracting.org](https://standard.open-contracting.org) to read the standard's documentation.

Visit the [OCDS Standard Development Handbook](https://ocds-standard-development-handbook.readthedocs.io/en/latest/standard/) for developer documentation about the standard.

## Maintenance

### Update merging examples

You will need [OCDS Kit](https://pypi.org/project/ocdskit/) to update the examples in `docs/examples/merging`.

```shell
cat docs/examples/merging/merge-*.json | ocdskit --pretty compile --package --linked-releases --published-date 2016-03-05T13:02:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json > docs/examples/merging/merged.json
cat docs/examples/merging/merge-*.json | ocdskit --pretty compile --package --linked-releases --published-date 2016-03-05T13:02:00Z --versioned --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json > docs/examples/merging/versioned.json
```
