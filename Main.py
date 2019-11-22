#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

from recursos.Coches import coches_api, Coche
from recursos.Talleres import talleres_api, Taller

from flask.json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Averias):
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
        if isinstance(obj, Clientes):
             return {
					'idCliente':obj.idCliente,
                	'nombre': obj.nombre,
					'domicilio': obj.domicilio,
                    'fechaNacimiento': obj.fechaNacimiento
        		    }
        if isinstance(obj, Mecanicos):
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
app.register_blueprint(mecanicos_api)
app.register_blueprint(clientes_api)

if __name__ == '__main__':
    app.run(debug=True)
