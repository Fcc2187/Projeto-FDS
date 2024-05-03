from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    assunto=models.TextField()
    def __str__(self):
        return self.assunto