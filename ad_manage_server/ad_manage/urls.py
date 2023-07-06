from django.contrib import admin
from django.urls import path
from .views import AdListView, AdsListView


urlpatterns = [
    path('adList/', AdListView.as_view()),
    path('adsList/', AdsListView.as_view()),
]
