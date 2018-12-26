from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bmicalc/', views.bmi_calc, name="bmi-calculation"),
    url(r'bmistat/', views.bmi_stat, name="bmi-statistics"),
]
