from django.shortcuts import render
import json
from django.http import HttpRequest, JsonResponse
from django.views import View


class Send_event(View):
    def post(self, request):
        data = {
            "returnValue": "true",
        }
        return JsonResponse(data)
