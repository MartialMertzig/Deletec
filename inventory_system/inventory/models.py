from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100) #Nom du produit
    description = models.TextField(blank=True) #Description du produit
    quantity = models.PositiveIntegerField() #Quantité
    price = models.DecimalField(max_digits=10, decimal_places=2) #Prix

    def __str__(self):
        return self.name 