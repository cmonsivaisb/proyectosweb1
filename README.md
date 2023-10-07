


# Visor de Proyectos Web

Visor de proyectos web

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python (versión X.X)
- Pip (versión X.X)
- Virtualenv (opcional pero recomendado)

## Instalación

1. **Clona el repositorio**

   Clona este repositorio en tu máquina local utilizando Git:

   ```bash
   git clone https://github.com/tuusuario/nombre-del-repo.git
   ```

2. **Crea un entorno virtual (opcional)**

   Se recomienda crear un entorno virtual para el proyecto. Puedes hacerlo con `virtualenv`:

   ```bash
   virtualenv venv
   ```

   Luego, activa el entorno virtual:

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS y Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Instala las dependencias**

   Ve al directorio raíz del proyecto y ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**

   Configura tu base de datos en el archivo `settings.py`. Puedes usar SQLite o configurar otro motor de base de datos como MySQL o PostgreSQL.
   Para la base de datos para MySQL. Puedes usar la siguiente configuración como ejemplo:
   ```
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nombre_de_tu_base_de_datos',
           'USER': 'tu_usuario_de_mysql',
           'PASSWORD': 'tu_contraseña_de_mysql',
           'HOST': 'localhost',  # O la dirección IP de tu servidor MySQL
           'PORT': '3306',  # El puerto de MySQL (por defecto es 3306)
       }
   }
   ```

6. **Aplica las migraciones**

   Ejecuta las migraciones para crear las tablas en la base de datos:

   ```bash
   python manage.py migrate
   ```

7. **Ejecuta el servidor de desarrollo**

   Inicia el servidor de desarrollo de Django:

   ```bash
   python manage.py runserver
   ```

   El proyecto estará disponible en [http://localhost:8000/](http://localhost:8000/).

8. **OPCIONAL> Agregar usuarios y desarolladores**

   Opcionalmente se pueden agregar los usuarios y desarolladores mediante la direccion /admin o
   ejecutando python manage.py shell y copiando los siguientes comantos

    ```
   from django.contrib.auth.models import User
   from project1.models import Desarrollador
   
   # Agregar desarrolladores
   desarrollador1 = Desarrollador.objects.create(nombre="Nombre1", apellido="Apellido1")
   desarrollador2 = Desarrollador.objects.create(nombre="Nombre2", apellido="Apellido2")
   
   # Agregar un usuario de tipo visor (sin privilegios de admin)
   usuario_visor = User.objects.create_user(username="usuario_visor", password="contraseña_visor")
   usuario_visor.save()
    ```


