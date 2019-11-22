#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, make_response, request

class Mecanico:
    def __init__(self, idMecanico, nombre):
        self.idMecanico = idMecanico
        self.nombre = nombre

####################################################################
# Example:
listaMecanicos = [ Mecanico(1, 'Beka'),
                   Mecanico(2, 'Samuel')]
####################################################################

mecanicos_api = Blueprint('mecanicos_api', __name__)

#Devolver todos los mecanicos
@mecanicos_api.route('/recursos/mecanicos/', methods=['GET'])
def obtenerCoches():
    return jsonify({'mecanicos': listaMecanicos})

#Devolver los datos de un mecanico segun el id indicado
@mecanicos_api.route('/recursos/mecanicos/<int:idMecanico>/', methods=['GET'])
def obtenerUnMecanico(idMecanico):
    for mecanico in listaMecanicos:
        if mecanico.idMecanico == idMecanico:
            return jsonify({'mecanico': mecanico})
    abort(404)

#Añade un nuevo mecanico
@mecanicos_api.route('/recursos/mecanicos/', methods=['POST'])
def crearMecanico():
    if not request.json or not 'idMecanico' in request.json:
        abort(404)
    idMecanico = listaMecanicos[-1].get('idMecanico')+1
    nombre = request.json.get('nombre')

    mecanico = Mecanico(idMecanico, nombre)
    listaMecanicos.append(mecanico)

    return jsonify({'mecanico': mecanico}),201

#Elimina un mecanico
@mecanicos_api.route('/recursos/mecanicos/<int:id>/', methods=['DELETE'])
def not_found(error):
    return make_response(jsonify({'ERROR': 'No se ha encontrado el recurso'}), 404)
