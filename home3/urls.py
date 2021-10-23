from django.contrib import admin
from django.urls import path
from home3 import views
urlpatterns = [
    path('',views.index,name='index'),
    path('next',views.next,name='next'),
    path('login',views.login,name='login'),
    path('validate',views.validate,name='validate')
]