from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse,HttpResponse
from django.contrib import messages


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request,'cart_summary.html', {"cart_products":cart_products, "quantities":quantities, "totals":totals})

def cart_add(request):
        cart = Cart(request)
        if request.POST.get('action')=='post':
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            product =  get_object_or_404(Product,id=product_id)
            cart.add(product=product, quantity=product_qty)
            cart_quantity = cart.__len__()
            # response = JsonResponse({"Product name: ": product.name})
            response = JsonResponse({'qty': cart_quantity})
            messages.success(request, ("Produto adicionado com sucesso."))
            return response
        else:
            messages.success(request, "Você precisa estar logado para adicionar esse produto.")
            return redirect('home')
    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete function in cart
        cart.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        # return redirect('cart_summary')
        messages.success(request, ("Produto removido do carrinho."))
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        # return redirect('cart_summary')
        messages.success(request, ("Seu carrinho foi atualizado."))
        return response

def cart_buy(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request,'buy.html', {"cart_products":cart_products, "quantities":quantities, "totals":totals})

def buy_done(request):
    if 'session_key' in request.session:
        del request.session['session_key']
        request.session.modified = True

    return render(request, 'buy_done.html', {'message': 'Obrigado pela compra, estamos avaliando seu pedido'})