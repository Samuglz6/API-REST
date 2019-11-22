#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, make_response, request

class Taller:
    def __init__(self, idTaller, nombreTaller, direccion, abierto, marca):
        self.idTaller = idTaller
        self.nombreTaller = nombreTaller
        self.direccion = direccion
        self.abierto = abierto
        self.marca = marca

####################################################################
# Example:
listaTalleres = [ Taller(1, 'Talleres Manolo','Calle ejemplo 13', True, 'Seat'),
             	  Taller(2, 'Bekario','Calle inventada 31', False, 'Volvo'),
             	  Taller(3, 'Reparaciones Lopez','Calle Falsa 2', True, 'Toyota'),
	     	 	  Taller(4, 'Arreglos Linde', 'Calle ficticia 12', True, 'Renault')]

####################################################################

talleres_api = Blueprint('talleres_api', __name__)

#Mostrar todos los talleres
@talleres_api.route('/recursos/talleres/', methods=['GET'])
def obtenerTalleres():
	return jsonify({'talleres': listaTalleres})

#Devolver los datos de un taller segun el id indicado
@talleres_api.route('/recursos/talleres/<int:idTaller>/', methods=['GET'])
def obtenerTaller(nombreTaller):
    for taller in talleres:
        if taller.get('idTaller') == idTaller:
            return jsonify({'taller':taller})
    abort(404)

#Añade un nuevo taller
@talleres_api.route('/recursos/talleres/', methods=['POST'])
def crearTaller():
    if not request.json or not 'idTaller' in request.json:
            abort(404)
    idTaller = listaTalleres[-1].get('idTaller')+1
    nombreTaller = request.json.get('nombreTaller')
    direccion = request.json.get('direccion')
    marca = request.json.get('marca')
    abierto = False

    taller = {'idTaller': idTaller, 'nombreTaller': nombreTaller,'direccion': direccion, 'marca': marca,'abierto': abierto}
    talleres.append(taller)

    return jsonify({'taller':taller}),201

#Elimina un taller existente
@talleres_api.route('/recursos/talleres/<int:id>/', methods=['DELETE'])
def borrarTaller(id):
	taller = [taller for taller in listaTalleres if taller['idTaller'] == id]
	listaTalleres.remove(taller[0])
	return jsonify({}), 204 # No content


#Definimos la respuesta para el codigo de error 404
@talleres_api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'Error': 'No se ha encontrado el recurso'}),404)
