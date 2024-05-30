from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.favoritos_summary, name="favoritos_summary"),
    path('favoritos_add/', views.favoritos_add, name="favoritos_add"),
    path('favoritos_delete/', views.favoritos_delete, name="favoritos_delete"),
]