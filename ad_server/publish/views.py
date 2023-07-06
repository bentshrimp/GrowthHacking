from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Ad, Slot, AdContract

class AdList(View):
    def get(self, request, slot_id):
        try:
            ad_num = Slot.objects.get(id=slot_id).ad_num
            ads = (
                Ad.objects.select_related("adcontract")
                .filter(adcontract__isnull=False, slot__id=slot_id)
                .order_by("adcontract__start_date")[:ad_num]
            )

            ad_values = ads.values(
                "id",
                "uri",
                "size",
                "target_link",
                "content_type",
                "slot__id",
                "adcontract__advertiser_id",
                "adcontract__price",
                "adcontract__start_date",
                "adcontract__end_date",
            )
            data = list(ad_values)
            return JsonResponse(data, safe=False)
        except:
            return HttpResponse("no data here")

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
