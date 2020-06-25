from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, about_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Back end and Database urls
    path('database/', include('database.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # Front end
    path('home/', home_view, name='home-view'),
    path('', home_view),
    path('about/', about_view, name='about-view'),
]
