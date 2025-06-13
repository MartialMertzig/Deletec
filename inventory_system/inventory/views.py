from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenue dans le système de gestion d'inventaire !")

from rest_framework import viewsets
from.models import Product, Productrequest
from .serializers import ProductSerializer, ProductRequestSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRequestViewSet(viewsets.ModelViewSet):
    queryset = Productrequest.objects.all()
    serializer_class = ProductRequestSerializer
