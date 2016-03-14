import requests
import requests_mock
import pytest
import os.path
import json
from jsonschema.validators import Draft4Validator as validator
from jsonschema import FormatChecker

schema_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

release_package_schema = json.load(open(os.path.join(schema_directory, 'release-package-schema.json')))
record_package_schema = json.load(open(os.path.join(schema_directory, 'record-package-schema.json')))
release_schema = json.load(open(os.path.join(schema_directory, 'release-schema.json')))
versioned_release_schema = json.load(open(os.path.join(schema_directory, 'versioned-release-validation-schema.json')))

ref_release_url = record_package_schema['definitions']['record']['properties']['compiledRelease']['$ref']
ref_versioned_release_url = record_package_schema['definitions']['record']['properties']['versionedRelease']['$ref']


def sample_url(extra_path):
    return 'https://raw.githubusercontent.com/open-contracting/sample-data/e8bb6b1aa/' + extra_path


@pytest.mark.parametrize(
    ('data_url', 'schema', 'validates'), 
    [
        (sample_url('generated-examples/1__0__0_generated_release.json'), release_package_schema, True),
        (sample_url('generated-examples/1__0__0_bad_generated_release.json'), release_package_schema, False),
        (sample_url('fictional-example/ocds-213czf-000-00001-01-planning.json'), release_package_schema, True),
        (sample_url('fictional-example/ocds-213czf-000-00001-02-tender.json'), release_package_schema, True),
        (sample_url('fictional-example/ocds-213czf-000-00001-03-tenderAmendment.json'), release_package_schema, True),
        (sample_url('fictional-example/ocds-213czf-000-00001-04-award.json'), release_package_schema, True),
        (sample_url('fictional-example/ocds-213czf-000-00001-05-contract.json'), release_package_schema, True),
        (sample_url('fictional-example/ocds-213czf-000-00001-06-implementation.json'), release_package_schema, True),
#        (sample_url('generated-examples/1__0__0_generated_record.json'), record_package_schema, True),
#        (sample_url('generated-examples/1__0__0_bad_generated_record.json'), record_package_schema, False),
    ]
)
def test_validate(data_url, schema, validates):
    data = requests.get(data_url).json()
    with requests_mock.Mocker() as m:
        m.get(ref_release_url, json=release_schema)
        m.get(ref_versioned_release_url, json=versioned_release_schema)
        #for error in validator(schema).iter_errors(data):
        #    print(error)
        assert validator(schema).is_valid(data) == validates

