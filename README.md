# Agenda de Reservas - Dojo Bushido

Este proyecto es una agenda digital desarrollada en Python y Django para la escuela de samuráis Dojo Bushido. La aplicación permite gestionar la reserva de espacios como salas de entrenamiento, meditación y el sento (sauna) de manera segura y eficiente, controlando el acceso y los permisos según el rol de cada usuario.

## Características Principales

- **Autenticación y Control de Sesiones**: Proceso seguro de inicio y cierre de sesión.
- **Gestor de Usuarios**:
  - Creación de usuarios con diferentes roles:
    - `Sensei`: Permisos completos.
    - `Maestro`: Reservas completas pero sin permiso para borrar.
    - `Estudiante`: Reservas solo de aulas.
- **Reservas de Espacios**:
  - Visualización de las reservas futuras.
  - Creación de reservas con control de permisos para espacios específicos (e.g., solo maestros pueden reservar el sento).
- **Interfaz de Usuario**:
  - Formularios intuitivos para la gestión de usuarios y reservas.
  - Listado de reservas con detalles como usuario, espacio y fecha.

## Tecnologías Utilizadas

- **Backend**:
  - [Python](https://www.python.org/)
  - [Django](https://www.djangoproject.com/)
- **Base de Datos**:
  - SQLite (por defecto, adaptable a otras opciones como PostgreSQL o MySQL).
- **Frontend**:
  - Templates de Django.
  - [Bootstrap](https://getbootstrap.com/) (opcional para diseño).
- **Control de Versiones**:
  - [Git](https://git-scm.com/)
  - [GitHub](https://github.com/)

## Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/dojo-agenda.git
   cd dojo-agenda
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor**:
   ```bash
   python manage.py runserver
   ```

7. Accede a la aplicación en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Uso

### Creación de Usuarios
- Accede a la página de administración o usa la interfaz para registrar nuevos usuarios.
- Asigna un rol (`Sensei`, `Maestro`, `Estudiante`) al crear cada usuario.

### Gestión de Reservas
- Inicia sesión con tus credenciales.
- Selecciona el espacio y fecha deseados para la reserva.
- Consulta las reservas futuras desde el panel correspondiente.

## Estructura del Proyecto

```
dojo-agenda/
├── reservas/            # Aplicación principal
│   ├── migrations/      # Migraciones de base de datos
│   ├── templates/       # Templates HTML
│   ├── views.py         # Lógica de vistas
│   ├── models.py        # Definición de modelos
├── dojo_agenda/         # Configuración del proyecto Django
├── manage.py            # Comando principal de Django
├── requirements.txt     # Dependencias del proyecto
```



## Licencia
Este proyecto está bajo la [Licencia MIT](LICENSE).

## Autor
Desarrollado por:Pedrolu47

