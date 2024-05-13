from .favoritos import Favoritos

def favoritos(request):
    return {'favoritos': Favoritos(request)}