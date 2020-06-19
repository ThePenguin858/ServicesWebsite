"""projeto_pr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, about_view, contacts_view
from database.views import (create_invoice_view, create_client_view,
                            list_clients_view, list_invoice_view,
                            dynamic_client_view)


urlpatterns = [
    path('home', home_view),
    path('', home_view),
    path('about', about_view),
    path('contacts', contacts_view),

    path('admin/', admin.site.urls),

    # Back end and Database urls
    path('client/<str:my_name>/', dynamic_client_view),

    path('create_invoice/', create_invoice_view),
    path('create_client/', create_client_view),

    path('list_invoices', list_invoice_view, ),
    path('list_clients', list_clients_view, ),
]
