# Purchases from electronic catalogs

Electronic catalogs are a technique, or instrument, for electronic procurement, in which the exact quantity or value of items to be provided by each supplier are not known in advance when the catalog is set-up.

When a buyer makes a purchase from an electronic catalog, an order is placed with a supplier for a specific quantity or value of items.

In OCDS, purchases from electronic catalogs should be modelled using `awards` and `contracts`, since catalog purchases:

1. Create a direct relationship between the items being purchased, the supplier providing the items, and the value of the items (an award in OCDS)

2. Result in a legally binding agreement for the supplier to provide the items (a contract in OCDS)

Modelling purchases from electronic catalogs using `awards` and `contracts` makes it easier to combine data on electronic catalog purchases with data on purchases made using other procurement techniques.

```eval_rst
.. admonition:: Example: Combining data from different procurement techniques
    :class: admonition

      Australia's Department of Defence uses an electronic catalog for purchases of basic office supplies (pens, paper, toner cartridges, etc.).

      3 suppliers provide the items in the catalog: COS, Office National and Mega Office Supplies. Each provides different categories of office supplies.

      In July 2019, the department makes 3 separate purchases from the catalog: envelopes that are supplied by COS, whiteboard markers that are supplied by Office National, and sticky notes that are supplied by Mega Office Supplies. These purchases are represented in the `awards` section of OCDS as follows:

      ```eval_rst
      .. csv-table-no-translate::
         :header-rows: 1
         :file: ../../examples/catalogs/catalog_purchases.csv
      ```

      During the same month, the department also concludes a separate contracting process to procure 30 office desks by awarding a contract to Office National. This purchase is also represented in the `awards` section of OCDS:

      ```eval_rst
      .. csv-table-no-translate::
         :header-rows: 1
         :file: ../../examples/catalogs/separate_process.csv
      ```

      By using the `awards` section consistently for both contracting processes, it is possible to calculate the total value of purchases from Office National in July 2019, using only the `awards` section:

      ```eval_rst
      .. csv-table-no-translate::
         :header-rows: 1
         :file: ../../examples/catalogs/combined.csv
      ```

```

```eval_rst
.. admonition:: Note
    :class: note

    .. markdown::

      The approach for modelling the set-up and second stages of electronic catalogs in OCDS is under discussion ([GitHub issue](https://github.com/open-contracting/standard/issues/396)).

```
