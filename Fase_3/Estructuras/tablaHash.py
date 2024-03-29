
# &_________________________________________________________ tablaHash.py _________________________________________________________________

import Estructuras.Solovay_Strassen as primo
import os
from pathlib import Path
import shutil

class Node:
    def __init__(self, carnet, list):
        self.carnet = carnet
        self.list = list

class tablaHash:
    def __init__(self):
        self.string = ""
        self.enlaces = ""
        self.n = 0
        self.size = 7
        self.hash_list = []
    
        for i in range(self.size):
            self.hash_list.append(None)

    def getTable(self):
        for i in range(self.size):
            if self.hash_list[i] is not None:
                print(str(i)+ ") " + str(self.hash_list[i].carnet))
            else:
                print(str(i)+ ") " +"----")

    def insert(self, carnet, list):
        position = self.getPosition(carnet)

        if self.hash_list[position] is None:
            self.hash_list[position] = Node(carnet, list)
    
        else:
            cont = 1
            while True:
                i = self.exploracionCuadratica(carnet, cont)
                if self.hash_list[i] is None:
                    self.hash_list[i] = Node(carnet, list)
                    break
                
                else:
                    cont += 1

        self.n += 1
        # print(str(self.hash_list.carnet)+" -- "+str(self.getPercentUse()*100)+"%")
        self.reHashing()
    
    def exploracionCuadratica(self, carnet, i):
        position = (self.getPosition(carnet)+(i*i)) % self.size
        return position
    
    def reHashing(self):
        if self.getPercentUse() >= 0.50:
            m = self.getNextPrime(self.size)
            newList = []
            for i in range(m):
                newList.append(None)
            
            auxList = self.hash_list.copy()
            self.size = m
            self.hash_list = newList
            self.n = 0
            for i in range(len(auxList)):
                if auxList[i] is not None:
                    self.insert(auxList[i].carnet, auxList[i].list)

    
    def getPosition(self, carnet):
        return (carnet % self.size)
    
    def getNextPrime(self, initialSize):
        return primo.next(initialSize)
    
    def getPercentUse(self):
        return self.n/self.size
    
    def search(self, carnet):
        cont = 0
        while True:
            i = self.exploracionCuadratica(carnet, cont)
            if self.hash_list[i] is None:
                return None
            elif self.hash_list[i].carnet == carnet:
                return self.hash_list[i]
            else:
                cont += 1
    
    def isEmpy(self):
        if self.n == 0:
            return True
        else:
            return False
    
    def generarReporte(self):
        self.enlaces = ""
        self.string = """digraph G {
        nodesep=.05;
        rankdir=LR;
        node [shape=record color="#c23616" style = "filled" fillcolor = "#ff6b6b" fontcolor=white penwidth=2.5 width = 2.2];"""
        self.generateTable()
        self.string += "\t\t\nnode [shape=note color=\"#01a3a4\" width = 2 height=0.7 style = filled fillcolor = \"#00d2d3\" fontcolor=black penwidth=2];"
        self.generateNodos()
        self.string += self.enlaces
        self.string +="\n}"
        self.generarArchivo()
    
    # *node0 [label = " <f0>201901772|<f1>201901772|<f2> 201901772 |<f5>201901772|<f6>201901772" height=3];

    def generateTable(self):
        self.auxstring = ""
        self.string += "\t\t\n\nnode0 [label = \""
        for i in range(self.size):
            if self.hash_list[i] is not None:
                self.string += "<f"+str(i)+">"+str(self.hash_list[i].carnet)+"|"
            elif self.hash_list[i] is None:
                self.string += "<f"+str(i)+"> |"
            self.auxstring += "\na"+str(i)+"[label=\""+str(i)+" \"shape=plain fillcolor=white fontcolor=black fontsize=18]"
            self.auxstring += "\na"+str(i)+" -> node0:f"+str(i)+" [dir=none color=white]"
        
        self.string = self.string[:-1]
        self.string += "\" height="+str(self.size-1)+"];"
        self.string += self.auxstring
    
    def generateNodos(self):
        for i in range(self.size):
            if self.hash_list[i] is not None:
                lista = self.hash_list[i].list.iterar()
                cont = 0
                for apuntes in lista:
                    self.string += "\t\t\nnode"+str(i)+str(apuntes.id)+" [label = \""+str(apuntes.titulo)+"\"];"
                    if cont > 0:
                        self.enlaces += "\t\t\nnode"+str(i)+str(apuntes.id-1)+" -> node"+str(i)+str(apuntes.id)
                    else:
                        self.enlaces += "\t\t\nnode0:f"+str(i)+" -> node"+str(i)+str(apuntes.id)
                    cont += 1

    def generarArchivo(self):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\Reportes_F3"
        path_current = "{}{}".format(os.path.abspath(os.path.dirname(__file__)), '\\')
        path_current = path_current.replace("\\Estructuras", "")+"Archivos_dot"
        pathdot = Path(path_current)
        pathdot.mkdir(parents=True, exist_ok=True)
        path = Path(path_desktop)
        path.mkdir(parents=True, exist_ok=True)
        archivo=open("Archivos_dot\\Apuntes.dot", 'w', encoding='utf8')
        archivo.write(self.string)
        archivo.close()
        os.system('cd Archivos_dot& dot -Tpdf Apuntes.dot -o '+path_desktop+'\\ApuntesEstudiantes.pdf')
        shutil.copy(path_desktop+'\\ApuntesEstudiantes.pdf', 'static\\reportes\\ApuntesEstudiantes.pdf')