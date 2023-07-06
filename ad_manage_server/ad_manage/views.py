from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Ad
from django.db.models import F


class HomeView(View):
    def get(self, request) -> HttpResponse:
        return render(request, "manager_platform.html", {})


class AdsListView(View):
    def get(self, request) -> JsonResponse:
        rows = Ad.objects.select_related("adcontract", "adcontract__advertiser").values(
            "id",
            "uri",
            "size",
            "target_link",
            "content_type",
            "slot",
            "adcontract__price",
            "adcontract__start_date",
            "adcontract__end_date",
            "adcontract__advertiser__id",
            "adcontract__advertiser__name",
            "adcontract__advertiser__phone",
        )

        data = [
            {
                "id": ad["id"],
                "advertiser_id": ad["adcontract__advertiser__id"],
                "advertiser_name": ad["adcontract__advertiser__name"],
                "start_date": str(ad["adcontract__start_date"]),
                "end_date": str(ad["adcontract__end_date"]),
                "target_link": ad["target_link"],
            }
            for ad in rows
        ]

        return JsonResponse(data, safe=False)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
