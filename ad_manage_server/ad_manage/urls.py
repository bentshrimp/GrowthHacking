from django.contrib import admin
from django.urls import path
from .views import HomeView, AdsListView


urlpatterns = [
    path('', HomeView.as_view()),
    path('adsList/<int:ad_id>', AdsListView.as_view()),
    path('adsList/', AdsListView.as_view()),
]
