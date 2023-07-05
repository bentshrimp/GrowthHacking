from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Ad, Slot, AdContract


class AdList(View):
    def get(self, request, slot_id):
        try:
            ad_num = Slot.objects.get(id=slot_id).ad_num
            ads = Ad.objects.select_related('adcontract').filter(
                adcontract__isnull=False, slot__id=slot_id).order_by('adcontract__start_date')[:ad_num]
        # test
        # for ad in ads:
        #     print(f"Ad ID: {ad.id}")
        #     print(f"Ad URI: {ad.uri}")
        #     print(f"Ad Size: {ad.size}")
        #     print(f"Ad Target Link: {ad.target_link}")
        #     print(f"Ad Content Type: {ad.content_type}")
        #     print(f"Ad Slot ID: {ad.slot_id}")

        #     ad_contract = ad.adcontract
        #     print(f"Ad Contract Advertiser ID: {ad_contract.advertiser_id}")
        #     print(f"Ad Contract Price: {ad_contract.price}")
        #     print(f"Ad Contract Start Date: {ad_contract.start_date}")
        #     print(f"Ad Contract End Date: {ad_contract.end_date}")

            ad_values = ads.values('id', 'uri', 'size', 'target_link', 'content_type', 'slot__id',
                               'adcontract__advertiser_id', 'adcontract__price', 'adcontract__start_date', 'adcontract__end_date')
            data = list(ad_values)
            return JsonResponse(data, safe=False)
        except:
            return HttpResponse("no data here")
