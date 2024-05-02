from django.db import models

# Create your models here.
class Contato(models.Model):
    assunto=models.TextField()

    def __str__(self):
        return self.assunto
    
class Complaint(models.Model):
    assunto = models.TextField() 
    def __str__(self):
        return self.assunto