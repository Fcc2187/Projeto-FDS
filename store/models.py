from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    Numero = models.CharField(max_length = 20, blank = True)
    Endereço1 = models.CharField(max_length=200, blank=True)
    Endereço2 = models.CharField(max_length=200, blank=True)
    Cidade = models.CharField(max_length=200, blank=True)
    Estado = models.CharField(max_length=200, blank=True)
    CEP = models.CharField(max_length=200, blank=True)
    País = models.CharField(max_length=200, blank=True)
    antigo_carrinho = models.CharField(max_length=200, blank=True, null=True)
    antigo_favoritos = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username 

def create_profile(sender, instance, created, **kwards):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
    
post_save.connect(create_profile, sender=User)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0 , decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1 )
    description = models.CharField(max_length=300, default= '', blank=True, null=True)
    image = models.ImageField(upload_to= 'uploads/product/')
    # sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 , decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    costumer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    adress= models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=12,default= '+5581999999999')
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def _str_ (self):
        return self.product
    

    