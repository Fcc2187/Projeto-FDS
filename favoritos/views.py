from django.shortcuts import render, get_object_or_404, redirect
from .favoritos import Favoritos
from store.models import Product
from django.http import JsonResponse,HttpResponse
from django.contrib import messages

def favoritos_summary(request):
    favoritos = Favoritos(request)
    favoritos_products = favoritos.get_prods
    quantities = favoritos.get_quants
    totals = favoritos.favoritos_total()
    return render(request,'favoritos_summary.html', {"favoritos_products":favoritos_products, "quantities":quantities, "totals":totals})


def favoritos_add(request):
        favoritos = Favoritos(request)
        if request.POST.get('action')=='post':
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            product =  get_object_or_404(Product,id=product_id)
            favoritos.add(product=product, quantity=product_qty)
            favoritos_quantity = favoritos.__len__()
            # response = JsonResponse({"Product name: ": product.name})
            response = JsonResponse({'qty': favoritos_quantity})
            messages.success(request, ("Produto adicionado com sucesso."))
            return redirect('home')
        else:
            messages.success(request, "Você precisa estar logado para adicionar esse produto.")
            return redirect('home')

def favoritos_delete(request):
    favoritos = Favoritos(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        favoritos.delete(product=product_id)
        response = JsonResponse({'product': product_id})
        messages.success(request, ("Produto removido do carrinho."))
        return response

