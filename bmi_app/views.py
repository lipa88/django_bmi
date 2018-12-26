from django.http import JsonResponse
import json
import numpy as np

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .models import Bmi
from .serializers import BmiSerializer


@api_view(['POST'])
def bmi_calc(request):
    """
    Calculate BMI and add new Bmi object to database.
    """
    serializer = BmiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data["bmi_value"], status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET'])
def bmi_stat(request):
    """
    Calculate BMI statistics.
    """
    bmi_array = np.array(Bmi.objects.values_list('bmi_value', flat=True))
    if len(bmi_array) == 0:
        return Response(status=status.HTTP_204_NO_CONTENT)
    response_data = {}
    response_data['avg'] = round(np.mean(bmi_array), 2)
    response_data['min'] = round(np.min(bmi_array), 2)
    response_data['max'] = round(np.max(bmi_array), 2)
    response_data['std'] = round(np.std(bmi_array), 2)     
    return Response(json.dumps(response_data), status=status.HTTP_200_OK)
