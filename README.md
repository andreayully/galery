# Galery

Prototipo funcional de una Galeria de imagenes web que permite la vista previa de los archivos y valdiar su tamaño maximo de manera asincrona.

## Probar de manera local
  * Pre-requisitos Python 3.+ y Virtualenv

  1. Crear ambiente virtual **virtualenv galery_env** y activar el ambiente **source galery_env/bin/activate**
  2. Clonar el proyecto **git clone https://github.com/andreayully/galery.git** y 
  3. **cd galery/** 
      
      - Instalar requerimientos **pip install -R requirements.txt**
  4. Realizar migraciones 
      - ``` python manage.py makemigrations ```
      - ``` python manage.py migrate ```
     
  5. Runserver ``` python manage.py runserver ``` [http://127.0.0.1:8000](http://127.0.0.1:8000)
