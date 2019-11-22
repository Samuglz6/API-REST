#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, make_response, request

class Averia:
    def __init__(self, idAveria, descripcion, coche):
        self.idAveria = idAveria
        self.descripcion = descripcion
        self.coche = coche

####################################################################
# Example:
listaAverias = [ Averia(1, '1234ABC', 1),
                 Averia(2, '8473LSM', 4),
                 Averia(3, '7973KDD', 3),
	     	     Averia(4, '4441NFC', 2)]
####################################################################

averias_api = Blueprint('averias_api', __name__)


#Devolver todas las averias existentes
@averias_api.route('/recursos/averias/', methods=['GET'])
def obtenerAverias():
    return jsonify({'averias': listaAverias})

#Devolver los datos de una averia segun el id indicado
@averias_api.route('/recursos/averias/<int:idAveria>', methods=['GET'])
def obtenerUnaAveria(idAveria):
    for averia in listaAverias:
        if averia.idAveria == idAveria:
            return jsonify({'averia': averia})
    abort(404)

#Añade un nuevo coche
@averias_api.route('/recursos/averias/', methods=['POST'])
def crearAveria():
    if not request.json or not 'idAveria' in request.json:
        abort(404)
    idAveria = listaAverias[-1].get('idAveria')+1
    descripcion = request.json.get('descripcion')
    coche = request.json.get('coche')

    averia = Averia(idAveria, descripcion, coche)
    listaAverias.append(averia)

    return jsonify({'averia': averia}),201

#Elimina un coche existente
@averias_api.route('/recursos/averias/<int:id>', methods=['DELETE'])
def borrarAveria(id):
    averia = [averia for averia in listaAverias if averia['idAveria'] == id]
    listaAverias.remove(averia[0])
    return jsonify({}), 204

#Manejo errores 404
@averias_api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'ERROR': 'No se ha encontrado el recurso'}),404)
