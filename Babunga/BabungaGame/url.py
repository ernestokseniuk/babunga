from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('api/register',views.register,name='register')
]
