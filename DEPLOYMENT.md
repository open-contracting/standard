# Putting a dev branch live

If the live branch doesn't exist, create it and push to github. 

Create a pull request for the merge to x.y from x.y-dev (e.g. 1.0-dev to 1.0).

```
Before merge:
- [ ] [Push translations to transifex if any text has changed](https://github.com/open-contracting/standard#translations)

After merge:
- [ ] Copy the files from dev to live following the instructions at the top of https://github.com/OpenDataServices/opendataservices-deploy/blob/master/salt/ocds-docs-live.sls
```

# Merging in schema changes

```
Before merge:
- [ ] Set up a dev instance of Cove using the new schema, and run tests against it

After merge:
- [ ] Update live Cove to use the new schema

```
