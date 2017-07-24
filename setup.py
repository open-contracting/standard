from setuptools import setup, find_packages

setup(
    name="ocds-standard",
    long_description=__doc__,
    packages=find_packages(),
    entry_points="""
        [babel.extractors]
        jsonschema_text = standard.schema.utils.jsonschema_extract:extract
        codelists_text = standard.schema.utils.codelists_extract:extract
        """
)
