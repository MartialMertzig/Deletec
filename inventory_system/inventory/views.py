from django.http import HttpResponse
from rest_framework import viewsets, permissions # Permet de définir les permissions
from.models import Product, Productrequest
from .serializers import ProductSerializer, ProductRequestSerializer
from django.shortcuts import render

#Vue de la page d'accueil

def index(request):
    return HttpResponse("Bienvenue dans le système de gestion d'inventaire !")

#Vue des API produits

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] # Permet de restreindre l'accès aux utilisateurs connectés

#Vue des API demandes de produits

class ProductRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ProductRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

def get_queryset(self):
    user = self.request.user
    if user.is_staff:
        return Productrequest.objects.all()
    return Productrequest.objects.filter(user=user)

def perform_create(self, serializer):
    serializer.save(user=self.request.user)

#Vue de la page liste produit

def liste_produit(request):
    return render(request, 'liste_produit.html')