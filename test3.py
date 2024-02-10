import requests

internal_url = "http://43.56.10.200/api/data"

def get_internal_data():
    response = requests.get(internal_url)
    return response.json()

data = get_internal_data()
print(data)
