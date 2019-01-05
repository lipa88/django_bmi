import numpy as np

from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from bmi_app import views
from bmi_app.models import Bmi


class BmiStatTests(APITestCase):
    def setUp(self):
        Bmi.objects.create(height=20.00, mass=10.00, bmi_value=250.0)
        Bmi.objects.create(height=25.00, mass=10.00, bmi_value=160.0)
        Bmi.objects.create(height=215.00, mass=90.00, bmi_value=19.47)

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
            response_data = '{"avg": 143.16, "min": 19.47, "max": 250.0, "std": 94.86}'
            self.assertEqual(response.data, response_data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

