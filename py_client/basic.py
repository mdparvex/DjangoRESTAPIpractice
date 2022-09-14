import requests

endpoint= "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint) #HTTP request
print(get_response.text) # source code or text raw response