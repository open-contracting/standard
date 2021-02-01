# Publish

Congratulations! You are almost ready to publish your OCDS data.

## Finalize your publication policy

In OCDS, a publication policy is an essential data guide for users. Each OCDS publisher ought to have a publication policy that covers:

* What information is and is not covered within the scope of the publication
* Any custom codelists used - or custom codes added to existing codelists
* How timely or frequent is publication
* Where the data comes from and how it is generated
* The format(s) of the publication and where to access the data
* License information for data reuse
* Contact information for the publisher

The publication policy ought to be made available as a public web page, with links to the policy added to OCDS release packages and record packages and any OCDS web portal.

The publication policy ought to also contain information about future plans for changes to the publication (and be updated when changes are made).

**Resource**: Use the [OCDS publication policy template](https://www.open-contracting.org/resources/ocds-1-1-publication-policy-template/) to develop your publication policy.

## License your data

Publishing data under an open licenses is an important part of open contracting. Without this, restrictions on re-use can prevent many of the important [use cases](../../getting_started/use_cases) for open contracting information being realized.

A license statement sets out the permission that users have to access, use and re-use the data. This can take the form of a [Public Domain Dedication or Certification](http://creativecommons.org/publicdomain/) which transfers a dataset into the public domain, or re-asserts that there are no existing copyrights or database rights inherent in the dataset (which is the case for government datasets in some jurisdictions), or the application of a license which sets out the terms under which a dataset can be re-used.

We encourage the use of either a public domain dedication/certification, or an attribution only license.

* Public domain dedication – asserting no copyright, database rights, or contractual rights over the open contracting data. Examples include [Creative Commons' public domain tools](http://creativecommons.org/publicdomain/). These licenses are useful for publishers who manage their own works or have the necessary rights to apply a public domain license to another person's work. In addition, although attribution cannot be "enforced" under such licenses, we encourage you to actively acknowledge and give attribution to all sources, such as the data providers or any data aggregators. Public domain approaches are preferred for Open Contracting Datasets.
* Attribution-only open licenses – licenses that allow for use and reuse, with the only restriction being that attribution (credit) be given. A examples includes the [Creative Commons Attribution licenses 4.0](http://creativecommons.org/licenses/by/4.0/)

When using custom licenses, publishers are encouraged to check that they are [compliant with the Open Definition](http://opendefinition.org/licenses/).

In structured data file you ought to embed a link to the license in the `license` field of the release or record package as indicated below:

```{eval-rst}
.. code-block:: json
   :emphasize-lines: 4

   {
     "uri":"https://standard.open-contracting.org/examples/releases/ocds-213czf-000-00001-02-tender.json",
     "publishedDate":"2010-03-01T09:30:00Z",
     "license":"http://opendatacommons.org/licenses/pddl/1.0/",
     "...":"..."
   }
```

In individual CSV files or other models of publishing, it might not be possible to embed the license information. In these cases (and in the structured data case also) publishers ought to ensure that a clear statement is provided alongside files where they are provided for download linking to, and explaining, the license terms they are published under. Particular attention ought to be paid to ensuring license information on any data catalogues where open contracting data is listed are accurate.

## Publish and share your data

Once you have published your data, it's time to share it with the world. It is also not the end of your OCDS journey. As users start using the data, there will likely be some requests for iterative improvements over time to improve the quality and usability of the data. You might even want to develop or adapt tools for displaying and using the data.

**Action:** Share your publication on the [OCDS mailing list](../../support/#ocds-community).

**Action:** Request a data quality and usability feedback report from the [OCDS Helpdesk](../../support/#ocds-helpdesk).

**Action:** [Request support from OCP](mailto:data@open-contracting.org) to build capacity or tools for key stakeholders to start using the data.

**Resource:** [OCDS Tool Directory](https://www.open-contracting.org/resources/open-contracting-tools-directory/)

**Resource:** [Guidance for using OCDS data](https://www.open-contracting.org/data/data-use/)
