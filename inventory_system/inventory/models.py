from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100) #Nom du produit
    description = models.TextField(blank=True) #Description du produit
    quantity = models.PositiveIntegerField() #Quantité
    price = models.DecimalField(max_digits=10, decimal_places=2) #Prix

    def __str__(self):
        return self.name 
    
from django.db import models
from django.contrib.auth.models import User
from .models import Product

class Productrequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('approved', 'Approuvée'),
        ('rejected', 'Refusée'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_requested = models.PositiveIntgerField()
    status = models.CharField(max_lenght=10, choices=STATUS_CHOICES, default='pending')
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.status})"