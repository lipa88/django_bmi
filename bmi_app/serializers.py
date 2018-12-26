from rest_framework import serializers
from .models import Bmi


class BmiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bmi
        fields = '__all__'
        extra_kwargs = {'bmi_value': {'required': False}}
    
    def validate_height(self, value):
        if value <= 0:
            raise serializers.ValidationError('Height must be greater than 0.')
        return value

    def create(self, validated_data):
        m = validated_data['mass']
        # height is in cm, but should be in meters
        h = validated_data['height'] / 100  
        validated_data['bmi_value'] = round(m / (h ** 2), 2)
        return super(BmiSerializer, self).create(validated_data)
