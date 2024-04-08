from django.db import models

# Create your models here.
class Contato(models.Model):
    nome=models.TextField()
    email=models.EmailField()
    assunto=models.TextField()
    def __str__(self):
        return self.email
