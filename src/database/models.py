from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=120)
    nif = models.DecimalField(max_digits=9, decimal_places=0)
    address = models.CharField(max_length=500, blank=True)
    zip_code = models.CharField(max_length=15)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=12, blank=True)


class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    emission_date = models.DateField()
    client_name = models.CharField(max_length=120)
    client_nif = models.DecimalField(max_digits=9, decimal_places=0)
    provider_name = models.CharField(max_length=120)
    provider_nif = models.DecimalField(max_digits=9, decimal_places=0)
    service_value = models.PositiveIntegerField()
    iva = models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    tax_explanation = models.TextField(blank=True)
    service_date = models.DateField(blank=True)
