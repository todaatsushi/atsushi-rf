from django.contrib import admin
from django.urls import path, include

from home.views import home_page, test

urlpatterns = [
    path('', home_page, name='home-page')
]
