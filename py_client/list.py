import requests

endpoint = 'http://127.0.0.1:8000/api/products/' #or localhost:800, change path to extract rsponse fromdifferent views

get_response = requests.get(endpoint ) #HTTP request


print(get_response.json())
print(get_response.status_code)