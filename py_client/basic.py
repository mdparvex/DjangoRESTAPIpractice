import requests

#endpoint= "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"

endpoint = 'http://127.0.0.1:8000/api/hello' #or localhost:800, change path to extract rsponse fromdifferent views

#get_response = requests.get(endpoint, params={"abc":123}, json={"query":"hello world"}) #HTTP request
get_response = requests.post(endpoint, json={"title":None,"content":"hello world"}) #HTTP request
#print(get_response.text) # source code or text raw response

#HTTP request send -> HTML
#REST API request sends -.=> Json

print(get_response.json())
print(get_response.status_code)