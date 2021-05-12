from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('contacts.urls')),
] + docs
