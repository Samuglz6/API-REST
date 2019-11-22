#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

from recursos.Coches import coches_api, Coche
from recursos.Talleres import talleres_api, Taller

from flask.json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Coche):
    	    return {
                	'idCoche': obj.idCoche,
					'matricula': obj.matricula,
					'marca': obj.marca,
					'fechaFabricacion': obj.fechaFabricacion,
					'tipoAveria': obj.tipoAveria
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
