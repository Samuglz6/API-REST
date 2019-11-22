#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, make_response, request

class Cliente:
    def __init__(self, idCliente, nombre, domicilio, fechaNacimiento):
        self.idCliente = idCliente
        self.nombre = nombre
        self.domicilio = domicilio
        self.fechaNacimiento = fechaNacimiento

####################################################################
# Example:
listaClientes = [ Cliente(1, 'Miguel', 'Calle inventada 31', '1/10/1990'),
                  Cliente(2, 'Ana', 'Calle Falsa 2', '10/1/1985'),
                  Cliente(3, 'Pedro','Calle ficticia 12', '25/8/1970')]
####################################################################

clientes_api = Blueprint('clientes_api', __name__)

#Devolver todos los Clientes existentes
@clientes_api.route('/recursos/clientes/', methods=['GET'])
def obtenerClientes():
	return jsonify({'Clientes': listaClientes})

#Devolver los datos de un Cliente segun el id indicado
@clientes_api.route('/recursos/clientes<int:idCliente>/', methods=['GET'])
def obtenerUnCliente(idCliente):
    for cliente in listaClientes:
	    if cliente.idCliente == idCliente:
		    return jsonify({'Cliente': Cliente})
    abort(404)

#Añade un nuevo Cliente
@clientes_api.route('/recursos/clientes/', methods=['POST'])
def crearCliente():
    if not request.json or not 'idCliente' in request.json:
        abort(404)
    idCliente = listaClientes[-1].get('idCliente')+1
    nombre = request.json.get('nombre')
    domicilio = request.json.get('domicilio')
    fechaNacimiento = request.json.get('fechaNacimiento')

    cliente = Cliente(idCliente, nombre, domicilio, fechaNacimiento)
    listaClientes.append(cliente)

    return jsonify({'cliente': cliente}),201

#Elimina un Cliente existente
@clientes_api.route('/recursos/clientes/<int:id>/', methods=['DELETE'])
def borrarCliente(id):
	cliente = [cliente for cliente in listaClientes if Cliente['idCliente'] == id]
	listaClientes.remove(cliente[0])
	return jsonify({}), 204 # No content

# Manejo errores 404
@clientes_api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'ERROR': 'No se ha encontrado el recurso'}),404)
