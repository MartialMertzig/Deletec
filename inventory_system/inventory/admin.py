from django.contrib import admin
from .models import Product, ProductRequest

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')  
    search_fields = ('name',)                     
    list_filter = ('quantity',)                   

@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity_requested', 'status', 'date_submitted')
    search_fields = ('user__username', 'product__name')
    list_filter = ('status', 'date_submitted')