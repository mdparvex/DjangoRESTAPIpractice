from django.shortcuts import render
import json
from django.http import JsonResponse


# Create your views here.
def api_home(request, *args, **kwargs):
    body=request.body #string of json data

    data={}
    try:
        data=json.loads(body) #convert string of json data to json dictionary
    except:
        pass

    data['params'] = dict(request.GET)
    data['headers']= dict(request.headers)
    data['content_type']= request.content_type
    print(data)
    return JsonResponse(data)
