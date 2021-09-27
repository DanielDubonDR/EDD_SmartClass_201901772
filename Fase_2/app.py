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

def getAnio(fecha):
    fecha = fecha.split("/")
    return fecha[2]

def getMes(fecha):
    fecha = fecha.split("/")
    return int(fecha[1])

def getNombreMes(mes):
    if mes == 1:
        return "Enero"
    elif mes == 2:
        return "Febrero"
    elif mes == 3:
        return "Marzo"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Mayo"
    elif mes == 6:
        return "Junio"
    elif mes == 7:
        return "Julio"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Septiembre"
    elif mes == 10:
        return "Octubre"
    elif mes == 11:
        return "Noviembre"
    elif mes == 12:
        return "Diciembre"

def getDia(fecha):
    fecha = fecha.split("/")
    return int(fecha[0])

def getHora(hora):
    hora = hora.split(':')
    return int(hora[0])

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
        #  FIXME: VACIAR LA LISTA DE TAREAS SI SE DESEA INGRESAR DIFERENTE RUTA YA QUE DUPLICA VALORES
        # archivo = open(path,"r", encoding="utf-8")
        # contenido = archivo.read()
        # archivo.close()
        if arbol_AVL.root is not None:
            # parser.parse(contenido)
            while lista_tareas.isEmpy() != True:
                nodeAux = lista_tareas.pop()
                alumno = arbol_AVL.search(int(nodeAux.carnet))
                if alumno is not None:
                    listaYears = alumno.listaAnios
                    anio = getAnio(nodeAux.fecha)
                    if listaYears.search(anio) is False:
                        listaYears.append(anio)

                    listaMeses = listaYears.get(anio)
                    mes = getMes(nodeAux.fecha)
                    
                    if listaMeses.search(mes) is False:
                        listaMeses.append(mes)
                    
                    tareasMes = listaMeses.get(mes)
                    dia = getDia(nodeAux.fecha)
                    hora = getHora(nodeAux.hora)
                    if tareasMes.verificarExiste(hora,dia) is False:
                        tareasMes.append(hora,dia)
                    # tareasMes.recorrerFilas()
                    tasks = tareasMes.getLista(hora, dia)
                    tasks.append(nodeAux.carnet, nodeAux.nombre, nodeAux.descripcion, nodeAux.materia, nodeAux.fecha, nodeAux.hora, nodeAux.estado)
                    # print(tasks)
                    
                    # print(listaMeses)
                    # !----continual aqui

                else:
                    return jsonify({'Error': 'El carnet '+str(nodeAux.carnet)+' no se encuentra registrado'})

            return jsonify({'Tipo': tipo, 'Mensaje': 'Se han cargado las tareas con exito'})
        else:
            return jsonify({'Error': 'Error no hay alumnos registrados'})

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
        if arbol_AVL.search(int(carnet)) is None:
            arbol_AVL.add(int(carnet), dpi, nombre, carrera, password, creditos, edad, correo)
            return jsonify({'Mensaje': 'Se ha ingresado un nuevo estudiante con exito'})
        else:
            return jsonify({'Mensaje': 'Error ya exite un alumno con el mismo carnet'})

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

# TODO: Realizar CRUD recordatorios
# ?_________________________________________________________ REPORTES _______________________________________________________________
@app.route('/reporte', methods=['GET'])
def graficar():
    tipo = request.json['tipo']
    if tipo == 0:
        if arbol_AVL.root is not None:
            arbol_AVL.graficar()
            return jsonify({'Tipo': str(tipo), 'Mensaje': 'Se ha generado el reporte con exito'})
        else:
            return jsonify({'ERROR': 'No se ha ingresado alumnos'})
    
    elif tipo == 1:
        carnet = request.json['carnet']
        anio = request.json['año']
        mes = request.json['mes']
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:
                listaYears = alumno.listaAnios
                if listaYears.search(anio) is not False:
                    listaMeses = listaYears.get(anio)
                    if listaMeses.search(mes) is not False:
                        tareasMes = listaMeses.get(mes)

                        tareasMes.graficar(getNombreMes(mes))
                        return jsonify({'Mensaje': 'Reporte generado con exito'})
                    else:
                        return jsonify({'Mensaje': 'No se tiene registradas tareas en este mes'})
                else:
                    return jsonify({'Mensaje': 'No se tiene registrado de ningun evento en este año'})
            else:
                return jsonify({'Mensaje': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error no hay alumnos registrados'})
        
    elif tipo == 2:
        carnet = request.json['carnet']
        anio = request.json['año']
        mes = request.json['mes']
        dia = request.json['dia']
        hora = request.json['hora']
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:
                listaYears = alumno.listaAnios
                if listaYears.search(anio) is not False:
                    listaMeses = listaYears.get(anio)
                    if listaMeses.search(mes) is not False:
                        tareasMes = listaMeses.get(mes)
                        if tareasMes.verificarExiste(hora,dia) is not False:
                            tasks = tareasMes.getLista(hora, dia)
                            # fecha = str(dia)+"/"+str(mes)+"/"+str(anio)+" "+str(hora)+":00"
                            tasks.graficar()
                            return jsonify({'Mensaje': 'Reporte generado con exito'})
                        else:
                            return jsonify({'Mensaje': 'No encontraron tareas en este dia y hora'})
                    else:
                        return jsonify({'Mensaje': 'No se tiene registradas tareas en este mes'})
                else:
                    return jsonify({'Mensaje': 'No se tiene registrado de ningun evento en este año'})
            else:
                return jsonify({'Mensaje': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error no hay alumnos registrados'})
    
# TODO: Generar reporte 3 y 4

if __name__ == '__main__':
    app.run(debug=True, port=3000)