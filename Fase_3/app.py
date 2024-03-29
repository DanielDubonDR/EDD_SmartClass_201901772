from flask import Flask, jsonify, request, render_template, redirect, session
import hashlib
from Estructuras.AVL import AVL
from Estructuras.Arbol_BPensum import ArbolB
from Estructuras.tablaHash import tablaHash
from Estructuras.listaApuntes import notesList
from Estructuras.adjacencyList import AdjacencyList
# from flask_cors import  CORS
import json

# *------------------------------------------------------ VARIABLES GLOBALES --------------------------------------------------------
arbol_AVL = AVL()
arbol_BPensum = ArbolB()
passwordMaestro = "D4t4_3structur3"
passEstablecida = False
hash_Table = tablaHash()
graph = AdjacencyList()
# arbol_AVL.generarClave(passwordMaestro)

app = Flask(__name__)
app.secret_key = b'_Esta_3s_Una_CLAV3_js_js_js_j_xD_'
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

def isEmpyArbol():
    if arbol_AVL.root is None:
        return True
    else:
        return False

def loadGraph():
    if graph.isEmpy():
        txt = arbol_BPensum.getData()
        txt = txt[:-1]
        txt = txt.split("#")
        for elementos in txt:
            aux = elementos.split("-")
            codigo = aux[0]
            nombre = aux[1]
            creditos = aux[2]
            graph.insert(codigo, nombre, creditos)
        
        for elementos in txt:
            aux = elementos.split("-")
            codigo = aux[0]
            prerequisitos = aux[3]
            if prerequisitos != "":
                prerequisitos = prerequisitos.split(",")
                for prerequisito in prerequisitos:
                    graph.edge(codigo, prerequisito)

    # graph.edge("0103","0101")
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

@app.route('/cargaMasivaEstudiantes', methods=['POST'])
def loadEstudiantes():
    datos = request.json['estudiantes']
    for estudiante in datos:
        carnet = estudiante['carnet']
        dpi = estudiante['DPI']
        nombre = estudiante['nombre']
        carrera = estudiante['carrera']
        correo = estudiante['correo']
        password = estudiante['password']
        edad = estudiante['edad']
        arbol_AVL.add(str(carnet), str(dpi), nombre, carrera, sha256(password), 0, str(edad), correo)
    
    return jsonify({'Mensaje': True})

@app.route('/loadApuntes', methods=['POST'])
def loadApuntes():
    datos = request.json['usuarios']
    for usuario in datos:
        notes = notesList()
        carnet = usuario['carnet']
        # print(carnet)
        for apunte in usuario['apuntes']:
            titulo = apunte['Título']
            contenido = apunte['Contenido']
            notes.append(titulo, contenido)
        
        hash_Table.insert(carnet, notes)
    
    return jsonify({'Mensaje': True})

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
    return jsonify({'Mensaje': True})


@app.route('/cursosEstudiante', methods=['POST'])
def CreateCursosEstudiante():
    datos = request.json['Estudiantes']
    if arbol_AVL.root is not None:

        for estudiante in datos:
            carnet = estudiante['Carnet']
            alumno = arbol_AVL.search(carnet)
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

        return jsonify({'Mensaje': True})

    else:
        return jsonify({'Error': 'Error no hay alumnos registrados'})

# ?_________________________________________________________ REPORTES _______________________________________________________________
@app.route('/reporte', methods=['POST'])
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
        carnet = session['user']
        anio = request.json['anio']
        semestre = request.json['semestre']
        if semestre == "Primer semestre":
            semestre = "1"
        else:
            semestre = "2"
        if arbol_AVL.root is not None:
            alumno = arbol_AVL.search(carnet)
            if alumno is not None:
                listaYears = alumno.listaAnios
                if listaYears.search(anio) is not False:
                    listaSemestres = listaYears.getSemestres(anio)

                    if listaSemestres.search(semestre) is not False:
                        Arbol_cursos = listaSemestres.getCursosSemestre(semestre)
                        Arbol_cursos.graficar("Cursos año "+anio+" semestre "+semestre, "#006266", "#A3CB38")
                        return jsonify({'Mensaje': True})
                        
                    else:
                        return jsonify({'Mensaje': 'semestre'})
                else:
                    return jsonify({'Mensaje': 'anio'})
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
    if 'user' in session:
        if session['user'] == "admin":
            return redirect("/admin")
        else:
            return redirect("/usuario")
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    
    elif request.method == 'POST':
        carnet = request.json['carnet']
        password = request.json['password']
        if carnet == 'admin' and password == 'admin':
            session['user'] = "admin"
            session['nombre'] = "admin"
            return jsonify({'Mensaje': 'admin'})

        else:
            if arbol_AVL.validar(carnet, sha256(password)):
                session['user'] = carnet
                session['nombre'] = arbol_AVL.getNombre(carnet)
                return jsonify({'Mensaje': 'estudiante'})
            else:
                return jsonify({'Mensaje': 'error'})

@app.route('/registrar')
def registrar():
    return render_template('login/registrar.html')

@app.route('/logout')
def cerrarSesion():
    session.pop('user')
    session.pop('nombre')
    return redirect('/')
# ?__________________________________________________________ ADMIN  ________________________________________________________________

@app.route('/admin')
def inicioadmin():
    return render_template('admin/inicio.html')

@app.route('/pass')
def passwordM():
    return render_template('admin/password.html')

@app.route('/masivaPensum')
def masivaPensum():
    return render_template('admin/cargarPensum.html')

