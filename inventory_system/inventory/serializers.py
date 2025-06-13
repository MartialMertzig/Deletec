from rest_framework import serializers
from .models import Product, Productrequest

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productrequest
        fields = '__all__'