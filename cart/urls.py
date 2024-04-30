from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.cart_summary, name="cart_summary"),
    path('add/',login_required(views.cart_add), name="cart_add"),
    path('delete/',views.cart_delete, name="cart_delete"),
    path('update/',views.cart_update, name="cart_update"),
]