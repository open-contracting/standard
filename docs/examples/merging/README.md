# Merging examples

## Maintenance

You will need [OCDS Kit](https://pypi.org/project/ocdskit/) and [jq](https://stedolan.github.io/jq/).

```shell
cat docs/examples/merging/merge-*.json | jq -crM | ocdskit --pretty compile --package --linked-releases --published-date 2016-03-05T13:02:00Z --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json > docs/examples/merging/merged.json
cat docs/examples/merging/merge-*.json | jq -crM | ocdskit --pretty compile --package --linked-releases --published-date 2016-03-05T13:02:00Z --versioned --uri https://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json > docs/examples/merging/versioned.json
```
