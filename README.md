# Seguridad-en-el-Desarrollo-de-Aplicaciones-1
Practica #1 Creación de 3 APIS, con 3 diferentes framework (laravel, AdonisJS, y Flask).
El Objetivo es conocer la instalación y configuración de los framework, así como su implementación como API.

Los 3 frameworks consumen la base de datos en PostgreSQL y, por lo tanto, la misma tabla (contactos).

##Instalaciones.
##PYTHON
##Comenzamos con Python, tenemos que instalar Fask como API con el siguiente comando:
  pip install flask-restful
##Instalamos la librería de SQLAlchemy para utilizar la base de datos en PostgreSQL:
  pip install Flask-SQLAlchemy
##
##ADONIS
##Una vez clonado el proyecto, instalamos los módulos necesarios de node con:
  npm install
##Ahora instalamos el paquete de postgres, con el cual el proyecto podrá utilizar la base de datos:
  npm i postgres
##
##LARAVEL
 
 
 
 
 
-Clonamos el proyecto y editamos el archivo de configuración hacia la base de datos (conf.py)
 donde la configuración es la siguiente:
 app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'user':'password'@'host':'port'/'database'
 
