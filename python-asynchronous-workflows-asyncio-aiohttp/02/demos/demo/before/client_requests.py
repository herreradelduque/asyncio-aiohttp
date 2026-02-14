import requests

API_URLS = [
    "http://localhost:8080/names/1",
    "http://localhost:8080/names/2",
]

 for url in API_URLS:
    response = requests.get(url)
    print(response.json())