@app.route('/setPass', methods=['POST'])
def setPass():
    if request.method == 'POST':
        pw = request.json['pw']
        global passwordMaestro
        global passEstablecida
        passwordMaestro = pw;
        arbol_AVL.generarClave(passwordMaestro)
        passEstablecida = True
        return jsonify({'Mensaje': True})

@app.route('/cargarUsers')
def cargarUsers():
    return render_template('admin/cargarEstudiantes.html', pasw=passEstablecida)

@app.route('/cargarCursosUsers')
def cargarCursosUsers():
    return render_template('admin/cargarCursosEs.html', arbol=isEmpyArbol())

@app.route('/reporteUsuarios')
def reporteUsuarios():
    if isEmpyArbol():
        return render_template('admin/reporteUsuarios.html', arbol=True)
    else:
        arbol_AVL.graficar()
        return render_template('admin/reporteUsuarios.html', arbol=False)

@app.route('/cargarApuntes')
def cargarApuntes():
    return render_template('admin/cargarApuntes.html')

@app.route('/reporteApuntes')
def reporteApuntes():
    if hash_Table.isEmpy():
        return render_template('admin/reporteApuntes.html', table=True)
    else:
        hash_Table.generarReporte()
        return render_template('admin/reporteApuntes.html', table=False)

@app.route('/onBuilding')
def onBuilding():
    return render_template('admin/build.html')


# ?__________________________________________________________ USER  ________________________________________________________________

@app.route('/usuario')
def usuario():
    return render_template('user/inicio.html', user=session['user'], nombre=session['nombre'])

@app.route('/verApuntes')
def verApuntes():
    apunte = hash_Table.search(int(session['user']))
    if apunte is not None:
        return render_template('user/apuntes.html', user=session['user'], apuntes=apunte.list)
    else:
        return render_template('user/apuntes.html', user=session['user'], apuntes=None)

@app.route('/verApunte/<int:id>')
def verApunte(id):
    apunte = hash_Table.search(int(session['user']))
    for i in apunte.list.iterar():
        if i.id == id:

            return render_template('user/visualizarApunte.html', user=session['user'], titulo=i.titulo, contenido=i.contenido)

@app.route('/addApunte')
def addApunte():
    return render_template('user/crearApunte.html', user=session['user'])

@app.route('/addNote', methods=['POST'])
def addNote():
    titulo = request.json['titulo']
    contenido = request.json['contenido']

    apunte = hash_Table.search(int(session['user']))

    if apunte is not None:
        apunte.list.append(titulo, contenido)

        return jsonify({'Mensaje': True})
    
    else:
        newList = notesList()
        newList.append(titulo, contenido)
        hash_Table.insert(int(session['user']), newList)
        
        return jsonify({'Mensaje': True})

@app.route('/addCurso')
def addCurso():
    txt = arbol_BPensum.iterar()
    txt = txt[:-1]
    txt = txt.split("#")
    return render_template('user/asignarCursos.html', user=session['user'], cursos=txt)

@app.route('/addCursoEstudiante', methods=['POST'])
def addCursoEstudiante():
    auxcurso = request.json['curso']
    semestre = request.json['semestre']
    auxcurso = auxcurso.split("-")
    codigo = auxcurso[0]
    nombre = auxcurso[1]
    if semestre == "Primer semestre":
        semestre = "1"
    else:
        semestre = "2"
    
    if arbol_AVL.root is not None:

        
        carnet = session['user']
        alumno = arbol_AVL.search(carnet)
        if alumno is not None:

            anio = "2021"
            listaYears = alumno.listaAnios
            if listaYears.search(anio) is False:
                listaYears.append(anio)

            listaSemestres = listaYears.getSemestres(anio)

            if semestre == "1" or semestre == "2":
                if listaSemestres.search(semestre) is False:
                    listaSemestres.append(semestre)
                
                Arbol_cursos = listaSemestres.getCursosSemestre(semestre)

                creditos = 0
                prerequisitos = ""
                obligatorio = True

                Arbol_cursos.appendDatos(codigo, nombre, creditos, prerequisitos, str(obligatorio))
                
                return jsonify({'Mensaje': True})

            else:
                print("Error, solo se admiten semetre 1 y semestre 2")


        else:
            return jsonify({'Error': 'El carnet '+str(carnet)+' no se encuentra registrado'})

    else:
        return jsonify({'Error': 'Error no hay alumnos registrados'})

@app.route('/verCursosAsignados')
def verCursosAsignados():
    return render_template('user/verCursoEstudiante.html', user=session['user'])

@app.route('/verCursos')
def verCursos():
    return render_template('user/verCursos.html', user=session['user'])

@app.route('/redCursos')
def redCursos():
    return render_template('user/redCursos.html', user=session['user'])

@app.route('/viewRedCursos/<string:codigo>')
def viewRedCursos(codigo):
    loadGraph()
    if graph.search(codigo) is not None:
        graph.generateMap(codigo)
        return render_template('user/viewRedCursos.html', user=session['user'], grafico=True)
    else:
        return render_template('user/viewRedCursos.html', user=session['user'], grafico=False)

@app.route('/reportePensumPre')
def reportePensumPre():
    if arbol_BPensum.raiz is None:
        return render_template('admin/reportePensum.html', user=session['user'], grafico=True)
    else:
        loadGraph()
        graph.generateRed()
        return render_template('admin/reportePensum.html', user=session['user'], grafico=False)


# ^------------------------------------------------------- ENCRIPTACION -------------------------------------------------------------

# &_________________________________________________________ SHA256 _________________________________________________________________

def sha256(dato):
    token = hashlib.sha256(dato.encode()).hexdigest()
    return token

if __name__ == '__main__':
    app.run(debug=True, port=3000)