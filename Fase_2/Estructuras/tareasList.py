from pathlib import Path
import os

class Nodo:
    def __init__(self, id, carnet, nombre, descripcion, materia, fecha, hora, estado):
        self.id = id
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.siguiente = None
    
    def __str__(self):
        return str(self.id)+str("\n")+str(self.nombre)+str("\n")+str(self.materia)

class Lista_Simple:
    def __init__(self):
        self.cabeza = self.cola = None
        self.id = 1
        self.tamanio = 0
    
    def isEmpy(self):
        if self.cabeza == None and self.cola ==None:
            return True
        else:
            return False
            
    def append(self, carnet, nombre, descripcion, materia, fecha, hora, estado):
        newNode = Nodo((self.tamanio+1), carnet, nombre, descripcion, materia, fecha, hora, estado)
        if self.isEmpy():
            self.cabeza = self.cola = newNode
            self.tamanio += 1
        else:
            self.cola.siguiente = newNode
            self.cola = newNode
            self.tamanio += 1
    
    def prepend(self, dato):
        newNode = Nodo(dato)
        if self.isEmpy():
            self.cabeza = self.cola = newNode
            self.tamanio += 1
        else:
            newNode.siguiente = self.cabeza
            self.cabeza = newNode
            self.tamanio += 1
    
    def shift(self):
        if self.tamanio == 1:
            self.cabeza = self.cola = None
            self.tamanio = 0
        else:
            nodeAux = self.cabeza
            self.cabeza = nodeAux.siguiente
            nodeAux.siguiente = None
            self.tamanio-=1
            
    def pop(self):
        if self.tamanio == 1:
            # nodeAux = self.cabeza
            self.cabeza = self.cola = None
            self.tamanio = 0
            # return nodeAux.dato
        else:
            nodeAux = newCola = self.cabeza
            while nodeAux.siguiente != None:
                newCola = nodeAux
                nodeAux = nodeAux.siguiente
            newCola.siguiente = None
            self.cola = newCola
            self.tamanio-=1
            # return nodeAux.dato

    def get(self, id):
        nodeAux = self.cabeza
        while nodeAux != None:
            if nodeAux.id == id:
                return nodeAux
            nodeAux = nodeAux.siguiente
        return None

    def update(self, id, dato):
        nodeAux = self.get(id)
        nodeAux.dato=dato

    def insert(self, id, dato):
        newNode = Nodo(dato)
        nodeAux = self.cabeza
        previous = None
        while nodeAux and nodeAux.dato != id:
            previous = nodeAux
            nodeAux = nodeAux.siguiente
        if previous is None:
            self.prepend(dato)
            self.tamanio +=1
        elif nodeAux:
            previous.siguiente = newNode
            newNode.siguiente = nodeAux
            self.tamanio +=1
    
    def delete(self, id):
        nodeAux = self.cabeza
        previous = None
        while nodeAux and nodeAux.dato != id:
            previous = nodeAux
            nodeAux = nodeAux.siguiente
        if previous is None:
            self.cabeza = nodeAux.siguiente
            self.tamanio -=1
        elif nodeAux:
            previous.siguiente = nodeAux.siguiente
            nodeAux.siguiente = None
            self.tamanio -=1
    
    def reverse(self):
        intercambio = None
        nodeAux = self.cabeza
        self.cola = nodeAux
        while nodeAux != None:
            nodoSig = nodeAux.siguiente
            nodeAux.siguiente = intercambio
            intercambio = nodeAux
            nodeAux = nodoSig
        self.cabeza = intercambio

    def graficar(self):
        string = """
        digraph List {
        rankdir=LR;
        label="\\nLista de Tareas """+str(self.cabeza.fecha)+str(" ")+str(self.cabeza.hora)+""" " fontsize=20;
        node [shape = note, color="#187296", style=filled, fillcolor="#7ed6df" penwidth=2.3];
        """
        conectarNodos = ""
        nodeAux = self.cabeza
        while nodeAux != None:
            string += "\n\t\tN"+str(nodeAux.id)+" [label=\"\ID tarea: "+str(nodeAux.id)+" \lCarnet: "+str(nodeAux.carnet)+" \lNombre: "+str(nodeAux.nombre)+" \lDescripcion: "+str(nodeAux.descripcion)+" \lMateria: "+str(nodeAux.materia)+" \lFecha: "+str(nodeAux.fecha)+" \lHora: "+str(nodeAux.hora)+" \lEstado: "+str(nodeAux.estado)+"\l\"];"
            if nodeAux.siguiente is not None:
                conectarNodos += "\n\t\tN"+str(nodeAux.id)+" -> N"+str(nodeAux.siguiente.id)
            nodeAux = nodeAux.siguiente
        string += conectarNodos
        string += "\n}"
        self.generarArchivo(string)

    def generarArchivo(self, string):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\Reportes_F2"
        path_current = "{}{}".format(os.path.abspath(os.path.dirname(__file__)), '\\')
        path_current = path_current.replace("\\Estructuras", "")+"Archivos_dot"
        pathdot = Path(path_current)
        pathdot.mkdir(parents=True, exist_ok=True)
        path = Path(path_desktop)
        path.mkdir(parents=True, exist_ok=True)
        archivo=open("Archivos_dot\\ListaTareas.dot", 'w', encoding='utf8')
        archivo.write(string)
        archivo.close()
        os.system('cd Archivos_dot& dot -Tpdf ListaTareas.dot -o '+path_desktop+'\\ListaTareas.pdf')
        os.startfile(path_desktop+"\\ListaTareas.pdf")


    def __str__(self):
        string = ""
        nodeAux = self.cabeza
        while nodeAux != None:
            string += str(nodeAux)
            nodeAux = nodeAux.siguiente
        return string
