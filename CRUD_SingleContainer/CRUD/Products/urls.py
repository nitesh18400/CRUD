from django.contrib import admin
from django.urls import path,include
from Products import views
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create_product,name='create_product'),
    path('retrieve/',views.retrive_product,name='retrive_product'),
    path('search/',views.search_product,name='search_product'),
]