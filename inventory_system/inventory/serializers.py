from rest_framework import serializers
from .models import Product, ProductRequest

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRequest
        fields = ['id', 'user', 'product', 'quantity_requested', 'status', 'date_submitted']
        read_only_fields = ['user', 'status', 'date_submitted']