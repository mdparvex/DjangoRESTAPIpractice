import requests

endpoint= "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"hello world"}) #HTTP request
print(get_response.text) # source code or text raw response

#HTTP request send -> HTML
#REST API request sends -.=> Json

print(get_response.json())