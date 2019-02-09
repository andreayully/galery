# Galery

Prototipo funcional de una Galería de imágenes web que permite la vista previa de los archivos y validar su tamaño máximo de manera asíncrona.

## Probar de manera local
  * Pre-requisitos Python 3.+ y Virtualenv

  1. Crear ambiente virtual **virtualenv galery_env** y activar el ambiente **source galery_env/bin/activate**
  2. Clonar el proyecto **git clone https://github.com/andreayully/galery.git**
  3. **cd galery/**

      - Instalar requerimientos **pip install -R requirements.txt**
  4. Realizar migraciones
      - ``` python manage.py makemigrations ```
      - ``` python manage.py migrate ```

  5. Runserver ``` python manage.py runserver ``` [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Características
- Django 1.11
- Base de datos noSql - SQLite
- Plantilla Bootstrap [https://colorlib.com/](https://colorlib.com/preview/#poportfolio)

### Consideraciones de diseño para una versión comercial
- Compatibilidad con todos los navegadores
- Verificación del responsive en todas las funcionalidades
- **Seguridad**: Manejo de usuarios, autenticación por token, decorador @login_required para las vistas, permisos según perfiles.
- **Rendimiento**: Utilizar un servidor de medios independiente para alojar archivos de subida en entorno productivo para mejorar la eficiencia de la aplicación
- **Mantenimiento**: Continuar con la utilización de vistas basadas en clases para las funcionalidades futuras permite que el código sea fácil de mantener y depurar. Actualización de versiones de las tecnologías utilizadas (Django, Python, etc) a las mas estables segun vayan saliendo para correccion de bugs y nuevas características que estas puedan aportar. Eliminar vulnerabilidades de seguridad según se vayan detectando. Revisión de funcionalidades en general.
