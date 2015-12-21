#!/usr/bin/env python
import json
import csv
import collections
import re

def format(text):
    return re.sub(r'\[([^\[]+)\]\(([^\)]+)\)', r'`\1 <\2>`__', text.replace("date-time","[date-time](#date)"))

def make_link(text):
    if "http" in text:
        return format("["+text.split("/")[-1]+"]("+text+")")
    else:
        text = text.replace("#/definitions/","")
        return format("["+text+"](#"+text.lower()+")")
        

def make_definition_table(json,file_path,what="properties",section=""): 
    table = [['Field Name','Description','Format']]
    if(section):
        if "/" in section:
            block = json[what][section.split("/")[0]]["properties"][section.split("/")[1]]["properties"]
        else:
            block = json[what][section]["properties"]
    else:
        block = json[what]

    
    for prop in block:
        types = block[prop].get('type','')
        if isinstance(types,list):
            types = format(", ".join(types).replace(", null","").replace("null,",""))
        else:
            types = format(types)
            

        if types == "array":
           if block[prop].get('items').get("$ref"):
               table.append([prop,format(block[prop].get('description','')) + " See " + make_link(block[prop]['items']["$ref"]) + " section for further details.","Object Array"])
           else:
               table.append([prop,format(block[prop].get('description','')),"Array"])
        elif block[prop].get("$ref"):
          table.append([prop,format(block[prop].get('description','')) + " See " + make_link(block[prop]["$ref"]),"Reference"])
        elif "object" in types:
            table.append([prop,format(block[prop].get('description','')) + " See " + make_link(prop),"Object"])
        else:
          table.append([prop,format(block[prop].get('description','')),block[prop].get('format','') + " " + types])
          
        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            for row in table:
                writer.writerow(row)


if __name__ == "__main__":
    from os.path import abspath, dirname, join

    schema_dir = dirname(dirname(abspath(__file__)))
    file_path = join(schema_dir,"../docs/field_definitions/")
    
    with open(join(schema_dir, 'release-schema.json'), 'r') as f:
        release = json.loads(f.read(),object_pairs_hook=collections.OrderedDict)

    with open(join(schema_dir, 'release-package-schema.json'), 'r') as f:
        releasePackage = json.loads(f.read(),object_pairs_hook=collections.OrderedDict)

    with open(join(schema_dir, 'record-package-schema.json'), 'r') as f:
        recordPackage = json.loads(f.read(),object_pairs_hook=collections.OrderedDict)

    make_definition_table(recordPackage,join(file_path,"record-package.csv"))
    
    make_definition_table(releasePackage,join(file_path,"release-package.csv"))
    
    make_definition_table(release,join(file_path,"release-toplevel.csv"))

    make_definition_table(release,join(file_path,"release-tender.csv"),what="definitions",section="Tender")
    
    make_definition_table(release,join(file_path,"release-planning.csv"),what="definitions",section="Planning")
    
    make_definition_table(release,join(file_path,"release-award.csv"),what="definitions",section="Award")
    
    make_definition_table(release,join(file_path,"release-contract.csv"),what="definitions",section="Contract")    

    make_definition_table(release,join(file_path,"release-implementation.csv"),what="definitions",section="Implementation")    

    make_definition_table(release,join(file_path,"release-transaction.csv"),what="definitions",section="Transaction")

    make_definition_table(release,join(file_path,"release-budget.csv"),what="definitions",section="Budget")
    
    make_definition_table(release,join(file_path,"release-identifier.csv"),what="definitions",section="Identifier")

    make_definition_table(release,join(file_path,"release-address.csv"),what="definitions",section="Address")
    
    make_definition_table(release,join(file_path,"release-contact-point.csv"),what="definitions",section="ContactPoint")

    make_definition_table(release,join(file_path,"release-organization.csv"),what="definitions",section="Organization")

    make_definition_table(release,join(file_path,"release-item.csv"),what="definitions",section="Item")
    
    make_definition_table(release,join(file_path,"release-item-unit.csv"),what="definitions",section="Item/unit")
    
    make_definition_table(release,join(file_path,"release-period.csv"),what="definitions",section="Period")
    
    make_definition_table(release,join(file_path,"release-milestone.csv"),what="definitions",section="Milestone")
    
    make_definition_table(release,join(file_path,"release-value.csv"),what="definitions",section="Value")

    make_definition_table(release,join(file_path,"release-identifier.csv"),what="definitions",section="Identifier")
    
    make_definition_table(release,join(file_path,"release-classification.csv"),what="definitions",section="Classification")
    
    make_definition_table(release,join(file_path,"release-document.csv"),what="definitions",section="Document")
