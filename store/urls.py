from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from .views import AdicionarComentarioView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_user/', views.update_user, name='update_user'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>',views.category, name='category'),
    path('category_summary/',views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
    path('meus-pedidos/', views.update_password, name='meus-pedidos'),
    path('produto/<int:produto_id>/adicionar_comentario/', AdicionarComentarioView.as_view(), name='adicionar_comentario'),

]
