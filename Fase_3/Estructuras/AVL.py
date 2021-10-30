from logging import fatal
from pathlib import Path
from Estructuras.yearList import DoubleList
import os
import time
from cryptography.fernet import Fernet
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import shutil

class Node:
    def __init__(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo):
        self.carnet = carnet
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.correo = correo
        self.listaAnios = DoubleList()
        self.der = None
        self.izq = None
        self.size = 0
        self.key = None
        self.dt = None

class  AVL:
    def __init__(self):
        self.root = None
        self.string = ""

    # * ----------------------------------------------- Verifica que rama es mayor ----------------------------------------------------
    def max_min(self, v1, v2):
        if v1 > v2:
            return v1
        else:
            return v2
    
    # *----------------------------------------- Metodo incial para agregar un nuevo nodo ---------------------------------------------
    def add(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo):
        self.root = self._add(self.encriptar(carnet), self.encriptar(dpi), self.encriptar(nombre), carrera, self.encriptar(password), creditos, self.encriptar(edad), self.encriptar(correo), self.root)
    
    # * --------------------------------------- Metodo recursivo para agregar un nuevo nodo -------------------------------------------
    def _add(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo, root):
        if root is None:
            return Node(carnet, dpi, nombre, carrera, password, creditos, edad, correo)
        else:
            if int(self.desencriptar(carnet)) < int(self.desencriptar(root.carnet)):
                root.izq = self._add(carnet, dpi, nombre, carrera, password, creditos, edad, correo, root.izq)
                if self.height(root.der) - self.height(root.izq) == -2:
                    if int(self.desencriptar(carnet)) < int(self.desencriptar(root.izq.carnet)):
                        root = self.SimpleIzq(root)
                    else:
                        root = self.dobleIzq(root)
            elif int(self.desencriptar(carnet)) > int(self.desencriptar(root.carnet)):
                root.der = self._add(carnet, dpi, nombre, carrera, password, creditos, edad, correo, root.der)
                if self.height(root.der) - self.height(root.izq) == 2:
                    if int(self.desencriptar(carnet)) > int(self.desencriptar(root.der.carnet)):
                        root = self.SimpleDer(root)
                    else:
                        root = self.dobleDer(root)
            else:
                root.carnet = carnet
        root.size = self.max_min(self.height(root.izq), self.height(root.der)) + 1
        return root

    # * ---------------------------------------- Devuelve la altura en que se encuentra el nodo ---------------------------------------
    def height(self, node):
        if node is not None:
            return node.size
        return -1

    # * --------------------------------------------- Rotacion simple por la izquierda ------------------------------------------------
    def SimpleIzq(self, node):
        aux = node.izq
        node.izq = aux.der
        aux.der = node
        node.size = self.max_min(self.height(node.der), self.height(node.izq)) + 1
        aux.size = self.max_min(self.height(aux.izq), node.size) + 1
        return aux

    # * ---------------------------------------------- Rotacion simple por la derecha -------------------------------------------------
    def SimpleDer(self, node):
        aux = node.der
        node.der = aux.izq
        aux.izq = node
        node.size = self.max_min(self.height(node.der), self.height(node.izq)) + 1
        aux.size = self.max_min(self.height(aux.der), node.size) + 1
        return aux
    
    # * --------------------------------------------- Rotacion doble por la izquierda -------------------------------------------------
    def dobleIzq(self, node):
        node.izq = self.SimpleDer(node.izq)
        return self.SimpleIzq(node)
    
    # * ---------------------------------------------- Rotacion simple por la derecha -------------------------------------------------
    def dobleDer(self, node):
        node.der = self.SimpleIzq(node.der)
        return self.SimpleDer(node)
    
    # * ---------------------------------------------- Funciones para buscar ----------------------------------------------------------

    def search(self, carnet):
        if self.root is None:
            return None
        else:
            return self._search(carnet, self.root)

    def _search(self, carnet, node):
        if node is None:
            return None

        elif int(carnet) < int(self.desencriptar(node.carnet)):
            return self._search( carnet, node.izq )

        elif int(carnet) > int(self.desencriptar(node.carnet)):
            return self._search( carnet, node.der )

        else:
            return node
    
    def validar(self, carnet, password):
        node = self.search(carnet)
        if node is None:
            return False
        else:
            if self.desencriptar(node.carnet) == carnet and self.desencriptar(node.password) == password:
                return True
            else:
                return False
    
    def getNombre(self, carnet):
        node = self.search(carnet)
        return self.desencriptar(node.nombre)

    def getMin(self):
            if self.root is None:
                return None
            else:
                return self._getMin( self.root )

    def _getMin(self, node):
        if node.izq:
            return self._getMin( node.izq )
        else:
            return node
    
    def getMax(self):
        if self.root is None:
            return None
        else:
            return self._getMax( self.root )

    def _getMax(self, node):
        if node.der:
            return self._getMax( node.der )
        else:
            return node

    # * ------------------------------------------------ Eliminar nodo del arbol ------------------------------------------------------
    def delete(self, carnet):
        self.root = self._delete(carnet, self.root)

    def _delete(self, carnet, node):
        if node is None:
            print('carnet no registrado')

        elif carnet < node.carnet:
            node.izq = self._delete(carnet, node.izq)
            if (self.height(node.der) - self.height(node.izq)) == 2:
                if self.height(node.der.der) >= self.height(node.der.izq):
                    node = self.SimpleDer(node)
                else:
                    node = self.dobleDer(node)
            node.size = self.max_min(self.height(node.izq), self.height(node.der)) + 1
            
        elif carnet > node.carnet:
            node.der = self._delete(carnet, node.der)
            if (self.height(node.izq) - self.height(node.der)) == 2:
                if self.height(node.izq.izq) >= self.height(node.izq.der):
                    node = self.SimpleIzq(node)
                else:
                    node = self.dobleIzq(node)
            node.size = self.max_min(self.height(node.izq), self.height(node.der))  +1
        
        elif node.izq and node.der:
            if node.izq.size <= node.der.size:
                minNode = self._getMin(node.der)
                node.carnet = minNode.carnet
                node.der = self._delete(node.carnet, node.der)
            else:
                maxNode = self._getdMax(node.izq)
                node.carnet = maxNode.carnet
                node.izq = self._delete(node.carnet,node.izq)
            node.size = self.max_min(self.height(node.izq), self.height(node.der)) + 1
        else:
            if node.der:
                node = node.der
            else:
                node = node.izq
        
        return node

    # * ------------------------------------------------- Recorrcarnetos del arbol --------------------------------------------------------
    def preorden(self):
        self._preorden(self.root)

    def _preorden(self, root):
        if root is not None:
            print(root.carnet)
            self._preorden(root.izq)
            self._preorden(root.der)
    
    def inorden(self):
        self._inorden(self.root)

    def _inorden(self, root):
        if root is not None:
            self._inorden(root.izq)
            print(root.carnet)
            self._inorden(root.der)

    def postorden(self):
        self._postorden(self.root)

    def _postorden(self, root):
        if root is not None:
            self._postorden(root.izq)
            self._postorden(root.der)
            print(root.carnet)

    # * ------------------------------------------------- GRAFICAR --------------------------------------------------------

    def preordenG(self):
        self._preordenG(self.root)

    def _preordenG(self, root):
        if root is not None:
            self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " [label = \""+self.txt(root.carnet) +"\" penwidth=2.5];"
            if root.izq is not None:
                self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " -> n" + self.desencriptar(root.izq.carnet) + "[tailport=sw headport=n];"
            if root.der is not None:
                self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " -> n" + self.desencriptar(root.der.carnet) + "[tailport=se headport=n];"
            self._preordenG(root.izq)
            self._preordenG(root.der)
    
    def preordenG1(self):
        self._preordenG1(self.root)

    def _preordenG1(self, root):
        if root is not None:
            self._preordenG1(root.izq)
            self.string += "\n\t\t" + self.desencriptar(root.carnet) + " [shape=plain label= \""+self.txt(root.nombre)+"\\n"+self.txt(root.dpi)+"\\n"+self.txt(root.correo)+"\\n"+self.txt(root.password)+"\"];"
            self.string += "\n\t\t{rank=same; n" + self.desencriptar(root.carnet) + "; " + self.desencriptar(root.carnet) + "}"
            self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " -> " + self.desencriptar(root.carnet) + ";"
            self._preordenG1(root.der)

    def preordenGG(self):
        self._preordenGG(self.root)

    def _preordenGG(self, root):
        if root is not None:
            self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " [label = \""+self.desencriptar(root.carnet) +"\" penwidth=2.5];"
            if root.izq is not None:
                self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " -> n" + self.desencriptar(root.izq.carnet) + "[tailport=sw headport=n];"
            if root.der is not None:
                self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " -> n" + self.desencriptar(root.der.carnet) + "[tailport=se headport=n];"
            self._preordenGG(root.izq)
            self._preordenGG(root.der)
    
    def preordenG2(self):
        self._preordenG2(self.root)

    def _preordenG2(self, root):
        if root is not None:
            self._preordenG2(root.izq)
            self.string += "\n\t\t" + self.desencriptar(root.carnet) + " [shape=plain label= \""+self.desencriptar(root.nombre)+"\\n"+self.desencriptar(root.dpi)+"\\n"+self.desencriptar(root.correo)+"\\n"+self.txt1(self.desencriptar(root.password))+"\"];"
            self.string += "\n\t\t{rank=same; n" + self.desencriptar(root.carnet) + "; " + self.desencriptar(root.carnet) + "}"
            self.string += "\n\t\tn" + self.desencriptar(root.carnet) + " -> " + self.desencriptar(root.carnet) + ";"
            self._preordenG2(root.der)

    def graficar(self):
        self.string = ""
        self.string += """  
        digraph G
        {
            node[shape=circle, style=filled, fillcolor=\"#303F9F\", fontcolor=white, color=\"#0A122A\"];
            splines=false;
        """
        self.preordenG()
        self.string += "\n\t\tedge[dir=none];"
        self.string += "\n\t\tnode[fillcolor=white, fontcolor=black];"
        self.preordenG1()
        self.string += "\n\t}"
        # print(self.string)
        self.generarArchivo()
        time.sleep(1)
        self.graficarDesencriptado()

    def graficarDesencriptado(self):
        self.string = ""
        self.string += """  
        digraph G
        {
            node[shape=circle, style=filled, fillcolor=\"#303F9F\", fontcolor=white, color=\"#0A122A\"];
            splines=false;
        """
        self.preordenGG()
        self.string += "\n\t\tedge[dir=none];"
        self.string += "\n\t\tnode[fillcolor=white, fontcolor=black];"
        self.preordenG2()
        self.string += "\n\t}"
        # print(self.string)
        self.generarArchivo2()
    
    def generarArchivo(self):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\Reportes_F3"
        path_current = "{}{}".format(os.path.abspath(os.path.dirname(__file__)), '\\')
        path_current = path_current.replace("\\Estructuras", "")+"Archivos_dot"
        pathdot = Path(path_current)
        pathdot.mkdir(parents=True, exist_ok=True)
        path = Path(path_desktop)
        path.mkdir(parents=True, exist_ok=True)
        archivo=open("Archivos_dot\\AVL.dot", 'w', encoding='utf8')
        archivo.write(self.string)
        archivo.close()
        os.system('cd Archivos_dot& dot -Tpdf AVL.dot -o '+path_desktop+'\\AVL_Encriptado.pdf')
        shutil.copy(path_desktop+'\\AVL_Encriptado.pdf', 'static\\reportes\\AVL_Encriptado.pdf')
        # os.startfile(path_desktop+"\\AVL_Encriptado.pdf")
    
    def generarArchivo2(self):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\Reportes_F3"
        path_current = "{}{}".format(os.path.abspath(os.path.dirname(__file__)), '\\')
        path_current = path_current.replace("\\Estructuras", "")+"Archivos_dot"
        pathdot = Path(path_current)
        pathdot.mkdir(parents=True, exist_ok=True)
        path = Path(path_desktop)
        path.mkdir(parents=True, exist_ok=True)
        archivo=open("Archivos_dot\\AVL.dot", 'w', encoding='utf8')
        archivo.write(self.string)
        archivo.close()
        os.system('cd Archivos_dot& dot -Tpdf AVL.dot -o '+path_desktop+'\\AVL_Desencriptado.pdf')
        shutil.copy(path_desktop+'\\AVL_Desencriptado.pdf', 'static\\reportes\\AVL_Desencriptado.pdf')
        # os.startfile(path_desktop+"\\AVL_Desencriptado.pdf")

    def txt(self, dato):
        result = dato.decode()
        return result[0:6]
# ^------------------------------------------------------- ENCRIPTACION -------------------------------------------------------------

# &_________________________________________________________ FERNAT _________________________________________________________________
    def generarClave(self, passwordMaestro):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(passwordMaestro.encode()))
        self.dt = Fernet(self.key)
    
    def encriptar(self, dato):
        datoEncriptado = self.dt.encrypt(dato.encode())
        return datoEncriptado

    def desencriptar(self, datoEncriptado):
        desencriptado = self.dt.decrypt(datoEncriptado).decode()
        return desencriptado
    
    def txt(self, dato):
        result = dato.decode()
        return result[9:15]
    
    def txt1(self, dato):
        return dato[0:9]