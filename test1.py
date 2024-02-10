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
print(data)
