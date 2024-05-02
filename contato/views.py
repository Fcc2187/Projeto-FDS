from django.shortcuts import render, redirect
from .models import Contato, Complaint
from django.urls import reverse

# Create your views here.
def contact(request):
    if request.method == "POST":
        contact = Contato()
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        contact.email = email
        contact.nome = nome
        contact.assunto = assunto
        contact.save()
        
        # Redirecionar para a página de reclamações com informações de contato
        return redirect(reverse('complaints') )
        
    return render(request, 'contact_summary.html')

def complaints(request):
     complaints = Contato.objects.all()
     return render(request, 'complaints.html', {'complaints': complaints})
