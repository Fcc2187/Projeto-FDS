from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.cart_summary, name="cart_summary"),
    path('add/', login_required(views.cart_add), name="cart_add"),
    path('delete/', views.cart_delete, name="cart_delete"),
    path('update/', views.cart_update, name="cart_update"),
    path('buy/', views.cart_buy, name="buy"),
    path('buy_done/', views.buy_done, name="buy_done"),
    path('checkout/', views.checkout, name='checkout'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('meus_pedidos/', views.meus_pedidos, name='meus_pedidos')
]
