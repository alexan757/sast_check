import requests

api_key = "YOUR_API_KEY"

def get_data():
    url = "https://api.example.com/data"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

data = get_data()

import xml.etree.ElementTree as ET

xml_data = """
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>
    <data>&xxe;</data>
</root>
"""

def process_xml():
    root = ET.fromstring(xml_data)
    data = root.find("data").text
    return data

result = process_xml()
print(result)
