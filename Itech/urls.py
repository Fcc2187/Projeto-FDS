from . import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/',include('cart.urls')),
    path('contato/', include('contato.urls')),
    path('payment/', include('payment.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
