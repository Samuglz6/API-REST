#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, abort, make_response, request

class Car:
	def __init__(self, carId, matricula, marca, fechaFabricacion, tipoAveria):
		self.carId = carId
		self.matricula = matricula
		self.marca = marca
		self.fechaFabricacion = fechaFabricacion
        self.tipoAveria = tipoAveria

####################################################################
# Example:
car_list = [ Car(1, '1234ABC', 'Volvo', '2010', 1),
             Car(2, '8473LSM', 'Toyota', '2012', 4),
             Car(3, '7973KDD', 'Seat', '2015', 3),
	     	 Car(4, '4441NFC', 'Ranault', '2018', 2)]

####################################################################

cars_api = Blueprint('cars_api', __name__)

#Devolver todos los coches existentes
@cars_api.route('/resources/cars/', methods=['GET'])
def getCars():
	return jsonify({'cars': car_list})

#Devolver los datos de un coche segun el id indicado
@cars_api.route('/resources/cars/<int:carId>/', methods=['GET'])
def getOneCar(carId):
	for car in car_list:
		if car.carId == carId:
			return jsonify({'car':car})
    abort(404)

#Añade un nuevo coche
@cars_api.route('/resources/cars/', methods=['POST'])
def createCar():
	if not request.json or not 'carId' in request.json:
        	abort(404)
    	carId = request.json.get('carId')
		matricula = request.json.get('matricula')
    	marca = request.json.get('marca')
		fechaFabricacion = request.json.get('fechaFabricacion')
    	tipoAveria = request.json.get('tipoAveria')

		car = Car(regId, matricula, marca, fechaFabricacion, tipoAveria)
    	car_list.append(car)

    	return jsonify({'car':car}),201

# Manejo errores 404
@devices_api.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'ERROR': 'No se ha encontrado el recurso'}),404)
