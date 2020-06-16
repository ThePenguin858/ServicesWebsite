from django import forms

from .models import Cliente, Fatura


class FaturaForm(forms.ModelForm):
    class Meta:
        model = Fatura
        fields = [
            'nome',
            'morada',
            'nif',
            'email',
            'codigo_postal',
            'telefone'
        ]


class ClienteForm(forms.ModelForm):
    
