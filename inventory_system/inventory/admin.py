from django.contrib import admin
from .models import Product, ProductRequest

#Enregistrement des produits dans l'admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price') #Infos produit
    search_fields = ('name',) #Permet de cherche les produits par leur nom si la liste devient trop longue                     
    list_filter = ('quantity',) #Permet de filtrer par quantité             

#Enregistrement des demandes produits dans l'admin
@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity_requested', 'status', 'date_submitted') #Informations liées à la demande client
    search_fields = ('user__username', 'product__name') #Recherche par nom utilisateur
    list_filter = ('status', 'date_submitted') #Filtre par status et date de soumission