from django.shortcuts import render

from .models import Client, Invoice
from .forms import ClientForm, InvoiceForm
# Create your views here.


def create_invoice_view(request, *args, **kwargs):
    """ View for creating receipts urls=create """

    my_form = InvoiceForm(request.POST or None)

    if my_form.is_valid():
        my_form.save()

    context = {
        'form': my_form
    }
    return render(request, 'database/fatura_create.html', context)


def create_client_view(request, *args, **kwargs):
    """ View for creating client urls=create """

    new_form = ClientForm(request.GET)

    if request.method == "POST":
        new_form = ClientForm(request.POST)
        if new_form.is_valid():
            Client.objects.create(**new_form.cleaned_data)

    context = {
        'Form': new_form
    }
    return render(request, 'database/client_create.html', context)
