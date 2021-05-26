# Seguridad-en-el-Desarrollo-de-Aplicaciones-1
Practica #1 Creación de 3 APIS, con 3 diferentes framework (laravel, AdonisJS, y Flask).
El Objetivo es conocer la instalación y configuración de los framework, así como su implementación como API.

Los 3 frameworks consumen la base de datos en PostgreSQL y, por lo tanto, la misma tabla (contactos).

##Instalaciones y configuraciones

##PYTHON
-Comenzamos con Python, tenemos que instalar Fask como API con el siguiente comando:
  pip install flask-restful
-Instalamos la librería de SQLAlchemy para utilizar la base de datos en PostgreSQL:
  pip install Flask-SQLAlchemy
-Editamos el archivo de configuración hacia la base de datos (conf.py) donde la configuración es la siguiente:
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/prueba'
-Para realizar las migraciones a la base de datos, escribimos en la consola de python (dentro del proyecto) los comandos:
  from models import db, ContactoModel y db.create_all()
-Y ahora ejecutamos el siguiente comando para levantar el servidor:
  python app.py
-El servidor estará levantado y listo para consumir la base de datos por medio de APIs
##
##ADONIS
-Una vez clonado el proyecto, instalamos los módulos necesarios de node con:
  npm install
-Ahora instalamos el paquete de postgres, con el cual el proyecto podrá utilizar la base de datos:
  npm i postgres
-Editamos el archivo .env, en este se escriben las configuraciones a la base de datos 
 y se agregan los datos conforme el nombre d esus variables:
  DB_CONNECTION=pg, DB_HOST=127.0.0.1, DB_PORT=5432, DB_USER=postgres, DB_PASSWORD=admin, DB_DATABASE=prueba
-Si queremos realizar la migracion desde este framework ejecutamos el siguiente contacto:
  adonis migration:run
-Ahora levantamos el servidor de adonis: adonis serve --dev
-El servidor estará levantado y listo para consumir la base de datos por medio de APIs
##
##LARAVEL
-Una vez clonado el proyecto, configuramos el archivo .env.example
 Primero le cambiamos el nombre a ".env" y escribimos la configuración para
 la conexión a la base de datos en postgres:
 DB_CONNECTION=pgsql DB_HOST=127.0.0.1 DB_PORT=5432 DB_DATABASE=prueba DB_USERNAME=postgres DB_PASSWORD=admin
-Ahora ejecutamos la migración de las tablas a la base de datos con el comando:
  php artisan migrate
-Ahora levantamos el servidor de forma local:
  php artisan serve
 -El servidor estará levantado y listo para consumir la base de datos por medio de APIs
 
 
 
