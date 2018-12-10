import xml.etree.ElementTree as ET
from turn2gs import turn2gs
def readXML(f):
    tree = ET.parse(f)
    root = tree.getroot()
    return root

def parseXML(tags,root):
    tagsNvalues = {}
    for child in root:
        childName = child.attrib['name']
        if childName in tags:
            tagsNvalues[childName] = child.text
    return tagsNvalues

root = readXML('strings.xml')

tags = ['default_web_client_id',
        'firebase_database_url',
        'project_id',
        'google_storage_bucket',
        'google_app_id',
        'google_api_key']

tagsNvalues = parseXML(tags,root)
print(tagsNvalues)


with open('google-services.json', 'w') as tf:
    tf.write(turn2gs(tagsNvalues))


#child.attrib['name'] gives string's name
#child.text gives string's text