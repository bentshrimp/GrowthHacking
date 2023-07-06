from django.contrib import admin
from django.urls import path
from .views import AdList, AdsList


urlpatterns = [
    path('adList/', AdList.as_view()),
    path('adsList/', AdsList.as_view()),
    path('adsList/<int:ad_id>', AdsList.as_view()),
]
