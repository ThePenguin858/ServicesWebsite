from django.shortcuts import render, get_object_or_404, redirect

from .models import Client, Invoice
from .forms import ModelClientForm, ModelInvoiceForm
# Create your views here.


def dynamic_client_view(request, my_name):
    obj = get_object_or_404(Client, name=my_name)

    context = {
        'object': obj
    }
    return render(request, 'database/client_view.html', context)


def list_invoice_view(request):
    """ List all of the invoices """
    queryset = Invoice.objects.all()

    context = {
        'object_list': queryset
    }

    return render(request, 'database/list_invoice.html', context)


def list_clients_view(request):
    """ List all of the clients """
    queryset = Client.objects.all()

    context = {
        'object_list': queryset
    }

    return render(request, 'database/list_client.html', context)


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
