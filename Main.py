#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

from recursos.Coches import coches_api, Coche
from recursos.Averias import averias_api, Averia
from recursos.Clientes import clientes_api, Cliente
from recursos.Mecanicos import mecanicos_api, Mecanico

from flask.json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Averia):
            return {
                    'idAveria': obj.idAveria,
                    'descripcion': obj.descripcion,
                    'coche': obj.coche
                    }
        if isinstance(obj, Coche):
    	    return {
                	'idCoche': obj.idCoche,
					'matricula': obj.matricula,
					'marca': obj.marca,
					'fechaFabricacion': obj.fechaFabricacion,
					'tipoAveria': obj.tipoAveria
            	   }
        if isinstance(obj, Cliente):
             return {
					'idCliente':obj.idCliente,
                	'nombre': obj.nombre,
					'domicilio': obj.domicilio,
                    'fechaNacimiento': obj.fechaNacimiento
        		    }
        if isinstance(obj, Mecanico):
            return{
                   'idMecanico': obj.idMecanico,
                   'nombre': obj.nombre,
                   }
        return super(MyJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

# Blueprint
app.register_blueprint(averias_api)
app.register_blueprint(coches_api)
app.register_blueprint(clientes_api)
app.register_blueprint(mecanicos_api)

if __name__ == '__main__':
    app.run(debug=True)
