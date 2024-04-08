from django.db import models
import datetime

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
