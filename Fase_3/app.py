from flask import Flask, jsonify, request, render_template, redirect, session
import hashlib
from Estructuras.AVL import AVL
from Estructuras.Arbol_BPensum import ArbolB
# from flask_cors import  CORS
import json

# *------------------------------------------------------ VARIABLES GLOBALES --------------------------------------------------------
arbol_AVL = AVL()
arbol_BPensum = ArbolB()
passwordMaestro = "D4t4_3structur3"
arbol_AVL.generarClave(passwordMaestro)

app = Flask(__name__)
# *----------------------------------------------------------- FUNCIONES ------------------------------------------------------------

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
        with open(path, encoding='utf8') as archivo:
            datos = json.load(archivo)

            for estudiante in datos['estudiantes']:
                carnet = estudiante['carnet']
                dpi = estudiante['DPI']
                nombre = estudiante['nombre']
                carrera = estudiante['carrera']
                correo = estudiante['correo']
                password = estudiante['password']
                edad = estudiante['edad']
                arbol_AVL.add(str(carnet), str(dpi), nombre, carrera, sha256(password), 0, str(edad), correo)

        return jsonify({'Tipo': tipo, 'Mensaje': 'Se han cargado los estudiantes con exito'})

    elif  tipo == "curso":
        if arbol_AVL.root is not None:
            path = request.json['path']

            with open(path, encoding='utf8') as archivo:
                datos = json.load(archivo)

                for estudiante in datos['Estudiantes']:
                    carnet = estudiante['Carnet']
                    alumno = arbol_AVL.search(int(carnet))
                    if alumno is not None:

                        for anios in estudiante['Años']:
                            anio = anios['Año']
                            listaYears = alumno.listaAnios
                            if listaYears.search(anio) is False:
                                listaYears.append(anio)

                            # ! ESTOY TRABAJANDO AQUI
                            listaSemestres = listaYears.getSemestres(anio)

                            for semestres in anios['Semestres']:
                                semestre = semestres['Semestre']

                                if semestre == "1" or semestre == "2":
                                    if listaSemestres.search(semestre) is False:
                                        listaSemestres.append(semestre)
                                    
                                    Arbol_cursos = listaSemestres.getCursosSemestre(semestre)

                                    for cursos in semestres['Cursos']:
                                        codigo = cursos['Codigo']
                                        nombre = cursos['Nombre']
                                        creditos = cursos['Creditos']
                                        prerequisitos = cursos['Prerequisitos']
                                        obligatorio = cursos['Obligatorio']

                                        Arbol_cursos.appendDatos(codigo, nombre, creditos, prerequisitos, str(obligatorio))
                                        # print("\t\t\t"+codigo)
                                        # print("\t\t\t"+nombre)
                                        # print("\t\t\t"+str(creditos))
                                        # print("\t\t\t"+prerequisitos)
                                        # print("\t\t\t"+str(obligatorio))
                                        # print("")

                                else:
                                    print("Error, solo se admiten semetre 1 y semestre 2")

                                
                                
                    else:
                        return jsonify({'Error': 'El carnet '+str(carnet)+' no se encuentra registrado'})

            return jsonify({'Tipo': tipo, 'Mensaje': 'Se han cargado los cursos de los alumnos con exito'})

        else:
            return jsonify({'Error': 'Error no hay alumnos registrados'})
        
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
        if arbol_AVL.search(carnet) is None:
            arbol_AVL.add(carnet, dpi, nombre, carrera, sha256(password), creditos, edad, correo)
            return jsonify({'Mensaje': True})
        else:
            return jsonify({'Mensaje': False})

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
                                # IMPLEMENTAR ELIMINAR DISPERSA
                                if tasks.tamanio == 0:
                                    tareasMes.delete(hora, dia)
                                    # tasks.cabeza = None
                                    # tasks.cola = None
                                    # tasks.id = 1
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
    datos = request.json['Estudiantes']
    if arbol_AVL.root is not None:

        for estudiante in datos:
            carnet = estudiante['Carnet']
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:

                for anios in estudiante['Años']:
                    anio = anios['Año']
                    listaYears = alumno.listaAnios
                    if listaYears.search(anio) is False:
                        listaYears.append(anio)

                    listaSemestres = listaYears.getSemestres(anio)

                    for semestres in anios['Semestres']:
                        semestre = semestres['Semestre']

                        if semestre == "1" or semestre == "2":
                            if listaSemestres.search(semestre) is False:
                                listaSemestres.append(semestre)
                            
                            Arbol_cursos = listaSemestres.getCursosSemestre(semestre)

                            for cursos in semestres['Cursos']:
                                codigo = cursos['Codigo']
                                nombre = cursos['Nombre']
                                creditos = cursos['Creditos']
                                prerequisitos = cursos['Prerequisitos']
                                obligatorio = cursos['Obligatorio']

                                Arbol_cursos.appendDatos(codigo, nombre, creditos, prerequisitos, str(obligatorio))
                                

                        else:
                            print("Error, solo se admiten semetre 1 y semestre 2")


            else:
                return jsonify({'Error': 'El carnet '+str(carnet)+' no se encuentra registrado'})

        return jsonify({'Mensaje': 'Se han cargado los cursos de los estudiantes con exito'})

    else:
        return jsonify({'Error': 'Error no hay alumnos registrados'})

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
                            # if tasks.tamanio != 0:
                            tasks.graficar()
                            return jsonify({'Mensaje': 'Reporte generado con exito'})
                            # else:
                            #     return jsonify({'Mensaje': 'No encontraron tareas en esta hora y/o dia'})
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
    
    elif tipo == 4:
        carnet = request.json['carnet']
        anio = request.json['año']
        semestre = request.json['semestre']
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(int(carnet))
            if alumno is not None:
                listaYears = alumno.listaAnios
                if listaYears.search(anio) is not False:
                    listaSemestres = listaYears.getSemestres(anio)

                    if listaSemestres.search(semestre) is not False:
                        Arbol_cursos = listaSemestres.getCursosSemestre(semestre)
                        Arbol_cursos.graficar("Cursos año "+anio+" semestre "+semestre, "#006266", "#A3CB38")
                        return jsonify({'Tipo': str(tipo), 'Mensaje': 'Se ha generado el reporte con exito'})
                        
                    else:
                        return jsonify({'Mensaje': 'No se tiene registrado cursos en este semestre'})
                else:
                    return jsonify({'Mensaje': 'No se tiene registrado datos en este año'})
            else:
                return jsonify({'Mensaje': 'El carnet '+str(carnet)+' no se encuentra registrado'})
        else:
            return jsonify({'Mensaje': 'Error no hay alumnos registrados'})
    
    else:
        return jsonify({'Mensaje': 'Error este tipo de reporte no existe'})

