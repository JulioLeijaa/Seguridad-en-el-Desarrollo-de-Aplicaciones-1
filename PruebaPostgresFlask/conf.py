from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

#iniciar app
app = Flask(__name__)
api = Api(app)

#conf de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/prueba'
db = SQLAlchemy(app)