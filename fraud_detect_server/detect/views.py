from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Event, User


class Send_event(View):
    def post(self, request):
        # todo - request body를 db에 insert
        try:
            req = request.POST
            print(req)
            u = User(ip = req.get("user_ip"), agent=req.get("agent"), location=req.get("location"))
            u.save()
            Event(type = req.get("type"), start_time=req.get("start_time"), end_time=req.get("end_time"), user_ip=u, cursor_x_pos=req.get("cursor_x_pos"), cursor_y_pos=req.get("cursor_y_pos")).save()
            return JsonResponse({"returnValue" : "true"})
        except:
            return JsonResponse({"returnValue" : "false"})
