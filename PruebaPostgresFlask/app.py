from conf import api, app
from routes import ContactoRoutes

#clase con métodos de rutas y su path
api.add_resource(ContactoRoutes, '/contacto')

#iniciar la app
if __name__ == '__main__':
    app.run()
    # app.run(debug=True)