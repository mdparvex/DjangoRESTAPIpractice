import requests

endpoint = 'http://127.0.0.1:8000/api/products/{{pk}}/delete/' #or localhost:800, change path to extract rsponse fromdifferent views

get_response = requests.delete(endpoint ) #HTTP request


#print(get_response.json())
print(get_response.status_code, get_response.status_code==405)