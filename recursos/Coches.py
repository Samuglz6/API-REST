#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, make_response, request

class Coche:
    def __init__(self, idCoche, matricula, marca, fechaFabricacion, tipoAveria):
        self.idCoche = idCoche
        self.matricula = matricula
        self.marca = marca
        self.fechaFabricacion = fechaFabricacion
        self.tipoAveria = tipoAveria

####################################################################
# Example:
listaCoches = [ Coche(1, '1234ABC', 'Volvo', '2010', 1),
                Coche(2, '8473LSM', 'Toyota', '2012', 4),
                Coche(3, '7973KDD', 'Seat', '2015', 3),
	     	    Coche(4, '4441NFC', 'Ranault', '2018', 2)]

####################################################################

coches_api = Blueprint('coches_api', __name__)

#Devolver todos los coches existentes
@coches_api.route('/recursos/coches/', methods=['GET'])
def obtenerCoches():
	return jsonify({'coches': listaCoches})

#Devolver los datos de un coche segun el id indicado
@coches_api.route('/recursos/coches/<int:idCoche>/', methods=['GET'])
def obtenerUnCoche(idCoche):
    for coche in listaCoches:
	    if coche.idCoche == idCoche:
		    return jsonify({'coche': coche})
    abort(404)

#Añade un nuevo coche
@coches_api.route('/recursos/coches/', methods=['POST'])
def crearCoche():
    if not request.json or not 'idCoche' in request.json:
        abort(404)
    idCoche = listaCoches[-1].get('idCoche')+1
    matricula = request.json.get('matricula')
    marca = request.json.get('marca')
    fechaFabricacion = request.json.get('fechaFabricacion')
    tipoAveria = request.json.get('tipoAveria')

    coche = Coche(idCoche, matricula, marca, fechaFabricacion, tipoAveria)
    listaCoches.append(coche)

    return jsonify({'coche': coche}),201

#Elimina un coche existente
@coches_api.route('/recursos/coches/<int:id>/', methods=['DELETE'])
def borrarCoche(id):
	coche = [coche for coche in listaCoches if coche['idCoche'] == id]
	listaCoches.remove(coche[0])
	return jsonify({}), 204 # No content

# Manejo errores 404
@coches_api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'ERROR': 'No se ha encontrado el recurso'}),404)
