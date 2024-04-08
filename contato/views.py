from django.shortcuts import render
from .models import Contato
from django.http import HttpResponse

# Create your views here.
def contact(request):
    if request.method=="POST":
        contact=Contato()
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        assunto=request.POST.get('assunto')
        contact.email=email
        contact.assunto=assunto
        contact.save()
        return HttpResponse("<h1>Obrigado por nos contatar!</h1>")
    return render(request, 'contact_summary.html')
