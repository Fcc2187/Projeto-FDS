from django.shortcuts import render, redirect
from .models import Contato, Complaint
from django.urls import reverse

# Create your views here.
def contact(request):
    if request.method == "POST":
        # Obtém ou cria um objeto de Contato associado ao usuário atual
        contato, created = Contato.objects.get_or_create(user=request.user)
        
        # Obtém o assunto do formulário POST
        assunto = request.POST.get('assunto')
        
        # Atualiza o campo 'assunto' do objeto contato
        contato.assunto = assunto
        
        # Salva as alterações no objeto contato
        contato.save()
        
        # Redireciona para a página de reclamações com informações de contato
        return redirect('complaints')
    
    return render(request, 'contact_summary.html')

def complaints(request):
     complaints = Contato.objects.filter(user=request.user)
     return render(request, 'complaints.html', {'complaints': complaints})
