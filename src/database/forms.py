from django import forms

from .models import Client, Invoice


class ClientForm(forms.Form):
    name = forms.CharField(max_length=120)
    nif = forms.DecimalField(max_digits=9, decimal_places=0)
    address = forms.CharField(max_length=500)
    zip_code = forms.CharField(max_length=15)
    contact_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "input": "email"
            }
        ))
    contact_phone = forms.CharField(
        max_length=12,
        widget=forms.TextInput(
            attrs={
                "input": "tel",
                "pattern": "[0-9]{3}-[0-9]{3}-[0-9]{3}"
            }
        ))


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "client"
        ]
