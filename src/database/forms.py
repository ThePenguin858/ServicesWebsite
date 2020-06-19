from django import forms

from .models import Client, Invoice

# TODO: Transformar ambos estes forms em modelForms


class ModelClientForm(forms.ModelForm):
    nif = forms.CharField(min_length=9, max_length=9)

    class Meta:
        model = Client
        fields = [
            'name',
            'nif',
            'address',
            'zip_code',
            'contact_email',
            'contact_phone'
        ]
        labels = {
            'name': 'Nome',
            'nif': 'NIF',
            'address': 'Morada',
            'zip_code': 'Codigo Postal',
            'contact_email': 'E-mail',
            'contact_phone': 'Contacto'
        }
        widgets = {

            'contact_phone': forms.TextInput(
                attrs={
                    'input': 'tel',
                    'pattern': '[0-9]{9}',
                    'placeholder': '921846856'
                }),

            'zip_code': forms.TextInput(
                attrs={
                    'pattern': '[0-9]{4}-[0-9]{3}',
                    'placeholder': '9125-119',
                })
        }


class ModelInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'client',
            'emission_date',
            'provider_name',
            'provider_nif',
            'service_value',
            'iva',
            'tax_explanation',
            'service_date'
        ]
        labels = {
            'client': 'Cliente:',
            'emission_date': 'Data de emissao:',
            'provider_name': 'Nome do fornecedor:',
            'provider_nif': 'NIF do fornecedor:',
            'service_value': 'Valor do servico:',
            'iva': 'Valor do IVA:',
            'tax_explanation': 'Motivo de isencao de IVA:',
            'service_date': 'Data de servico:'
        }
        widgets = {
            'emission_date': forms.DateInput(attrs={'type': 'date'}),
            'service_date': forms.DateInput(attrs={'type': 'date'}),
            'tax_explanation': forms.Textarea(
                attrs={
                    'rows': 20,
                    'cols': 40,
                    'wrap': 'True',
                    'style': 'resize=none;'
                })
        }


# class InvoiceForm(forms.Form):
    # client = forms.ModelChoiceField(queryset=Client.objects.values('name'))

    # emission_date = forms.DateField(widget=forms.DateInput(
        # attrs={
        # "type": "date"
        # }
    # ))
    # client_name = forms.CharField(max_length=120)
    # client_nif = forms.DecimalField(max_digits=9, decimal_places=0)
    # provider_name = forms.CharField(max_length=120)
    # provider_nif = forms.DecimalField(max_digits=9, decimal_places=0)
    # service_value = forms.IntegerField()
    # iva = forms.DecimalField(decimal_places=2, max_digits=5)
    # tax_explanation = forms.CharField(required=False, widget=forms.Textarea())
    # service_date = forms.DateField(required=False, widget=forms.DateInput(
        # attrs={
        # "type": "date"
        # }
    # ))
