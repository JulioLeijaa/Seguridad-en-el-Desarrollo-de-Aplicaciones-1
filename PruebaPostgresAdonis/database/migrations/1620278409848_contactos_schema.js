'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class ContactosSchema extends Schema {
    up() {
        this.create('contactos', (table) => {
            table.increments()
            table.string('nombre', 80)
            table.string('correo', 254)
            table.string('telefono', 50)
            table.timestamps()
        })
    }

    down() {
        this.drop('contactos')
    }
}

module.exports = ContactosSchema