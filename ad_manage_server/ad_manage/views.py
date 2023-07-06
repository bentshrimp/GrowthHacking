from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views import View
from .models import Ad, Slot, AdContract, Advertiser
from django.db.models import F

class AdList(View):
    def get(self, request):
        return render(request, 'manager_platform.html', {})
    
class AdsList(View):
    # AD ID, advertiser_ID, advertiser_name, start_date, end_date(계약 시작,종료날짜), target_link
    def get(self, request):
        data = []

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

        for ad in rows:
            ad_data = {
                "id": ad["id"],
                "advertiser_id": ad["adcontract__advertiser__id"],
                "advertiser_name": ad["adcontract__advertiser__name"],
                "start_date": str(ad["adcontract__start_date"]),
                "end_date": str(ad["adcontract__end_date"]),
                "target_link": ad["target_link"],
            }
            data.append(ad_data)
        
        response = JsonResponse(data, safe=False)

        return response

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request, ad_id):
        try:
            AdContract.objects.get(ad_id=ad_id).delete()
            Ad.objects.get(id=ad_id).delete()
            return JsonResponse({"returnValue" : "true"})
        except:
            return JsonResponse({"returnValue" : "false"})
