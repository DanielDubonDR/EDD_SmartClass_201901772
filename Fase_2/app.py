from flask import Flask, jsonify, request
from Analizador.Syntactic import parser
from Analizador.Syntactic import lista_usuarios, lista_tareas
from Estructuras.AVL import AVL
# from flask_cors import  CORS
import json

# *------------------------------------------------------ VARIABLES GLOBALES --------------------------------------------------------
arbol_AVL = AVL()

app = Flask(__name__)
# *----------------------------------------------------------- FUNCIONES ------------------------------------------------------------
def cargarUsuarios(path):
    archivo = open(path,"r", encoding="utf-8")
    contenido = archivo.read()
    archivo.close()

    parser.parse(contenido)
    # print(lista_usuarios)
    while lista_usuarios.isEmpy() != True:
        nodeAux = lista_usuarios.pop()
        arbol_AVL.add(int(nodeAux.carnet), nodeAux.dpi, nodeAux.nombre, nodeAux.carrera, nodeAux.password, nodeAux.creditos, nodeAux.edad, nodeAux.correo)

def cargarTareas(path):
    archivo = open(path,"r", encoding="utf-8")
    contenido = archivo.read()
    archivo.close()

    parser.parse(contenido)
    print(lista_tareas)

# !-------------------------------------------------------------- API ---------------------------------------------------------------

# ?_________________________________________________________ CARGAS MASIVAS __________________________________________________________

@app.route('/carga', methods=['POST'])
def cargaMasiva():
    tipo = request.json['tipo']
    path = request.json['path']
    if tipo == "estudiante":
        cargarUsuarios(path)
        return jsonify({'Tipo': tipo, 'Mensaje': 'Se han cargado los estudiantes con exito'})

    elif tipo == "recordatorio":
        cargarTareas(path)
        return jsonify({'Tipo': tipo, 'Mensaje': 'Se han cargado las tareas con exito'})

    elif  tipo == "curso":
        return jsonify({'Tipo': tipo})
        
    else:
        return jsonify({'Error': 'Tipo invalido'})

# ?______________________________________________________ CRUD ESTUDIANTES __________________________________________________________
@app.route('/estudiante', methods=['POST', 'GET', 'PUT', 'DELETE'])
def CRUD_Estudiantes():
    if request.method == 'POST':
        carnet = request.json['carnet']
        dpi = request.json['DPI']
        nombre = request.json['nombre']
        carrera = request.json['carrera']
        correo = request.json['correo']
        password = request.json['password']
        creditos = request.json['creditos']
        edad = request.json['edad']

        arbol_AVL.add(int(carnet), dpi, nombre, carrera, password, creditos, edad, correo)
        return jsonify({'Mensaje': 'Se ha ingresado un nuevo estudiante con exito'})

    elif request.method == 'GET':
        carnet = request.json['carnet']
        if arbol_AVL.root is not None:
            nodeAux = arbol_AVL.search(int(carnet))
            if nodeAux is not None:
                datos = {'carnet': nodeAux.carnet, 'DPI': nodeAux.dpi, 'nombre': nodeAux.nombre, 'carrera': nodeAux.carrera, 'correo': nodeAux.correo, 'password': nodeAux.password, 'creditos': nodeAux.creditos, 'edad': nodeAux.edad}
                return jsonify(datos)
            else:
                return jsonify({'Mensaje': 'Alumno no encontrado'})
        else:
            return jsonify({'Error': 'No se ha registrado ningun alumno aun'})
    
    elif request.method == 'PUT':
        if arbol_AVL.root is not None:
            carnet = request.json['carnet']
            dpi = request.json['DPI']
            nombre = request.json['nombre']
            carrera = request.json['carrera']
            correo = request.json['correo']
            password = request.json['password']
            creditos = request.json['creditos']
            edad = request.json['edad']
            nodeAux = arbol_AVL.search(int(carnet))
            if nodeAux is not None:
                nodeAux.dpi = dpi
                nodeAux.nombre = nombre
                nodeAux.carrera = carrera
                nodeAux.correo = correo
                nodeAux.password = password
                nodeAux.creditos = creditos
                nodeAux.edad = edad
                return jsonify({'Mensaje': 'Se ha modificado al alumno con exito'})
            else:
                return jsonify({'Mensaje': 'Alumno no encontrado'})
        else:
            return jsonify({'Error': 'No se ha registrado ningun alumno aun'})
    
    elif request.method == 'DELETE':
        if arbol_AVL.root is not None:
            carnet = request.json['carnet']
            nodeAux = arbol_AVL.search(int(carnet))
            if nodeAux is not None:
                arbol_AVL.delete(int(carnet))
                return jsonify({'Mensaje': 'Se ha eliminado al alumno con exito'})
            else:
                return jsonify({'Mensaje': 'Alumno no encontrado'})
        else:
            return jsonify({'Error': 'No se ha registrado ningun alumno aun'})

# ?_________________________________________________________ REPORTES _______________________________________________________________
@app.route('/reporte', methods=['GET'])
def graficarALV():
    tipo = request.json['tipo']
    if tipo == 0:
        if arbol_AVL.root is not None:
            arbol_AVL.graficar()
            return jsonify({'Tipo': str(tipo), 'Mensaje': 'Se ha generado el reporte con exito'})
        else:
            return jsonify({'ERROR': 'No se ha ingresado alumnos'})

if __name__ == '__main__':
    app.run(debug=True, port=3000)