# !--------------------------------------------------------- FRONTEND ---------------------------------------------------------------

# ?__________________________________________________________ LOGIN _________________________________________________________________
@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    
    elif request.method == 'POST':
        carnet = request.json['carnet']
        password = request.json['password']
        if carnet == 'admin' and password == 'admin':
            return jsonify({'Mensaje': 'admin'})

        else:
            # TODO: REALIZAR LA VERIFICACION DE CREDENCIALES DESPUES PROCEDER A REALIZAR LAS CARGAS MASIVAS EN ADMIN
            return jsonify({'Mensaje': 'estudiante'})

@app.route('/registrar')
def registrar():
    return render_template('login/registrar.html')
# ?__________________________________________________________ ADMIN  ________________________________________________________________

@app.route('/admin')
def inicioadmin():
    return render_template('admin/inicio.html')

# ?__________________________________________________________ USER  ________________________________________________________________

@app.route('/usuario')
def usuario():
    return render_template('user/inicio.html')

# ^------------------------------------------------------- ENCRIPTACION -------------------------------------------------------------

# &_________________________________________________________ SHA256 _________________________________________________________________

def sha256(dato):
    token = hashlib.sha256(dato.encode()).hexdigest()
    return token

if __name__ == '__main__':
    app.run(debug=True, port=3000)