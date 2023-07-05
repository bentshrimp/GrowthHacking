from django.contrib import admin
from django.urls import path
from .views import AdList


urlpatterns = [
    path('', AdList.as_view())
]
