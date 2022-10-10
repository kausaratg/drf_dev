import requests
endpoint = "http://127.0.0.1:8000/api/products/100"

get_requests = requests.get(endpoint)

print(get_requests.json())