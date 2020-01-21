
# Award notices and decisions

Award notices are used by procuring entities to disclose award decisions, i.e. the value and/or items awarded to each supplier.

A single award notice can be used to disclose many award decisions; however in order for an award in OCDS to communicate a direct relationship between the items being purchased, the supplier providing the items, and the value of the items, such notices ought to be split into multiple awards in OCDS.

```eval_rst
.. admonition:: Example: Modelling award notices with multiple decisions
    :class: admonition

      In Paraguay, a single award notice is used to disclose many award decisions. Detailed information is provided about each individual award decision; however all decisions on an award notice share the same identifier. For example:

      ![Example award notice from Paraguay](../../_static/awards_example_paraguay.png)

      Using a single award object to model such a notice in OCDS would make it impossible to determine which items related to which suppliers or how much of the total award value related to each supplier:

      ```eval_rst
      .. csv-table-no-translate::
         :header-rows: 1
         :file: ../../examples/award_decisions/single_award.csv
      ```

      For the award object in OCDS to communicate a direct relationship between items, suppliers, and values, Paraguay's award notice is split into multiple award objects, one for each supplier/value pairing on the notice.

      ```eval_rst
      .. csv-table-no-translate::
         :header-rows: 1
         :file: ../../examples/award_decisions/multi_award.csv
      ```

      There are no identifiers for the individual supplier/value pairings on the original award notice, so it is necessary to create a new identifier for each award object in OCDS. The approach to creating an identifier will depend on the properties of the dataset; for example, in Paraguay a combination of the award notice identifier and the supplier name is used, however this approach is only appropriate as long as there can only be one supplier per award decision and each supplier can only appear once per notice.

      ```eval_rst
      .. csv-table-no-translate::
         :header-rows: 1
         :file: ../../examples/award_decisions/identifiers.csv
      ```

      [View the example in Paraguay’s API](http://beta.dncp.gov.py/datos/api/v3/doc/ocds/record/ocds-03ad3f-340885-1)

```
