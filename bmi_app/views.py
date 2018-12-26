from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Min, Max, StdDev
import json
import math

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import mixins, viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .models import Bmi
from .serializers import BmiSerializer, BmiStatSerializer 


@api_view([ 'POST', ])
def bmi_calc(request):
    """
    Calculate and create new bmi object.
    """
    if request.method == 'POST':
        serializer = BmiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data["bmi_value"], status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


def std_dev(x_list, x_avg):
    """
    Calculate StdDev (StdDev doesn't exist in sqlite).
    """
    x_sum = 0
    for x in x_list:
        x_sum += ( x - x_avg ) ** 2
    n = len(x_list)
    return math.sqrt( x_sum / (n - 1) )


@api_view([ 'GET', ])
def bmi_stat(request):
    """
    Calculate bmi statistics.
    """
    if request.method == 'GET':
        try:
            queryset = Bmi.objects.all()
            responce_data = {}
            responce_data['avg'] = round(queryset.aggregate(Avg('bmi_value'))['bmi_value__avg'], 2)
            responce_data['min'] = round(queryset.aggregate(Min('bmi_value'))['bmi_value__min'], 2)
            responce_data['max'] = round(queryset.aggregate(Max('bmi_value'))['bmi_value__max'], 2)
            x_list = [i['bmi_value'] for i in queryset.values()]
            responce_data['std'] = round(std_dev(x_list, responce_data['avg']), 2)      
            return Response(json.dumps(responce_data), status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)




