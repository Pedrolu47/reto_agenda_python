# reservas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from .forms import ReservaForm, CustomUserCreationForm  # Asegúrate de que estos formularios están correctamente definidos
from .models import Reserva  # Verifica que el modelo Reserva esté definido correctamente

def home(request):
    return render(request, 'home.html')  # Asegúrate de tener una plantilla 'home.html'

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige a una vista de inicio o página principal
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión

""" from .forms import ReservaForm  # Importamos el formulario de reservas """

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la reserva
            return redirect('consultar_reservas')  # Redirige a la vista de reservas
    else:
        form = ReservaForm()

    return render(request, 'reservar.html', {'form': form})

def consultar_reservas(request):
    # Lógica para consultar reservas futuras
    reservas = Reserva.objects.all()  # Recupera todas las reservas (o las futuras si aplicas un filtro)
    return render(request, 'consultar_reservas.html', {'reservas': reservas})

# Create your views here.
