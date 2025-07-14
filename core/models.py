from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('cliente', 'Cliente'),
        ('trabalhador', 'Trabalhador'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO)

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    tipo_servico = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.nome} - {self.tipo_servico}"
