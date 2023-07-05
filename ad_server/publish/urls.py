from django.urls import path
from .views import AdList

urlpatterns = [
    path('adList/<int:slot_id>/', AdList.as_view()),
]
