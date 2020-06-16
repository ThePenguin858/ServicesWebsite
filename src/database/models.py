from django.db import models

# Create your models here.


class Cliente(models.Model):
    cid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)
    morada = models.CharField(max_length=500, blank=True)
    nif = models.CharField(max_length=9)
    email = models.EmailField()
    codigo_postal = models.CharField(max_length=8)
    telefone = models.CharField(max_length=9)


class Fatura(models.Model):
    fid = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_emissao = models.DateField()
