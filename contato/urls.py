from django.urls import path, include
from . import views

from contato.views import contact

urlpatterns = [

    path('contato/', views.contact, name="contact_summary"),
    path('complaints/', views.complaints, name='complaints'),

]