## Publication Patterns

OCDS supports a 5 ☆ approach to publishing Open Contracting data on the web. Each step builds on the steps before.

**☆ Upload basic contracting data and documents to web**

> Whether or not you can adopt a common standard right now, you should make sure important notices and documents are freely accessible online.

**☆ ☆ Provide machine-readable data**

>Providing data about your contracting processes in CSV files or other structured formats makes it easier for others to analyse. 
>
>*If you jump straight to 3 ☆ publication, you can generate flattened CSV versions of your data using the OCDS flatten tool.*

**☆ ☆ ☆ Use the OCDS standard**

>Producing bulk releases and records packages using the OCDS standard makes your data easier to re-use and join-up with other contracting data. 

**☆ ☆ ☆ ☆ Provide API access to data**

>Providing each release and record at it's own persistent URI improves the usability of your data. Providing APIs helps users locate the information they are looking for quicker, and enables third-parties to build more advanced and responsive services on your data. 

**☆ ☆ ☆ ☆ ☆ Provide joined-up data**

>Adding links to your contracting data, connecting out to other datasets on project planning, public spending or company registrations, adds further value to your data, enabling new kinds of re-use. 


### Packaging releases and records

When publishing releases and records, they must be provided within a release or record package. These act as an envelope for the data.

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

### Bulk and individual files

For 4 ☆ publication, you should:

* Ensure all documents referenced in OCDS releases are available online;
* Publish each release and record at it's own persistent URL;
* Additionally, produce bulk packages of releases and records for users to download;
* Additionally, produce 'flat' versions of the data for users to access in CSV for Excel formats

You will need to make decisions about how to segment the data in bulk files, so that files are easy for users to work with. 

