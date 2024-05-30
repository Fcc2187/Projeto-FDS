from store.models import Product, Profile

class Favoritos:
    
    def __init__(self, request):
        self.session = request.session
        self.request = request
        favoritos = self.session.get('favoritos', {})

        if 'favoritos' not in request.session:
            favoritos = self.session['favoritos'] = {}

        self.favoritos = favoritos


    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        if product_id  in self.favoritos:
            pass
        else:
            #self.favoritos[product_id] = {'price': str(product.price)}
            self.favoritos[product_id] = int(product_qty)
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            favoritosy = str(self.favoritos)
            favoritosy = favoritosy.replace("\'", "\"")
            current_user.update(antigo_favoritos=str(favoritosy))
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id  in self.favoritos:
            pass
        else:
            #self.favoritos[product_id] = {'price': str(product.price)}
            self.favoritos[product_id] = int(product_qty)
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            favoritosy = str(self.favoritos)
            favoritosy = favoritosy.replace("\'", "\"")
            current_user.update(antigo_favoritos=str(favoritosy))

    def favoritos_total(self):
        # Pegar a ID dos produtos
        product_ids = self.favoritos.keys()
        # Procurar por essas keys no banco de dados dos produtos
        products = Product.objects.filter(id__in=product_ids)
        # Conseguir quantidades
        quantities = self.favoritos
        # Inicia contagem em 0
        total = 0

        for key, value in quantities.items():
            # Converte key string em inteiro
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total  

    def __len__(self):
        return len(self.favoritos)
    
    def get_prods(self):
        product_ids = self.favoritos.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.favoritos
        return quantities
    
    def delete(self,product):
        product_id= str(product)
        #delete from dictionary/favoritos
        if product_id in self.favoritos:
            del self.favoritos[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            favoritosy = str(self.favoritos)
            favoritosy = favoritosy.replace("\'", "\"")
            current_user.update(antigo_favoritos=str(favoritosy))
