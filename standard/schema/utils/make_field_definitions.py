#!/usr/bin/env python
import json
import csv


def make_definition_table(json,file_path,what="properties",section=""): 
    table = [['Field Name','Description','Format']]
    if(section):
        block = json[what][section]["properties"]
    else:
        block = json[what]

    
    for prop in block:
        types = block[prop].get('type','')
        if isinstance(types,list):
            types = ", ".join(types)
        else:
            types = types
            

        if types == "array":
            pass
        if block[prop].get("$ref"):
          #  table.append([prop,block[prop].get('title',''),"Reference","-","See " + block[prop]["$ref"].replace("#/definitions/","")])
          table.append([prop,"See " + block[prop]["$ref"].replace("#/definitions/",""),"Reference"])
        else:
          #  table.append([prop,block[prop].get('title',''),types,block[prop].get('format',''),block[prop].get('description','')])
          table.append([prop,block[prop].get('description',''),block[prop].get('format','')])
          
        with open(file_path, 'wb') as f:
            writer = csv.writer(f)
            for row in table:
                writer.writerow(row)


if __name__ == "__main__":
    from os.path import abspath, dirname, join

    schema_dir = dirname(dirname(abspath(__file__)))
    file_path = join(schema_dir,"../docs/field_definitions/")
    
    with open(join(schema_dir, 'release-schema.json'), 'rb') as f:
        release = json.loads(f.read())

    with open(join(schema_dir, 'release-package-schema.json'), 'rb') as f:
        releasePackage = json.loads(f.read())

    with open(join(schema_dir, 'record-package-schema.json'), 'rb') as f:
        recordPackage = json.loads(f.read())

    make_definition_table(recordPackage,join(file_path,"record-package.csv"))
    
    make_definition_table(releasePackage,join(file_path,"release-package.csv"))
    
    make_definition_table(release,join(file_path,"release-identifier.csv"),what="definitions",section="Identifier")

    make_definition_table(release,join(file_path,"release-address.csv"),what="definitions",section="Address")

    make_definition_table(release,join(file_path,"release-organization.csv"),what="definitions",section="Organization")

    make_definition_table(release,join(file_path,"release-item.csv"),what="definitions",section="Item")
    
    make_definition_table(release,join(file_path,"release-milestone.csv"),what="definitions",section="Milestone")
    
    make_definition_table(release,join(file_path,"release-value.csv"),what="definitions",section="Value")