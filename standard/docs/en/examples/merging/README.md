# Merging examples

## Maintenance

You will need [OCDS Kit](https://pypi.org/project/ocdskit/) and [jq](https://stedolan.github.io/jq/).

```shell
cat standard/docs/en/examples/merging/merge-*.json | jq -crM | ocdskit --pretty compile --package --linked-releases --published-date 2016-03-05T13:02:00Z --uri http://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json > standard/docs/en/examples/merging/merged.json
cat standard/docs/en/examples/merging/merge-*.json | jq -crM | ocdskit --pretty compile --package --linked-releases --published-date 2016-03-05T13:02:00Z --versioned --uri http://standard.open-contracting.org/examples/records/ocds-213czf-000-00002-merge.json > standard/docs/en/examples/merging/versioned.json
```
