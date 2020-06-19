from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=120)
    nif = models.CharField(max_length=9, unique=True)
    address = models.CharField(max_length=500, blank=True)
    zip_code = models.CharField(max_length=16)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=13, blank=True)

    def get_absolute_url(self):
        return f'/client/{self.name}'


class Invoice(models.Model):
    fid = models.AutoField(unique=True, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    emission_date = models.DateField()
    provider_name = models.CharField(max_length=120)
    provider_nif = models.DecimalField(max_digits=9, decimal_places=0)
    service_value = models.PositiveIntegerField()
    iva = models.DecimalField(decimal_places=2, max_digits=10)
    tax_explanation = models.TextField(blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return f'/invoice/{self.fid}'
