# Licensing

Publishing data under an open licenses is an important part of open contracting. Without this, restrictions on re-use may prevent many of the important [use cases](../../../getting_started/use_cases/) for open contracting information being realised.

A license statement sets out the permission that users have to access, use and re-use the data. This can take the form of a [Public Domain Dedication or Certification](http://creativecommons.org/publicdomain/) which transfers a dataset into the public domain, or re-asserts that there are no existing copyrights or database rights inherent in the dataset (which is the case for government datasets in some jurisdictions), or the application of a license which sets out the terms under which a dataset may be re-used.

We recommend the use of either a public domain dedication/certification, or an attribution only license.

* Public domain dedication – asserting no copyright, database rights, or contractual rights over the open contracting data. Examples include [Creative Commons’ public domain tools](http://creativecommons.org/publicdomain/). These licenses are useful for publishers who manage their own works or have the necessary rights to apply a public domain license to another person’s work. In addition, although attribution cannot be "enforced" under such licenses, we recommend that you actively acknowledge and give attribution to all sources, such as the data providers or any data aggregators. Public domain approaches are preferred for Open Contracting Datasets.
* Attribution-only open licenses – licenses that allow for use and reuse, with the only restriction being that attribution (credit) be given. A examples includes the [Creative Commons Attribution licenses 4.0](http://creativecommons.org/licenses/by/4.0/)

When using custom licenses, publishers are encouraged to check that they are [compliant with the Open Definition](http://opendefinition.org/licenses/).

In structured data file you can embed a link to the license in the ```license``` field of the release or record package as indicated below:

```eval_rst
.. code-block:: json
   :emphasize-lines: 4
     
     {
         "uri":"http://standard.open-contracting.org/examples/releases/ocds-213czf-000-00001-02-tender.json",
         "publishedDate":"2010-03-01T09:30:00Z",
         "license":"http://opendatacommons.org/licenses/pddl/1.0/",
         "...":"..."
     }
```

In individual CSV files or other models of publishing, it may not be possible to embed the license information. In these cases (and in the structured data case also) publishers should ensure that a clear statement is provided alongside files where they are provided for download linking to, and explaining, the license terms they are under. Particular attention should be paid to ensuring license information on any data catalogues where open contracting data is listed are accurate.