import xml.etree.ElementTree as ET
import sys
from turn2gs import turn2gs

try:
    tree = ET.parse('strings.xml')
except FileNotFoundError:
    print("Can not find 'strings.xml'")
    sys.exit()

root = tree.getroot()

def parseXML(tags,root):
    tagsNvalues = {}
    for child in root:
        childName = child.attrib['name']
        if childName in tags:
            tagsNvalues[childName] = child.text
    return tagsNvalues


tags = ['default_web_client_id',
        'firebase_database_url',
        'project_id',
        'google_storage_bucket',
        'google_app_id',
        'google_api_key']

tagsNvalues = parseXML(tags,root)
print(tagsNvalues)



try:
    with open('google-services.json', 'w') as tf:
        tf.write(turn2gs(tagsNvalues))
except PermissionError:
    print('No permission to write "google-services.json"')

#child.attrib['name'] gives string's name
#child.text gives string's text
