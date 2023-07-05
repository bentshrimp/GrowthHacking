from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Ad, Slot, AdContract

class AdList(View):
    def get(self, request):
        return render(request, 'index.html', {})