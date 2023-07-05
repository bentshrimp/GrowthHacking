from django.urls import path
from .views import Send_event

urlpatterns = [
    path('', Send_event.as_view()),
]
