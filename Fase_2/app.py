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
        arbol_AVL.add(nodeAux.carnet, nodeAux.dpi, nodeAux.nombre, nodeAux.carrera, nodeAux.password, nodeAux.creditos, nodeAux.edad, nodeAux.correo)

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