"""
URL configuration for dojo_agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# dojo_agenda/urls.py
from django.contrib import admin
from django.urls import path, include  # Importa 'include' para incluir URLs de otras aplicaciones
from django.conf import settings
from django.conf.urls.static import static
from reservas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include('reservas.urls')),  # Incluir las URLs de la app 'reservas'
    path('', views.home, name='home'),  # Esta es la URL principal de la aplicación
]

# Si estás trabajando con archivos estáticos (como imágenes o archivos de usuario), agrega esto también:
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

