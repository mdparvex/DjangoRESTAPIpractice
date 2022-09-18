from rest_framework import generics
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductListCreateAPIview(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        #or i can write any condition
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title

        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

#method base view
@api_view(["POST", "GET"])
def product_alt_view(request, pk=None):

    if request.method=='GET':
        
        #url args
        #get request, detail view, list view
        if pk is not None:
            queryset = get_object_or_404(Products, pk=pk)
            data = ProductSerializer(queryset, many=False).data
            return Response(data)
        
        queryset = Products.objects.all()

        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if request.method=='POST':
        #create and update view
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raiseExceptions=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = title

            serializer.save(content=content)
        
            return Response(serializer.data)
        return Response({"invalid":"not valid"}, status=400)

