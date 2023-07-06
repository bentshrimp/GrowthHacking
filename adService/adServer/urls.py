from django.urls import path
from .views import AdList, AdsList

urlpatterns = [
    path('adList/<int:slot_id>/', AdList.as_view()),
    path('adsList/', AdsList.as_view()),
]
