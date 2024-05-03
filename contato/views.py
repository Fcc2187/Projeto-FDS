from django.shortcuts import render, redirect
from .models import Contato
from django.urls import reverse
from django.db.models import Q

def contact(request):
    if request.method == "POST":
        # Obtém o assunto do formulário POST
        assunto = request.POST.get('assunto')
        
        # Cria uma nova instância de Contato associada ao usuário atual
        contato = Contato.objects.create(user=request.user, assunto=assunto)
        
        # Redireciona para a página de reclamações com informações de contato
        return redirect('complaints')
    
    return render(request, 'contact_summary.html')

def complaints(request):
    # Filtra todas as reclamações associadas ao usuário atual
    complaints = Contato.objects.filter(user=request.user)
    return render(request, 'complaints.html', {'complaints': complaints})
