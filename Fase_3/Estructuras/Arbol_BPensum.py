from Estructuras.DobleBPensum import DoubleList
from Estructuras.ListaPuntero import ListaPuntero
from pathlib import Path
import os
import shutil

class PaginaB:
    def __init__(self):
        self.size = 0
        self.maxClaves = 0
        self.punteros = ListaPuntero()
        self.datos = DoubleList()
        self.inicializar()
        self.string = ""
        self.cont = 0

    def inicializar(self):
        for i in range(5):
            if i != 4:
                self.datos.append("", None, None, None, None)
            self.punteros.appendPuntero(None)
        self.maxClaves = 5

    def paginaLlena(self):
        return (self.size == self.maxClaves-1)
    
    def paginaCasiLlena(self):
        return (self.size == self.maxClaves/2)
    
    def getCodigo(self, posicion):
        return self.datos.get(posicion).codigo
    
    def setCodigo(self, posicion, codigo):
        self.datos.appendDato(codigo, posicion)
    
    def getNombre(self, posicion):
        return self.datos.get(posicion).nombre
    
    def setNombre(self, posicion, nombre):
        self.datos.get(posicion).nombre = nombre
    
    def getCreditos(self, posicion):
        return self.datos.get(posicion).creditos
    
    def setCreditos(self, posicion, creditos):
        self.datos.get(posicion).creditos = creditos
    
    def getPrerequisitos(self, posicion):
        return self.datos.get(posicion).prerequisitos
    
    def setPrerequisitos(self, posicion, prerequisitos):
        self.datos.get(posicion).prerequisitos = prerequisitos
    
    def getObligatorio(self, posicion):
        return self.datos.get(posicion).obligatorio
    
    def setObligatorio(self, posicion, obligatorio):
        self.datos.get(posicion).obligatorio = obligatorio

    def getApuntador(self, posicion):
        return self.punteros.get(posicion).puntero
    
    def setApuntador(self, posicion, puntero):
        self.punteros.appendPunteroPagina(puntero, posicion)

