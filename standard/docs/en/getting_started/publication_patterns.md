## Publication Patterns





### Packages

Each release or record must be published within an envelope that provides essential meta-data. These are called release and record packages. 

A package provides information on:

* Where the data can be accessed (a URI)
* The publisher of the data
* The date of publication
* The license the data is provided under
* Links to a publication policy and further documentation

A package may contain a single release or record, or may be used to publish a collection of releases, or a collection of records.

Consult the the release package and record package schemas (TODO - ADD LINKS) to package up your data. 

#### Example release package

```json
{
"uri":"http://standard.open-contracting.org/examples/releases/ocds-213czf-000-00001-01-planning.json",
"publishedDate":"2009-03-15T14:45:00Z",
"publisher": {
        "scheme": "GB-COH",
        "uid": "09506232",
        "name": "Open Data Services Co-operative Limited",
        "uri": "http://standard.open-contracting.org/examples/"
    },
"license":"http://opendatacommons.org/licenses/pddl/1.0/",
"publicationPolicy":"https://github.com/open-contracting/sample-data/",
"releases":[{"...":"..."}]
}
```