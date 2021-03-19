# Publication Patterns

## Packaging releases and records

When publishing releases and records, they need to be provided within a release package or record package. These act as an envelope for the data.

A package provides information on:

* Where the data can be accessed (a URI)
* The publisher of the data
* The date of publication
* The license the data is provided under
* Links to a publication policy and further documentation

A package can contain one or more releases or records.

Consult the [release package](../schema/release_package) and [record package](../schema/record_package) schemas to package up your data.

### Example release package

```json
{
"uri":"https://standard.open-contracting.org/examples/releases/ocds-213czf-000-00001-01-planning.json",
"publishedDate":"2009-03-15T14:45:00Z",
"version":"1.1",
"extensions":[],
"publisher": {
        "scheme": "GB-COH",
        "uid": "09506232",
        "name": "Open Data Services Co-operative Limited",
        "uri": "https://standard.open-contracting.org/examples/"
    },
"license":"http://opendatacommons.org/licenses/pddl/1.0/",
"publicationPolicy":"https://github.com/open-contracting/sample-data/",
"releases":[{"...":"..."}]
}
```

## Bulk and individual files

You are encouraged to:

* Ensure all documents referenced in OCDS releases are available online;
* Publish each release and record at its own persistent URL;
* Additionally, produce bulk packages of releases and records for users to download;
* Additionally, produce 'flat' versions of the data for users to access in CSV for Excel formats

You will need to make decisions about how to [segment the data in bulk files](../../guidance/build/hosting/#bulk-downloads), so that files are easy for users to work with. 