class ArbolB:
    def __init__(self):
        self.raiz = None
        self.codigo = None
        self.nombre = None
        self.creditos = None
        self.prerequisitos = None
        self.obligatorio = None
        self.aux1 = False
        self.aux2 = None
        self.subeArriba = False
        self.estado = False
        self.comparador = False

    def isEmpy(self, raiz):
        return (raiz == None or raiz.size == 0)
    
    def appendDatos(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        self._appendDatos(self.raiz, codigo, nombre, creditos, prerequisitos, obligatorio)
    
    def _appendDatos(self, raiz, codigo, nombre, creditos, prerequisitos, obligatorio):
        self.empujar(raiz, codigo, nombre, creditos, prerequisitos, obligatorio)
        if self.subeArriba:
            self.raiz = PaginaB()
            self.raiz.size = 1
            self.raiz.setCodigo(0, self.codigo)
            self.raiz.setNombre(0, self.nombre)
            self.raiz.setCreditos(0, self.creditos)
            self.raiz.setPrerequisitos(0, self.prerequisitos)
            self.raiz.setObligatorio(0, self.obligatorio)

            self.raiz.setApuntador(0, raiz)
            self.raiz.setApuntador(1, self.aux2)
    
    def empujar(self, raiz, codigo, nombre, creditos, prerequisitos, obligatorio):
        pos = 0
        self.estado = False

        if self.isEmpy(raiz) and self.comparador == False:
            self.subeArriba = True

            self.codigo = codigo
            self.nombre = nombre
            self.creditos = creditos
            self.prerequisitos = prerequisitos
            self.obligatorio = obligatorio
            self.aux2 = None
        
        else:
            pos = self.buscarNodoB(codigo, raiz)
            if self.comparador == False:
                if self.estado:
                    self.subeArriba = False
                else:
                    self.empujar(raiz.getApuntador(pos), codigo, nombre, creditos, prerequisitos, obligatorio)

                    if self.subeArriba:
                        if raiz.size < 4:
                            self.subeArriba = False
                            self.MeterHoja(raiz, pos, self.codigo, self.nombre, self.creditos, self.prerequisitos, self.obligatorio)
                        
                        else:
                            self.subeArriba=True
                            self.DividirPaginaB(raiz, pos, self.codigo, self.nombre, self.creditos, self.prerequisitos, self.obligatorio)
            else:
                print("Dato Repetido")
                self.comparador = False
    
    def buscarNodoB(self, codigo, raiz):
        cont = 0
        if self.compareTo(codigo, raiz.getCodigo(0)) < 0 :
            self.estado = False
            cont = 0
        else:
            while cont != raiz.size:
                if codigo == raiz.getCodigo(cont):
                    self.comparador = True
                cont += 1
            cont = raiz.size
        
            while self.compareTo(codigo, raiz.getCodigo(cont-1)) < 0 and cont > 1:
                cont -= 1
                estado = True if codigo == raiz.getCodigo(cont-1) else False
        return cont

    def MeterHoja(self, raiz, posicion, codigo, nombre, creditos, prerequisitos, obligatorio):
        aux = raiz.size

        while aux != posicion:
            if aux != 0:
                raiz.setCodigo(aux, raiz.getCodigo(aux-1))
                raiz.setNombre(aux, raiz.getNombre(aux-1))
                raiz.setCreditos(aux, raiz.getCreditos(aux-1))
                raiz.setPrerequisitos(aux, raiz.getPrerequisitos(aux-1))
                raiz.setObligatorio(aux, raiz.getObligatorio(aux-1))
                raiz.setApuntador(aux+1, raiz.getApuntador(aux))
            
            aux -= 1
        
        raiz.setCodigo(posicion, codigo)
        raiz.setNombre(posicion, nombre)
        raiz.setCreditos(posicion, creditos)
        raiz.setPrerequisitos(posicion, prerequisitos)
        raiz.setObligatorio(posicion, obligatorio)
        raiz.setApuntador(posicion+1, self.aux2)
        raiz.size = raiz.size + 1
        
    def DividirPaginaB(self, raiz, posicion, codigo, nombre, creditos, prerequisitos, obligatorio):
        posicion2 = 0
        posicionMedia = 0

        if posicion <= 2:
            posicionMedia = 2
        else:
            posicionMedia = 3
        
        paginaDerecha = PaginaB()
        posicion2 = posicionMedia + 1

        while posicion2 != 5:
            if (posicion2-posicionMedia) != 0:
                paginaDerecha.setCodigo((posicion2-posicionMedia)-1, raiz.getCodigo(posicion2-1))
                paginaDerecha.setNombre((posicion2-posicionMedia)-1, raiz.getNombre(posicion2-1))
                paginaDerecha.setCreditos((posicion2-posicionMedia)-1, raiz.getCreditos(posicion2-1))
                paginaDerecha.setPrerequisitos((posicion2-posicionMedia)-1, raiz.getPrerequisitos(posicion2-1))
                paginaDerecha.setObligatorio((posicion2-posicionMedia)-1, raiz.getObligatorio(posicion2-1))
                paginaDerecha.setApuntador(posicion2-posicionMedia, raiz.getApuntador(posicion2))
            posicion2 += 1

        paginaDerecha.size = (4-posicionMedia)
        raiz.size = posicionMedia

        if posicion <=2:
            self.aux1 = True
            self.MeterHoja(raiz, posicion, codigo, nombre, creditos, prerequisitos, obligatorio)
        else:
            self.aux1 = True
            self.MeterHoja(paginaDerecha, (posicion-posicionMedia), codigo, nombre, creditos, prerequisitos, obligatorio)

        self.codigo = raiz.getCodigo(raiz.size-1)
        self.nombre = raiz.getNombre(raiz.size-1)
        self.creditos = raiz.getCreditos(raiz.size-1)
        self.prerequisitos = raiz.getPrerequisitos(raiz.size-1)
        self.obligatorio = raiz.getObligatorio(raiz.size-1)
        paginaDerecha.setApuntador(0, raiz.getApuntador(raiz.size))

        raiz.size = raiz.size-1
        self.aux2 = paginaDerecha

        if self.aux1:
            raiz.setCodigo(3, "")
            raiz.setNombre(3, "")
            raiz.setCreditos(3, 0)
            raiz.setPrerequisitos(3, "")
            raiz.setObligatorio(3, "")
            raiz.setApuntador(4, None)

            raiz.setCodigo(2, "")
            raiz.setNombre(2, "")
            raiz.setCreditos(2, 0)
            raiz.setPrerequisitos(2, "")
            raiz.setObligatorio(2, "")
            raiz.setApuntador(3, None)
    
    def preorden(self):
        self._preorden(self.raiz)
    
    def _preorden(self, pagina):
        if pagina is not None:
            for i in range(pagina.size):
                if pagina.getCodigo(i) is not None:
                    if pagina.getCodigo(i) != "":
                        print(pagina.getCodigo(i)+"_", end="")
            
            print("")

            self._preorden(pagina.getApuntador(0))
            self._preorden(pagina.getApuntador(1))
            self._preorden(pagina.getApuntador(2))
            self._preorden(pagina.getApuntador(3))
            self._preorden(pagina.getApuntador(4))
    
    def iterar(self):
        self.data = ""
        self._iterar(self.raiz)
        return self.data
    
    def _iterar(self, pagina):
        if pagina is not None:
            for i in range(pagina.size):
                if pagina.getCodigo(i) is not None:
                    if pagina.getCodigo(i) != "":
                        self.data += pagina.getCodigo(i)+"-"+pagina.getNombre(i)+"#"

            self._iterar(pagina.getApuntador(0))
            self._iterar(pagina.getApuntador(1))
            self._iterar(pagina.getApuntador(2))
            self._iterar(pagina.getApuntador(3))
            self._iterar(pagina.getApuntador(4))
    
    def getData(self):
        self.info = ""
        self._getData(self.raiz)
        return self.info
    
    def _getData(self, pagina):
        if pagina is not None:
            for i in range(pagina.size):
                if pagina.getCodigo(i) is not None:
                    if pagina.getCodigo(i) != "":
                        self.info += pagina.getCodigo(i)+"-"+pagina.getNombre(i)+"-"+str(pagina.getCreditos(i))+"-"+pagina.getPrerequisitos(i)+"#"

            self._getData(pagina.getApuntador(0))
            self._getData(pagina.getApuntador(1))
            self._getData(pagina.getApuntador(2))
            self._getData(pagina.getApuntador(3))
            self._getData(pagina.getApuntador(4))

    def compareTo(self, a, b):
        if int(a) > int(b):
            return 1
        elif int(a) < int(b):
            return -1
        elif  int(a) == int(b):
            return 0
    
    def graficar(self, title, color, background):
        self.cont = 0
        self.string = """ 
        digraph BTree
        {
        label="\\n"""+title+"""" fontsize=25;
        rankdir=TB;
        node[color=" """+color+"""",style="filled, rounded", fillcolor=" """+background+"""", shape=record penwidth=2, fontcolor=" """+color+""""];
        edge[color=" """+color+"""" penwidth=1.3 arrowhead=vee];
        splines=false;
        """
        self._graficar(self.raiz)
        self.__graficar(self.raiz)
        self.string += "\n\t}"
        # print(self.string)
        self.generarArchivo()


    
    def _graficar(self, pagina):
        aux = 0
        if pagina is not None:
            self.cont = 0
            for i in range(pagina.size):
                if pagina.getCodigo(i) != None:
                    if pagina.getCodigo(i) != "":
                        self.cont += 1
                        if i != 0:
                            self.string += " | "

                        if self.cont == 1:
                            self.string += "\n\t\tNodo"+pagina.getCodigo(i)+"[label=\"<f0> | "

                        if i == 0:
                            self.string += "<f"+str(i+1)+">"+pagina.getCodigo(i)+"\\n"+pagina.getNombre(i)+" | <f"+str(i+2)+"> "
                            aux = 3
                        else:
                            self.string += "<f"+str(aux)+">"+pagina.getCodigo(i)+"\\n"+pagina.getNombre(i)+" | <f"+str(aux+1)+"> "
                            aux +=2

                        if i == (pagina.size - 1):
                            aux = 0
                            self.string += " \", group=0];"
            
            self._graficar(pagina.getApuntador(0))
            self._graficar(pagina.getApuntador(1))
            self._graficar(pagina.getApuntador(2))
            self._graficar(pagina.getApuntador(3))
            self._graficar(pagina.getApuntador(4))
    
    def __graficar(self, pagina):
        if pagina is not None:
            if pagina.getCodigo(0) is not None:
                if pagina.getCodigo(0) != "":
                    if pagina.getApuntador(0) is not None:
                        self.string += "\n\t\tNodo"+pagina.getCodigo(0)+":f0->"+"Nodo"+pagina.getApuntador(0).getCodigo(0)
                    
                    if pagina.getApuntador(1) is not None:
                        self.string += "\n\t\tNodo"+pagina.getCodigo(0)+":f2->"+"Nodo"+pagina.getApuntador(1).getCodigo(0)
                    
                    if pagina.getApuntador(2) is not None:
                        self.string += "\n\t\tNodo"+pagina.getCodigo(0)+":f4->"+"Nodo"+pagina.getApuntador(2).getCodigo(0)

                    if pagina.getApuntador(3) is not None:
                        self.string += "\n\t\tNodo"+pagina.getCodigo(0)+":f6->"+"Nodo"+pagina.getApuntador(3).getCodigo(0)

                    if pagina.getApuntador(4) is not None:
                        self.string += "\n\t\tNodo"+pagina.getCodigo(0)+":f8->"+"Nodo"+pagina.getApuntador(4).getCodigo(0)

            self.__graficar(pagina.getApuntador(0))
            self.__graficar(pagina.getApuntador(1))
            self.__graficar(pagina.getApuntador(2))
            self.__graficar(pagina.getApuntador(3))
            self.__graficar(pagina.getApuntador(4))
    
    def generarArchivo(self):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\Reportes_F2"
        path_current = "{}{}".format(os.path.abspath(os.path.dirname(__file__)), '\\')
        path_current = path_current.replace("\\Estructuras", "")+"Archivos_dot"
        pathdot = Path(path_current)
        pathdot.mkdir(parents=True, exist_ok=True)
        path = Path(path_desktop)
        path.mkdir(parents=True, exist_ok=True)
        archivo=open("Archivos_dot\\CursosPensum.dot", 'w', encoding='utf8')
        archivo.write(self.string)
        archivo.close()
        os.system('cd Archivos_dot& dot -Tpdf CursosPensum.dot -o '+path_desktop+'\\CursosPensum.pdf')
        shutil.copy(path_desktop+'\\CursosPensum.pdf', 'static\\reportes\\CursosPensum.pdf')
        # os.startfile(path_desktop+"\\CursosPensum.pdf")


# a = ArbolB()
# a.appendDatos("100", "Matematica basica 1", 7, "", "true")
# a.appendDatos("080", "Matematica basica 2", 8, "", "false")
# a.appendDatos("060", "Matematica basica 3", 9, "", "true")
# a.appendDatos("075", "Matematica basica 4", 10, "", "true")
# a.appendDatos("020", "Matematica basica 5", 11, "", "false")
# a.appendDatos("065", "Matematica basica 6", 12, "", "true")
# a.appendDatos("140", "Matematica basica 7", 13, "", "false")
# a.appendDatos("150", "Matematica basica 8", 15, "", "true")
# a.appendDatos("160", "Matematica basica 9", 16, "", "false")
# a.appendDatos("170", "Matematica basica 10", 17, "", "true")
# a.appendDatos("180", "Matematica basica 11", 18, "", "false")
# a.appendDatos("190", "Matematica basica 12", 19, "", "true")
# a.appendDatos("200", "Matematica basica 13", 20, "", "false")
# # a.preorden()
# a.graficar()