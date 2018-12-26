from django.test import TestCase
import json
import numpy as np

from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from . import views
from .models import Bmi


class BmiTests(APITestCase):
    def test_bmi_calc(self):
        """
        Ensure we can create a new Bmi object with correct bmi_value.
        """
        count_before = Bmi.objects.count()
        factory = APIRequestFactory()
        request = factory.post('/bmicalc/', {"height":"20","mass":"10"}, format='json')
        response = views.bmi_calc(request)
        self.assertEqual(response.data, 0.03)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bmi.objects.count() - count_before, 1)
        self.assertEqual(Bmi.objects.last().bmi_value, 0.03)

    def test_bmi_stat(self):
        """
        Ensure we can correct calculate bmi statistics.
        """
        factory = APIRequestFactory()
        request = factory.get('/bmistat/')
        response = views.bmi_stat(request)
        bmi_array = np.array(Bmi.objects.values_list('bmi_value', flat=True))
        if len(bmi_array) == 0:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        else:
            responce_data = {}
            responce_data['avg'] = round(np.average(bmi_array), 2)
            responce_data['min'] = round(np.min(bmi_array), 2)
            responce_data['max'] = round(np.max(bmi_array), 2)
            responce_data['std'] = round(np.std(bmi_array), 2)     
            responce_data = json.dumps(responce_data) 
            self.assertEqual(response.data, responce_data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

  


        

