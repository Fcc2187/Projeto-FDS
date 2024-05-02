from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contato(models.Model):
    assunto=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.assunto
    
class Complaint(models.Model):
    assunto = models.TextField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.assunto