from rest_framework import serializers
from .models import Product, ProductRequest

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductRequestSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = ProductRequest
        fields = [
            'id', 'user', 'product', 'product_id',
            'quantity_requested', 'status', 'status_display', 'date_submitted'
        ]
        read_only_fields = ['user', 'status', 'date_submitted']

    def create(self, validated_data):
        # Associer product_id à product manuellement
        validated_data['product'] = validated_data.pop('product_id')
        return ProductRequest.objects.create(**validated_data)