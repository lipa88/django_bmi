from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from bmi_app import views
from bmi_app.models import Bmi


class BmiCalcTests(APITestCase):
    def test_bmi_calc(self):
        """
        Ensure we can create a new Bmi object with correct bmi_value.
        """
        count_before = Bmi.objects.count()
        factory = APIRequestFactory()
        request = factory.post('/bmicalc/',
                               {"height": "20", "mass": "10"}, format='json')
        response = views.bmi_calc(request)
        self.assertEqual(response.data, 250.0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bmi.objects.count() - count_before, 1)
        self.assertEqual(Bmi.objects.last().bmi_value, 250.0)

    def test_bmi_calc_zero_division(self):
        """
        Ensure we can handle zero division in BMI calculation.
        """
        factory = APIRequestFactory()
        request = factory.post('/bmicalc/',
                               {"height": "0", "mass": "10"}, format='json')
        response = views.bmi_calc(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

