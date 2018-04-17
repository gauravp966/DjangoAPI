from rest_framework import serializers
from .models import emp

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = emp
        fields = '__all__'