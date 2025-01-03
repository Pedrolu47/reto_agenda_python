# reservas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reservar/', views.crear_reserva, name='reservar'),
    path('consultar/', views.consultar_reservas, name='consultar_reservas'),
]
