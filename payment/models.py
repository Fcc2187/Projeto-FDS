from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    endereco1 = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)#Hellcife
    estado = models.CharField(max_length=200, null=True , blank=True)#Pirocambuco
    codigo_postal = models.CharField(max_length=200, null=True , blank=True)#69
    pais = models.CharField(max_length=200)#Bostil

    class meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'Shipping Address - {str(self.id)}'