from logging import raiseExceptions
from django.shortcuts import render
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Products
#API view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


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

@api_view(["GET"])
def get_api(request):
    #API view
    model_data = Products.objects.all().order_by('?').first()
    data= {}
    if model_data:

        #data = model_to_dict(model_data) #fields=['id','title'] can specify inside model_to_dict

        #data['id'] = model_data.id
        #data['title'] = model_data.title
        #data['content'] = model_data.content
        #data['price'] = model_data.price

        #model instance (model data)
        #turn a python dict
        #return JSONtomy client

        data = ProductSerializer(model_data).data

    return Response(data)

@api_view(["POST"])
def post_api(request):
    #API view
    
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raiseExceptions=True):
        serializer.save()
        
        return Response(serializer.data)
    return Response({"invalid":"not valid"}, status=400)
