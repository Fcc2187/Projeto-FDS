from django.db import models

# Create your models here.
class Contato(models.Model):
    nome=models.CharField(max_length=30)
    email=models.EmailField()
    assunto=models.TextField()

    def __str__(self):
        return self.email
    
class Complaint(models.Model):
    email = models.TextField()
    assunto = models.EmailField()
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome