from .cart import Cart
from store.models import Favoritos

def cart(request):
    return {'cart': Cart(request)}

def favoritos(request):
    favoritos = Favoritos(request)
    return {'favoritos': favoritos}