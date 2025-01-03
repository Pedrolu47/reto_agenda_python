# forms.py
from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario personalizado para el registro
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, help_text="Nombre")
    last_name = forms.CharField(max_length=100, required=True, help_text="Apellido")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')  # Campos que aparecerán en el formulario
# forms.py

  # Asegúrate de que el modelo 'Reserva' esté correctamente importado

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['espacio', 'fecha']  # Campos que se mostrarán en el formulario

    # Puedes agregar validaciones adicionales si es necesario.
