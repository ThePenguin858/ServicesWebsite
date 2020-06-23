from django import forms

from .models import Client, Invoice


class ClientForm(forms.ModelForm):
    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                'class': 'form__input',
            }))

    nif = forms.CharField(
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'class': 'form__input form__input--small',
            }))

    address = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form__input',
            }))

    contact_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form__input',
            }))

    contact_phone = forms.CharField(
        max_length=9,
        widget=forms.TextInput(
            attrs={
                'input': 'tel',
                'pattern': '[0-9]{9}',
                'placeholder': '921846856',
                'class': 'form__input form__input--small',
            }))

    zip_code = forms.CharField(
        max_length=16,
        widget=forms.TextInput(
            attrs={
                'pattern': '[0-9]{4}-[0-9]{3}',
                'placeholder': '9125-119',
                'class': 'form__input form__input--small',
            }))

    class Meta:
        model = Client
        fields = [
            'name',
            'nif',
            'address',
            'contact_email',
            'contact_phone',
            'zip_code',
        ]
        labels = {
            'name': 'Nome',
            'nif': 'Nif',
            'address': 'Morada',
            'zip_code': 'Código postal',
            'contact_email': 'Email',
            'contact_phone': 'Contacto',
        }


class InvoiceForm(forms.ModelForm):
    emission_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form__input form__input--small',
            'type': 'date',
        }))

    provider_name = forms.CharField(max_length=120,
                                    widget=forms.TextInput(
                                        attrs={
                                            'class': 'form__input form__input--small',
                                        }))

    provider_nif = forms.CharField(max_length=9,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form__input form__input--small',
                                       }))
    service_value = forms.DecimalField(min_value=0,
                                       decimal_places=2,
                                       widget=forms.NumberInput(
                                           attrs={
                                               'class': 'form__input form__input--small',
                                           }))

    iva = forms.DecimalField(required=False, decimal_places=2, max_digits=10, min_value=0,
                             widget=forms.NumberInput(
                                 attrs={
                                     'class': 'form__input form__input--small',
                                 }))

    tax_explanation = forms.Textarea(attrs={
        'class': 'form__input form__input--textarea', })

    service_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form__input form__input--small', }))

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
            'name': 'Nome:',
        }


# class InvoiceForm(forms.Form):

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
