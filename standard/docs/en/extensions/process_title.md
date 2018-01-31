# Process title and description

## Metadata

To use this extension, include its URL in the ```extension``` array of your release or record package.

```json
{
    "extensions":["https://raw.githubusercontent.com/open-contracting/ocds_process_title_extension/v1.1.3/extension.json"],
    "releases":[]
}
```

This extension is maintained at [https://github.com/open-contracting/ocds_process_title_extension](https://github.com/open-contracting/ocds_process_title_extension)

## Documentation

In some cases it is important to provide an overall title and description for a contracting process, distinct from the individual title and description fields contained within `tender`, `award` and `contract` blocks.

This extension provides `release.title` and `release.description` fields.

These will often be used to provide a human-readable summary of information that is provided elsewhere in the OCDS document as structured data.

Publishers using these fields should be aware that not all applications will display their contents, and so key information for understanding the nature of the contracting process should generally **also** be provided using core OCDS fields.

### Issues

Report issues for this extension in the [ocds-extensions repository](https://github.com/open-contracting/ocds-extensions/issues), putting the extension's name in the issue's title.

### Changelog

#### v1.1.3

* Use Apache 2.0 License
* Add tests and tidy code
