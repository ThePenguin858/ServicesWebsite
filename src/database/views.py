from django.shortcuts import render

from .models import Client, Invoice
from .forms import ModelClientForm, ModelInvoiceForm
# Create your views here.


def create_invoice_view(request, *args, **kwargs):
    """ View for creating receipts urls=create """

    my_form = ModelInvoiceForm(request.POST or None)

    if my_form.is_valid():
        my_form.save()
        my_form = ModelInvoiceForm()
    else:
        print(my_form.errors)

    context = {'form': my_form}

    return render(request, 'database/invoice_create.html', context)


def create_client_view(request, *args, **kwargs):
    """ View for creating client urls=create """

    new_form = ModelClientForm(request.POST or None)

    if new_form.is_valid():
        new_form.save()
        new_form = ModelClientForm()

    context = {'Form': new_form}

    return render(request, 'database/client_create.html', context)
