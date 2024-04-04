from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def index(request):
    mensagem = ''  # inicializar a variável de mensagem
    
    if request.method == "POST":
        contact = Contact()
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        contact.email = email
        contact.assunto = assunto
        contact.save()
        mensagem = "Obrigado por nos contatar!"  # definir a mensagem de sucesso
    
    return render(request, 'index.html', {'mensagem': mensagem})  # passar a mensagem para o template

