### Putting a dev branch live

If the live branch doesn't exist, create it and push to github. 

Create a pull request for the merge to x.y from x.y-dev (e.g. 1.0-dev to 1.0).

```
Before merge:
- [ ] [Push translations to transifex if any text has changed](https://github.com/open-contracting/standard#translations)
- [ ] [Pull completed translations from transifex](https://github.com/open-contracting/standard#translations)

After merge:
- [ ] Copy the files from dev to live following the instructions at the top of https://github.com/OpenDataServices/opendataservices-deploy/blob/master/salt/ocds-docs-live.sls
- [ ] For a new translation, edit http://standard.open-contracting.org/robots.txt
```

### Merging in schema changes

(these are usually in addition to the above)

```
Before merge:
- [ ] If the version has changed, remember to updated the schema ids and refs
- [ ] Set up a dev instance of Cove using the new schema, and run tests against it

After merge:
- [ ] Create x__y__z schema folder - https://github.com/OpenDataServices/opendataservices-deploy/blob/master/salt/ocds-docs-live.sls#L25
- [ ] Update live Cove to use the new schema

```
