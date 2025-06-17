from rest_framework import serializers
from .models import Product, ProductRequest

# Serializer pour le modèle Product (Produits)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' #Tout inclure car chaque champ peut être utile côté client

# Serializer pour les ProductRequest (Demandes de produits)
class ProductRequestSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    ) # Affiche le statut (En attente etc.)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = ProductRequest
        fields = [
            'id', 'user', 'product', 'product_id',
            'quantity_requested', 'status', 'status_display', 'date_submitted'
        ] # Champs non éditables côté client
        read_only_fields = ['user', 'status', 'date_submitted']

    def create(self, validated_data):
        # Remplace product_id par product
        validated_data['product'] = validated_data.pop('product_id')
        return ProductRequest.objects.create(**validated_data)