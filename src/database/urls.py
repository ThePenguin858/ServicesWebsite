
from django.urls import path

from .views import (create_invoice_view, create_client_view,
                    list_clients_view, list_invoice_view,
                    dynamic_client_view)
appname = 'database'
urlpatterns = [

    # Back end and Database urls
    path('client/<str:my_name>/',
         dynamic_client_view, name='client-detail'),

    path('create_invoice/', create_invoice_view, name='create-invoice'),
    path('create_client/', create_client_view, name='create-client'),

    path('list_invoices', list_invoice_view, name='list-invoices'),
    path('list_clients', list_clients_view, name='list-clients'),
]
