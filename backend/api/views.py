from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"response not okay"}, status=400)

