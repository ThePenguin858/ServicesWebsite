from django.shortcuts import render

from .models import Fatura
from .forms import FaturaForm
# Create your views here.


def create_fatura_view(request, *args, **kwargs):
    """ View for creating receipts urls=create """

    my_form = FaturaForm(request.POST or None)

    if my_form.is_valid():
        my_form.save()

    context = {
        'form': my_form
    }
    return render(request, 'database/fatura_create.html', context)
