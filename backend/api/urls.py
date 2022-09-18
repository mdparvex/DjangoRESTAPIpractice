from django.urls import path
from . import views

urlpatterns =[
    path('', views.api_home),
    path('get', views.get_api),
    path('post', views.post_api)
    ]