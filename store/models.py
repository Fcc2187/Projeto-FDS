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

class Favoritos():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        favoritos = self.session.get('session_key')

        if 'session_key' not in request.session:
            favoritos = self.session['session_key'] = {}

        self.favoritos = favoritos
    
    def favoritos_add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.favoritos:
            # Se o produto já estiver nos favoritos, você pode atualizar sua quantidade aqui se necessário
            pass
        else:
            # Se o produto não estiver nos favoritos, adicione-o ao dicionário de favoritos com a quantidade especificada
            self.favoritos[product_id] = quantity  # Defina a quantidade do produto aqui
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            
            favorito = str(self.favoritos)
            favorito = favorito.replace("\'", "\"")
            current_user.update(antigo_favoritos=str(favorito))

    def get_prods(self):
        product_ids = self.favoritos.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def __len__(self):
        return len(self.favoritos)
        
    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/favoritos
        if product_id in self.favoritos:
            del self.favoritos[product_id]

        self.session.modified = True

        # Verificar se o usuário está autenticado
        if self.request.user.is_authenticated:
            # Obter o usuário autenticado
            user = User.objects.get(id=self.request.user.id)

            # Atualizar os favoritos do usuário
            user.profile.antigo_favoritos = str(self.favoritos)
            user.profile.save()



    