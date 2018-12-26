from rest_framework import serializers
from .models import Bmi


class BmiSerializer(serializers.ModelSerializer):
    bmi_value = serializers.SerializerMethodField()

    class Meta:
        model = Bmi
        fields = '__all__'
    
    def get_bmi_value(self, instance):
        return round(instance.mass / (instance.height ** 2 ), 2)
    
    def create(self, validated_data):
        validated_data['bmi_value'] = round(validated_data['mass'] / (validated_data['height'] ** 2), 2)
        return super(BmiSerializer, self).create(validated_data)




