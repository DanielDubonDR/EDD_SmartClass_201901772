from pathlib import Path
import os
import shutil
from Estructuras.List import List

class NodeGraph:
    def __init__ (self, codigo, nombre, creditos, list ):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.list = list
        self.siguiente = None
        self.anterior = None

class AdjacencyList:
    def __init__ (self):
        self.cabeza = None
        self.cola = None

    def getSize(self):
        aux = self.cabeza
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.siguiente

        return counter
    
    def isEmpy(self):
        return self.cabeza is None
    
    def getList(self):
        aux = self.cabeza
        counter = 0
        adjacency_list = ""
        while aux is not None:
            if not aux.list.isEmpy():
                aux2 = aux.list.cabeza
                while aux2 is not None:
                    adjacency_list += " -> " + str(aux2.codigo)+ " "+ str(aux2.nombre)
                    aux2 = aux2.siguiente
            print(str(counter) + ") "+str(aux.codigo) + ":"+ adjacency_list)
            adjacency_list = ""
            counter += 1
            aux = aux.siguiente
        
    def exists(self, verification_number):
        aux = self.cabeza
        while aux is not None:
            if aux.codigo == verification_number:
                return True
            aux = aux.siguiente
        return False
    
    def getNode(self, codigo):
        aux = self.cabeza
        while aux is not None:
            if aux.codigo == codigo:
                return aux
            aux = aux.siguiente
        print("no encontrado"+codigo)
    
    def insert(self, codigo, nombre, creditos):
        if not self.exists(codigo):
            new_list = List()
            new_node =  NodeGraph(codigo, nombre, creditos, new_list)
            if self.isEmpy():
                self.cola = new_node
                self.cabeza = self.cola
            else:
                self.cola.siguiente = new_node
                new_node.anterior = self.cola
                self.cola = new_node
        
        else:
            print("Valor repetido")
    
    def edge(self, value1, value2):
        aux = self.cabeza
        while aux is not None:
            if aux.codigo == value1:
                node = self.getNode(value2)
                aux.list.insert(value2, node.nombre, node.creditos)
                break
            aux = aux.siguiente
    
    def getListList(self, codigo):
        aux = self.cabeza
        while aux is not None:
            if aux.codigo == codigo:
                return aux.list.getList()
            aux = aux.siguiente


    def generateMap(self, codigo):
        primero = True
        self.string = """
digraph G {
rankdir=RL;
splines=false;
node[shape=box3d color="#006266" style = "filled" fillcolor = "#00d2d3" penwidth=2 width=4.5]
edge[color="#027575" penwidth=1.3 dir="back" arrowtail="vee"]; """
        lista = [self.getNode(codigo)]
        while lista:
            nodeActual = lista.pop(0)
            if primero:
                self.string += "\nn"+str(nodeActual.codigo)+" [label=\""+str(nodeActual.codigo)+"\\n"+str(nodeActual.nombre)+"\" shape=box3d color=\"#c23616\" style=\"filled\" fillcolor=\"#ff6b6b\" fontcolor=white penwidth=2]"
                primero = False
            else:
                self.string += "\nn"+str(nodeActual.codigo)+" [label=\""+str(nodeActual.codigo)+"\\n"+str(nodeActual.nombre)+"\"]"
            # print(nodeActual.codigo)
            
            sucesores = self.getListList(nodeActual.codigo)
            if sucesores:
                for items in sucesores:
                    self.string += "\nn"+str(nodeActual.codigo)+" -> n"+str(items.codigo)+"[label=\""+str(items.creditos)+"\" tailport=w headport=e];"
                lista.extend(sucesores)
        self.string += "\n}"
        # print(self.string)
        self.eliminarDuplicados()
    
    def eliminarDuplicados(self):
        lineSeen = set()
        aux = self.string
        self.string = ""
        for line in aux.splitlines():
            if line not in lineSeen:
                self.string += "\n"+line
                lineSeen.add(line)
        self.generarArchivo()
    
    def generarArchivo(self):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\Reportes_F3"
        path_current = "{}{}".format(os.path.abspath(os.path.dirname(__file__)), '\\')
        path_current = path_current.replace("\\Estructuras", "")+"Archivos_dot"
        pathdot = Path(path_current)
        pathdot.mkdir(parents=True, exist_ok=True)
        path = Path(path_desktop)
        path.mkdir(parents=True, exist_ok=True)
        archivo=open("Archivos_dot\\graph.dot", 'w', encoding='utf8')
        archivo.write(self.string)
        archivo.close()
        os.system('cd Archivos_dot& dot -Tpdf graph.dot -o '+path_desktop+'\\redEstudios.pdf')
        shutil.copy(path_desktop+'\\redEstudios.pdf', 'static\\reportes\\redEstudios.pdf')