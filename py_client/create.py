import requests

endpoint = 'http://127.0.0.1:8000/api/products/' #or localhost:800, change path to extract rsponse fromdifferent views

'''
i can post data from here
data = {
    'title': 'hello'
    'description':'fine'
    'price':30.99
}
get_response = requests.post(endpoint , json=data)
'''
get_response = requests.post(endpoint ) #HTTP request



print(get_response.json())
print(get_response.status_code)