import xmltodict
import json
import yaml

with open ('sample.json','r') as jsonfile:
    pydict=json.load(jsonfile)
xmldata=xmltodict.unparse(pydict)
with open ('sample.xml','w') as xmlfile:
    xmlfile.write(xmldata)
yamldata=yaml.safe_dump(pydict)
with open ('sample.yaml','w') as yamlfile:
    yamlfile.write(yamldata)