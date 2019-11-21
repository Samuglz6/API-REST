#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

from api.coches import coches_api, Coche
from api.talleres import talleres_api, Taller

from flask.json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
	def default(self, obj):
    	if isinstance(obj, Car):
    		return {
                	'idCoche': obj.regId,
					'matricula': obj.matricula,
					'marca': obj.marca,
					'fechaFabricacion': obj.fechaFabricacion,
					'troubleType': obj.troubleType
            	   }
		if isinstance(obj, Taller):
        	return {
					'idTaller':obj.idTaller,
                	'nombreTaller': obj.nombreTaller,
					'direccion': obj.direccion,
					'abierto': obj.abierto,
					'marca': obj.marca
        		   }
        return super(MyJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

# Blueprint
app.register_blueprint(talleres_api)
app.register_blueprint(coches_api)


if __name__ == '__main__':
    app.run(debug=True)
