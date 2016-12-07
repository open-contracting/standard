## Documentation details

Contracting processes involve many different documents. There should be a presumption of 'open by default' when it comes to publishing these documents as part of an Open Contracting process.

The OCDS documentation block, which is used widely through the different sections of the standard, provides a means to link out to externally hosted documents. 

These should generally be provided at their own stable URL, without requirements to log-in or authenticate. Redactions should be kept to a minimum. 

### Providing enhanced documentation and document links

A number of implementations of OCDS, notable OCDS for PPPs, explicitly require a number of key items of information to be disclosed. These items are articulated as an extended list of entries for the ```documentType``` codelist. 

However, rather than just linking out to the entire document where the information is found, this extension describes a way to:

* Summarise the information in the ```description``` field of the relevant document block;
* Link to specific page numbers;
* Describe any additional arrangements required to access the document or find the relevant information;
* Record the author of the document;

Providing clear summaries allows applications to display this information in a user-interface, allowing users to access key facts and justifications without clicking through to download and search for the information in a full document.

Linking to the specific page where information is found supports quality assurance of disclosure. 

Describing ```accessDetails``` for a document ensures that, even when documents are only accessible through attendance at a location (for example), that users can find how to discover them - and so that auditors can check documents have been made accessible in the appropriate ways.

Recording the author of a document is important for checking whether there are potential conflicts of interest to be aware of: for example, when the author of a feasbility study is later involved in the team submitting a bid. 

### Extension fields

```eval_rst
.. extensiontable::
   :extension: documentation_details
```