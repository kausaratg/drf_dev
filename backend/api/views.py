from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    # print(request.GET)
    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # print(request.headers)
    # data['content_type'] = request.content_type
    # # return JsonResponse({"message": "Hi there this is your django api response"})
    # return JsonResponse(data)
    # if request.method != "POST":
    #     return Response({"detail":'Get not allowed'}, status=405)
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    # instance = Product.objects.all().order_by("?").last()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    # return Response(data)
