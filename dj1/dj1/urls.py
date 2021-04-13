
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('22/', views.jq1),
    path('222/', views.jq2),
    path('333/', views.jq2),
    path('342', views.index3),
    path('', views.index),
]
