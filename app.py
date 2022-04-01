
import json
from flask import Flask, jsonify, make_response, request
import flask
from controllers import estudiantecontroller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para validar el funcionamiento del servidor
@app.route('/',methods=['GET'])
def Test():
    return make_response('Hola mundo', 200)


# Ruta para obtener todos los estudiantes desde la base de datos
@app.route('/estudiante', methods=['GET'])
def obtenerEstudiantes():
    result = {'msg':'', 'code':200} 
    try:
        result = estudiantecontroller.obtenerEstudiantes()
    except Exception as err:
        print(err)
        result = {'msg':err, 'code':500} 
    
    result = flask.Response(
        status=result['code'],
        response=json.dumps(result['msg']),
        mimetype='application/json',
        headers={'Access-Control-Allow-Origin':'*'}
    )

    return result


# Ruta para insertar estudiante
@app.route('/estudiante', methods=['POST'])
def insertarEstudiantes():
    result = {'msg':'', 'code':200} 
    body = request.get_json()
    try:
        result = estudiantecontroller.insertarEstudiante({
            'carnet':int(body.get('carnet')),
            'nombre':body.get('nombre')
        })
    except Exception as err:
        print(err)
        result = {'msg':err, 'code':500} 
    
    result = flask.Response(
        status=result['code'],
        response=json.dumps(result['msg']),
        mimetype='application/json',
        headers={'Access-Control-Allow-Origin':'*'}
    )
    
    return result


# Ruta para eliminar estudiante
@app.route('/estudiante/<int:carnet>', methods=['DELETE'])
def eliminarEstudiantes(carnet):
    result = {'msg':'', 'code':200} 

    try:
        result = estudiantecontroller.eliminarEstudiante({
            'carnet':int(carnet)
        })
    except Exception as err:
        print(err)
        result = {'msg':err, 'code':500} 
    
    result = flask.Response(
        status=result['code'],
        response=json.dumps(result['msg']),
        mimetype='application/json',
        headers={'Access-Control-Allow-Origin':'*'}
    )
    
    return result