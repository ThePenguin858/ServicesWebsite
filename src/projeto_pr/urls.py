from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, about_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Back end and Database urls
    path('database/', include('database.urls')),
    path('', include('django.contrib.auth.urls')),
    # Front end
    path('', include('pages.urls')),
]
