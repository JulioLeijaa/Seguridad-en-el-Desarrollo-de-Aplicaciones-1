from flask import jsonify
from flask_restful import Resource, reqparse
from models import ContactoModel
from conf import db

#argumentos/parametros para tomar de los requests
args_contacto = reqparse.RequestParser()
args_contacto.add_argument('nombre',type=str)
args_contacto.add_argument('correo',type=str)
args_contacto.add_argument('telefono',type=str)

#clase con los métodos de las rutas por verbos(GET, POST)
class ContactoRoutes(Resource):
    def get(self):
        try:
            response = ContactoModel.query.all()
            response = [{
                'id':i.id,
                'nombre':i.nombre,
                'correo':i.correo,
                'telefono':i.telefono,
                'created_at':i.created_at,
                'updated_at':i.updated_at} for i in response]
            return jsonify(response)
        except:
            return {
                'error' : 'Error al obtener los contactos'
            }

    def post(self):
        try:
            args = args_contacto.parse_args()
            contacto = ContactoModel(
                            nombre = args.nombre,
                            correo = args.correo,
                            telefono = args.telefono)
            db.session.add(contacto)
            db.session.commit()
            return {
                'message' : 'Contacto ' + contacto.nombre +' agregado correctamente.'
            }, 201
        except:
            return {
                'message' : 'Error al registrar el contacto'
            }