Enquiries 
========================

## Metadata

To use this extension, include its URL in the ```extension``` array of your release or record package.

```json
{
    "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_enquiry_extension/v1.1.1/extension.json"],
    "releases":[]
}
```

This extension is maintained at [https://github.com/open-contracting/ocds_enquiry_extension](https://github.com/open-contracting/ocds_enquiry_extension)

## Documentation

The enquiries extension can be used to record questions raised during a contracting process, and the answers provided.

### Structure

The extension adds an ```enquiries``` array to tender, consisting of one or more enquiry objects, each with fields for a question, and an answer.

Example:

```json
{
  "tender":{
    "enquiries":[{
      "id":"Q1",
      "date":"2017-01-22T14:55:00Z",
      "author":{
        "name":"Open Data Services Co-op",
        "id":"GB-COH-09506232"
      },
      "title":"Variations of timeline accepted?",
      "description":"The tender specifies delivery of Item 1 by end of March 2017. Will alternative proposals for the timeline be considered?",
      "dateAnswered":"2017-02-05T09:00:00Z",
      "answer":"There is a hard deadline of 15th April 2017. All proposals must be for delivery of Item 1 by this date.",
      "relatedItem":"1",
      "threadID":"1"
    }]
  }
}
```

Supporting documents with clarifications, or a full document containing answers to questions can be included in the ```tender/documents``` array with a ```documentType``` of 'clarifications'. 

Where the answers to a question are only available in attached documents, an ```answer``` value such as 'Consult section N of "%document name%" in the documents section' may be entered to allow analysts of the data to identify that an answer to this question has been provided. 

When a system allow a discussion format, where each answer can be followed by a further clarification question, the ```threadID``` property can be used to link together multiple entries in the ```enquiries``` array.

### Usage guidance

Implementations may vary on the amount of enquiry information they provide, and when it is provided. 

Some publishers may omit the identity of the question author to protect confidentiality of enquirers, or may anonymize this information (e.g. simply putting the author name as 'Organization 1' or 'Organization 2' so that it is possible to see questions from the same organization, but not to know the identity of that organization.)

The ```relatedItem``` and ```relatedLot``` properties are available for use when questions can be asked in relation to a specific lot or item. 

Where possible, the recommended approach is to:

* Make release with a ```tenderUpdate``` release tag for every new question or batch of questions received, providing an enquiries array with each of the questions in;
* Make a release with a ```tenderUpdate``` release tag when the answers to the questions are provided, updating the earlier enquiries array so each entry now contains both a question and an answer;

This approach will enable third-party applications to watch for releases that provide answers to questions, and will support procurement monitors in reviewing the way in which questions are being answered. 

We recommend that publishers provide question answers as plain text, or with minimal HTML markup (paragraphs and line-breaks), and that consuming applications parse text appropriately to format it for readability (e.g. replace line-breaks with paragraph breaks in HTML).

### Reference

```eval_rst
.. extensiontable::
   :extension: enquiries
   :exclude_definitions: Tender
```
