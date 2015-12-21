[TOC]

# Record Package

<span class="lead">The record package schema describes the container document for publishing records. The contents of a record are based on the release schema. The package contains important meta-data.</span>

You can view an interactive version of the record schema below (requires javascript) or [download this version of the schema here]({% url 'schema' release_name 'record-package-schema' %}).

A separate, auto-generated, [versioned release validation schema]({% url 'schema' release_name 'versioned-release-validation-schema' %}) is provided for validating releases within fully versioned records.

## Schema browser

Click on schema elements to expand the tree, or use the '+' icon to expand all elements. Use { } to view the underlying schema for any section.

<script src="{{ STATIC_URL }}docson/widget.js" data-schema="{% url 'schema' release_name 'record-package-schema' %}"></script>

