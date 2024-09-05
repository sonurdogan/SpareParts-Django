from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path('product/<int:pk>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('offer/', views.offer, name='offer'),
]