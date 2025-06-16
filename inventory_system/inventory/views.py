from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Product, ProductRequest
from .serializers import ProductSerializer, ProductRequestSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Vue de la page d'accueil
def index(request):
    return HttpResponse("Bienvenue dans le système de gestion d'inventaire !")

# Vue des API produits
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vue des API demandes de produits
class ProductRequestViewSet(viewsets.ModelViewSet):
    queryset = ProductRequest.objects.all()
    serializer_class = ProductRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ProductRequest.objects.all()
        return ProductRequest.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Vue de la liste de produits pour l'utilisateur connecté
@login_required
def product_list(request):
    products = Product.objects.all()
    demandes = ProductRequest.objects.filter(user=request.user)

    if request.method == 'POST':
        produit_id = request.POST.get('product')
        quantite = request.POST.get('quantite')

        if produit_id and quantite:
            try:
                produit = Product.objects.get(id=produit_id)
                quantite = int(quantite)
                if quantite > 0:
                    ProductRequest.objects.create(
                        user=request.user,
                        product=produit,
                        quantity_requested=quantite
                    )
                    return redirect('product-list')
            except Product.DoesNotExist:
                print("Produit inexistant")
            except Exception as e:
                print("Erreur :", e)

    return render(request, 'liste_produit.html', {
        'products': products,
        'demandes': demandes
    })