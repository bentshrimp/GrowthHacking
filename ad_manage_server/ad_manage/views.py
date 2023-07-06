from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        req = request.POST
        ad_id = req.get("ad_id")
        ad_uri = req.get("ad_uri")
        ad_size = req.get("ad_size")
        ad_target_link = req.get("ad_target_link")
        ad_content_type = req.get("ad_content_type")
        slot_id = req.get("slot_id")
        slot_ad_num = req.get("slot_ad_num")
        advertiser_id = req.get("advertiser_id")
        advertiser_name = req.get("advertiser_name")
        advertiser_phone = req.get("advertiser_phone")
        adContract_price = req.get("ad_price")
        adContract_start_date = req.get("ad_start_date")
        adContract_end_date = req.get("ad_end_date")

        slot = Slot(id=slot_id, ad_num=slot_ad_num)
        slot.save()
        ad = Ad(id=ad_id, uri=ad_uri, size=ad_size, target_link=ad_target_link,
                content_type=ad_content_type, slot=slot)
        ad.save()
        advertiser = Advertiser(
            id=advertiser_id, name=advertiser_name, phone=advertiser_phone)
        advertiser.save()
        adContract = AdContract(ad=ad, advertiser=advertiser, price=adContract_price,
                                start_date=adContract_start_date, end_date=adContract_end_date)
        adContract.save()
        
        return JsonResponse({"returnValue" : "true"})

    def put(self, request):
        pass

    def delete(self, request):
        pass
