from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Min, Max, StdDev
import json
import math
import numpy as np

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import mixins, viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .models import Bmi
from .serializers import BmiSerializer


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


@api_view([ 'GET', ])
def bmi_stat(request):
    """
    Calculate bmi statistics.
    """
    if request.method == 'GET':
        try:
            bmi_array = np.array(Bmi.objects.values_list('bmi_value', flat=True))
            responce_data = {}
            responce_data['avg'] = round(np.average(bmi_array), 2)
            responce_data['min'] = round(np.min(bmi_array), 2)
            responce_data['max'] = round(np.max(bmi_array), 2)
            responce_data['std'] = round(np.std(bmi_array), 2)     
            return Response(json.dumps(responce_data), status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)




