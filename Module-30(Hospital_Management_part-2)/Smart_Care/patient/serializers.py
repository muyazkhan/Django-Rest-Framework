from rest_framework import serializers
from .models import Patient


class  patient(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model =  Patient
        fields = '__all__'
        # fields = ['name', 'phone', 'problem']
