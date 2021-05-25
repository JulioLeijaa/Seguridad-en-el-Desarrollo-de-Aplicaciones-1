'use strict'
//cambiar require por use(App/Models/Modelo) para los modelos
const Contacto = use("App/Models/Contacto");

class ContactoController {
    async register({ request, response }) {
        const { nombre, correo, telefono } = request.all();

        let contacto = new Contacto();
        contacto.nombre = nombre;
        contacto.correo = correo;
        contacto.telefono = telefono;

        try {
            const guardar = await contacto.save();

            if (guardar) {
                return response.status(201).json(contacto);
            }

            return response.status(401).json({ error: 'Ocurrió un problema al registrar el ususario' });
        } catch (error) {
            return response.status(401).json(error.message);
        }
    }

    //usar siempre { response } para que tome en cuenta este objeto
    async showAll({ response }) {
        return response.status(200).json(await Contacto.all());
    }
}

module.exports = ContactoController