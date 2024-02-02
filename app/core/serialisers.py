from rest_framework import serializers
from core.models import Material

class MaterialNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name']
        extra_kwargs = {}

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        extra_kwargs = {}