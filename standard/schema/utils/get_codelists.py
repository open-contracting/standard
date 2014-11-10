#!/usr/bin/env python
import requests
from xml.dom import minidom
import StringIO
import csv


def fetch_codelist(name,url,lang="en"):
    output = []
    cl = requests.get(url)
    f = StringIO.StringIO(cl.content)
    csvData = csv.DictReader(f)

    output.append(["Category","Code","Title_"+ lang,"Description_"+lang,"Source"])
    for row in csvData:
        output.append([row.get("Category"),row.get("Code"),row.get("Title_"+lang),row.get("Description_"+lang),row.get("URL","")])
    
    return output

if __name__ == "__main__":
    from os.path import abspath, dirname, join

    schema_dir = dirname(dirname(abspath(__file__)))
    file_path = join(schema_dir,"codelists/")

    # Fetch codelists from the spreadsheet used to maintain them and output
    r = requests.get("https://spreadsheets.google.com/feeds/worksheets/1FEJr2A1pR2DnKCw24lj78TPBFs1HH0tiZmRnYhmwUFc/public/basic")

    xmldoc = minidom.parseString(r.content)
    itemlist = xmldoc.getElementsByTagName('entry') 

    for s in itemlist :
        listName = s.getElementsByTagName("title")[0].firstChild.nodeValue
        if not listName == "Codelists":
            for link in s.getElementsByTagName("link"):
                if link.attributes['rel'].nodeValue == "http://schemas.google.com/spreadsheets/2006#exportcsv":
                    listUrl = link.attributes['href'].nodeValue
                    table = fetch_codelist(listName,listUrl)
                    
                    with open(file_path + listName+".csv", 'wb') as f:
                        writer = csv.writer(f)
                        for row in table:
                            writer.writerow(row)
    
    iati = requests.get("http://iatistandard.org/codelists/downloads/clv2/csv/en/OrganisationRegistrationAgency.csv")
    with open(file_path + "organizationIdentifierRegistrationAgency_iati.csv", 'wb') as f:
        f.write(iati.content)