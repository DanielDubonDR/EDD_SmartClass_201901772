from flask import Flask, jsonify, request
from Analizador.Syntactic import parser
from Analizador.Syntactic import lista_usuarios, lista_tareas
from Estructuras.AVL import AVL
from Estructuras.Arbol_BPensum import ArbolB
# from flask_cors import  CORS
import json

# *------------------------------------------------------ VARIABLES GLOBALES --------------------------------------------------------
arbol_AVL = AVL()
arbol_BPensum = ArbolB()

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
# ?______________________________________________________ CRUD RECORDATORIOS __________________________________________________________
@app.route('/recordatorios', methods=['POST', 'GET', 'PUT', 'DELETE'])
def CRUD_Recordatorios():
    if request.method == 'POST':
        carnet = request.json['Carnet']
        nombre = request.json['Nombre']
        descripcion = request.json['Descripcion']
        materia = request.json['Materia']
        fecha = request.json['Fecha']
        hr = request.json['Hora']
        estado = request.json['Estado']
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:
                listaYears = alumno.listaAnios
                anio = getAnio(fecha)
                if listaYears.search(anio) is False:
                    listaYears.append(anio)

                listaMeses = listaYears.get(anio)
                mes = getMes(fecha)
                
                if listaMeses.search(mes) is False:
                    listaMeses.append(mes)
                
                tareasMes = listaMeses.get(mes)
                dia = getDia(fecha)
                hora = getHora(hr)
                if tareasMes.verificarExiste(hora,dia) is False:
                    tareasMes.append(hora,dia)

                tasks = tareasMes.getLista(hora, dia)
                tasks.append(carnet, nombre, descripcion, materia, fecha, hr, estado)

                return jsonify({'Mensaje': 'Se ha creado el recordatorio con exito'})

            else:
                return jsonify({'Error': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error, no hay alumnos registrados'})
    
    elif request.method == 'GET':
        carnet = request.json['Carnet']
        fecha = request.json['Fecha']
        hora = request.json['Hora']
        posicion = request.json['Posicion']
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:
                listaYears = alumno.listaAnios
                anio = getAnio(fecha)
                if listaYears.search(anio) is not False:
                    listaMeses = listaYears.get(anio)
                    mes = getMes(fecha)

                    if listaMeses.search(mes) is not False:
                    
                        tareasMes = listaMeses.get(mes)
                        dia = getDia(fecha)
                        hora = getHora(hora)
                        if tareasMes.verificarExiste(hora,dia) is not False:
                            tasks = tareasMes.getLista(hora, dia)
                            task = tasks.get(posicion)
                            if task is not None:
                                data = {
                                    'Carnet': task.carnet,
                                    'Nombre': task.nombre,
                                    'Descripcion': task.descripcion,
                                    'Materia': task.materia,
                                    'Fecha': task.fecha,
                                    'Hora': task.hora,
                                    'Estado': task.estado,
                                    'Posicion': task.id
                                }
                                return jsonify(data)
                            else:
                                return jsonify({'Mensaje': 'Error, no existe alguna tarea en la posicion indicada'})
                        else:
                            return jsonify({'Mensaje': 'No encontraron tareas en esta hora y/o dia'})
                    else:
                        return jsonify({'Mensaje': 'No se tiene registradas tareas en este mes'})
                else:
                    return jsonify({'Mensaje': 'No se tiene registrado ningun evento en este año'})
            else:
                return jsonify({'Error': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error, no hay alumnos registrados'})
    
    elif request.method == 'PUT':
        carnet = request.json['Carnet']
        nombre = request.json['Nombre']
        descripcion = request.json['Descripcion']
        materia = request.json['Materia']
        fecha = request.json['Fecha']
        hora = request.json['Hora']
        estado = request.json['Estado']
        posicion = request.json['Posicion']
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:
                listaYears = alumno.listaAnios
                anio = getAnio(fecha)
                if listaYears.search(anio) is not False:
                    listaMeses = listaYears.get(anio)
                    mes = getMes(fecha)

                    if listaMeses.search(mes) is not False:
                    
                        tareasMes = listaMeses.get(mes)
                        dia = getDia(fecha)
                        hora = getHora(hora)
                        if tareasMes.verificarExiste(hora,dia) is not False:
                            tasks = tareasMes.getLista(hora, dia)
                            task = tasks.get(posicion)
                            if task is not None:
                                task.nombre = nombre
                                task.descripcion = descripcion
                                task.materia = materia
                                task.estado = estado
                                return jsonify({'Mensaje': 'Se ha modificado el recordatorio con exito'})
                            else:
                                return jsonify({'Mensaje': 'Error, no existe alguna tarea en la posicion indicada'})
                        else:
                            return jsonify({'Mensaje': 'No encontraron tareas en esta hora y/o dia'})
                    else:
                        return jsonify({'Mensaje': 'No se tiene registradas tareas en este mes'})
                else:
                    return jsonify({'Mensaje': 'No se tiene registrado ningun evento en este año'})
            else:
                return jsonify({'Error': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error, no hay alumnos registrados'})
    
    elif request.method == 'DELETE':
        carnet = request.json['Carnet']
        fecha = request.json['Fecha']
        hora = request.json['Hora']
        posicion = request.json['Posicion']
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:
                listaYears = alumno.listaAnios
                anio = getAnio(fecha)
                if listaYears.search(anio) is not False:
                    listaMeses = listaYears.get(anio)
                    mes = getMes(fecha)

                    if listaMeses.search(mes) is not False:
                    
                        tareasMes = listaMeses.get(mes)
                        dia = getDia(fecha)
                        hora = getHora(hora)
                        if tareasMes.verificarExiste(hora,dia) is not False:
                            tasks = tareasMes.getLista(hora, dia)
                            task = tasks.get(posicion)
                            if task is not None:
                                tasks.delete(posicion)
                                # TODO: IMPLEMENTAR ELIMINAR DISPERSA
                                if tasks.tamanio == 0:
                                    tasks.cabeza = None
                                    tasks.cola = None
                                    tasks.id = 1
                                return jsonify({'Mensaje': 'Se ha eliminado la tarea satisfactoriamente'})
                            else:
                                return jsonify({'Mensaje': 'Error, no existe alguna tarea en la posicion indicada'})
                        else:
                            return jsonify({'Mensaje': 'No encontraron tareas en esta hora y/o dia'})
                    else:
                        return jsonify({'Mensaje': 'No se tiene registradas tareas en este mes'})
                else:
                    return jsonify({'Mensaje': 'No se tiene registrado ningun evento en este año'})
            else:
                return jsonify({'Error': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error, no hay alumnos registrados'})

# ?________________________________________________________ CRUD CURSOS _____________________________________________________________
@app.route('/cursosPensum', methods=['POST'])
def CreateCursosPensum():
    cursos = request.json['Cursos']
    for curso in cursos:
        codigo = curso['Codigo']
        nombre = curso['Nombre']
        creditos = curso['Creditos']
        prerequisitos = curso['Prerequisitos']
        obligatorio = curso['Obligatorio']
        arbol_BPensum.appendDatos(codigo, nombre, creditos, prerequisitos, str(obligatorio))
        # print(codigo+" "+nombre+" "+str(creditos)+" "+prerequisitos+" "+str(obligatorio))
    return jsonify({'Mensaje': 'Se han cargado los cursos con exito'})

@app.route('/cursosEstudiante', methods=['POST'])
def CreateCursosEstudiante():
    cursos = request.json['Estudiantes']
    return jsonify({'Mensaje': 'Leido con exito'})

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
                            if tasks.tamanio != 0:
                                tasks.graficar()
                                return jsonify({'Mensaje': 'Reporte generado con exito'})
                            else:
                                return jsonify({'Mensaje': 'No encontraron tareas en esta hora y/o dia'})
                        else:
                            return jsonify({'Mensaje': 'No encontraron tareas en esta hora y/o dia'})
                    else:
                        return jsonify({'Mensaje': 'No se tiene registradas tareas en este mes'})
                else:
                    return jsonify({'Mensaje': 'No se tiene registrado ningun evento en este año'})
            else:
                return jsonify({'Mensaje': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error no hay alumnos registrados'})
    
    elif tipo == 3:
        if arbol_BPensum.raiz is not None:
            arbol_BPensum.graficar("Cursos Pensum", "#0a3d62", "#82ccdd")
            return jsonify({'Tipo': str(tipo), 'Mensaje': 'Se ha generado el reporte con exito'})
        else:
            return jsonify({'ERROR': 'No se ha ingresado cursos al pensum'})
    
# TODO: Generar reporte 4

if __name__ == '__main__':
    app.run(debug=True, port=3000)