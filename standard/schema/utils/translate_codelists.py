import gettext
import glob
import csv
import os
from os.path import abspath, dirname, join


language = os.environ.get("CODELIST_LANG")
fallback = False
if language == 'en':
    fallback = True

translator = gettext.translation('codelists', 'docs/locale', languages=[language], fallback=fallback)

codelists_dir = join(dirname(dirname(abspath(__file__))), 'codelists')
codelists_output_dir = join(dirname(dirname(abspath(__file__))), 'codelists_translated')

directory_name = 'build/' + language 

def convert_fieldname(name):
    for heading in ('Title', 'Description'):
        if heading in name:
            return translator.gettext(heading)
    return translator.gettext(name)

if not os.path.exists(directory_name):
    os.makedirs(directory_name)

for file in glob.glob(codelists_dir + '/*.csv'):
    output_file = join(codelists_output_dir, file.split('/')[-1])
    with open(file) as csv_file, open(output_file, 'w+') as out_csv_file:
        dict_reader = csv.DictReader(csv_file)
        fieldnames = [convert_fieldname(fieldname) for fieldname in dict_reader.fieldnames]
        dict_writer = csv.DictWriter(out_csv_file, fieldnames)
        dict_writer.writeheader()

        for row in dict_reader:
            new_row = {}
            for key, value in row.items():
                if 'title' in key.lower() or 'description' in key.lower() or 'name' in key.lower():
                    if value:
                        value = translator.gettext(value)
                new_row[convert_fieldname(key)] = value
            dict_writer.writerow(new_row)

