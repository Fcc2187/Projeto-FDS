from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product, Profile
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, 'cart_summary.html', {"cart_products": cart_products, "quantities": quantities, "totals": totals})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, "Produto adicionado com sucesso.")
        return response
    else:
        messages.success(request, "Você precisa estar logado para adicionar esse produto.")
        return redirect('home')

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        messages.success(request, "Produto removido do carrinho.")
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty': product_qty})
        messages.success(request, "Seu carrinho foi atualizado.")
        return response

def cart_buy(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, 'buy.html', {"cart_products": cart_products, "quantities": quantities, "totals": totals})

def buy_done(request):
    if 'session_key' in request.session:
        del request.session['session_key']
        request.session.modified = True
    return render(request, 'buy_done.html', {'message': 'Obrigado pela compra, seu pedido será enviado para seu endereço!'})

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request, 'checkout.html', {"cart_products": cart_products, "quantities": quantities, "totals": totals})

@csrf_exempt
def process_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Assume the payment is successful
        cart = Cart(request)
        for product_id in cart.get_ids():
            cart.delete(product=product_id)

        messages.success(request, "Pagamento realizado com sucesso!")
        return redirect(reverse('buy_done'))

    return redirect('checkout')
