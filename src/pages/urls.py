from django.urls import include, path

from .views import home_view, about_view, contacts_view


urlpatterns = [
    path('home/', home_view),
    path('', home_view),
    path('about/', about_view),
    path('contacts/', contacts_view),
]
