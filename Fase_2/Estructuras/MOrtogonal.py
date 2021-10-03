from .NodosOrtogonal import Nodo, nCabecera
from .Cabecera import listaCabeceras
from pathlib import Path
import os

class matrizOrtogonal:
    def __init__(self):
        self.CFilas = listaCabeceras()
        self.CColumnas = listaCabeceras()
        self.stringGraficar = ""
        self.auxstringGraficar = ""

    def append(self, fila, columna):
        nuevo = Nodo(fila, columna)

        CFila = self.CFilas.getCabecera(fila)
        if CFila == None:
            CFila = nCabecera(fila)
            CFila.accesoNodo = nuevo
            self.CFilas.appendCabecera(CFila)
        else:
            if nuevo.columna <  CFila.accesoNodo.columna:
                nuevo.derecha = CFila.accesoNodo
                CFila.accesoNodo.izquierda = nuevo
                CFila.accesoNodo = nuevo
            else:
                actual = CFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        CColumna = self.CColumnas.getCabecera(columna)
        if CColumna == None:
            CColumna = nCabecera(columna)
            CColumna.accesoNodo = nuevo
            self.CColumnas.appendCabecera(CColumna)
        else:
            if nuevo.fila <  CColumna.accesoNodo.fila:
                nuevo.abajo = CColumna.accesoNodo
                CColumna.accesoNodo.arriba = nuevo
                CColumna.accesoNodo = nuevo
            else:
                actual = CColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def recorrerFilas(self):
        CFila = self.CFilas.primero
        while CFila != None:
            actual = CFila.accesoNodo
            print("\nFila"+str(actual.fila))
            print("Columna   dato")
            while actual != None:
                print(str(actual.columna)+"         "+str(actual.listaTareas.tamanio))
                actual = actual.derecha
            CFila = CFila.siguiente
    
    def getLista(self, ff, cc):
        CFila = self.CFilas.primero
        while CFila != None:
            actual = CFila.accesoNodo
            f=actual.fila
            while actual != None:
                c=actual.columna
                if c==cc and f==ff: 
                    return actual.listaTareas
                actual = actual.derecha
            CFila = CFila.siguiente
        return False
    
    def verificarExiste(self, ff, cc):
        encontrado=False
        CFila = self.CFilas.primero
        while CFila != None:
            actual = CFila.accesoNodo
            f=actual.fila
            while actual != None:
                c=actual.columna
                if c==cc and f==ff: 
                    encontrado=True
                actual = actual.derecha
            CFila = CFila.siguiente
        return encontrado
    
    def mensaje(self):
        print("hola")
    
    def search(self, ff, cc):
        CFila = self.CFilas.primero
        while CFila != None:
            actual = CFila.accesoNodo
            f=actual.fila
            while actual != None:
                c=actual.columna
                if c==cc and f==ff: 
                    return actual
                actual = actual.derecha
            CFila = CFila.siguiente
        return False
    
    def delete(self, ff, cc):
        nodoEliminar = self.search(ff,cc)
        if nodoEliminar != False:
            # *0BTENER APUTNADORES
            arriba = nodoEliminar.arriba
            abajo = nodoEliminar.abajo
            derecha = nodoEliminar.derecha
            izquierda = nodoEliminar.izquierda
            print(arriba)
            print(abajo)
            print(derecha)
            print(izquierda)
            # ! CASO 1 (nodo unico):
            if arriba is None and abajo is None and derecha is None and izquierda is None:
                self.eliminarCabeceraFila(ff)
                self.eliminarCabeceraColumna(cc)
            
            # ! CASO 2:
            elif arriba is None and abajo is None and derecha is None and izquierda is not None:
                self.eliminarCabeceraColumna(cc)
                izquierda.derecha = None
                nodoEliminar.izquierda = None
            
            # ! CASO 3:
            elif arriba is None and abajo is None and derecha is not None and izquierda is None:
                self.eliminarCabeceraColumna(cc)
                CFila = self.CFilas.getCabecera(ff)
                CFila.accesoNodo = derecha
                derecha.izquierda = None
                nodoEliminar.derecha = None
            
            # ! CASO 4:
            elif arriba is None and abajo is None and derecha is not None and izquierda is not None:
                self.eliminarCabeceraColumna(cc)
                izquierda.derecha = derecha
                derecha.izquierda = izquierda
                nodoEliminar.izquierda = None
                nodoEliminar.derecha = None
            
            # ! CASO 5:
            elif arriba is None and abajo is not None and derecha is None and izquierda is None:
                self.eliminarCabeceraFila(ff)
                CColumna = self.CColumnas.getCabecera(cc)
                CColumna.accesoNodo = abajo
                abajo.arriba = None
                nodoEliminar.abajo = None
            
            # ! CASO 6:
            elif arriba is None and abajo is not None and derecha is None and izquierda is not None:
                CColumna = self.CColumnas.getCabecera(cc)
                CColumna.accesoNodo = abajo
                abajo.arriba = None
                izquierda.derecha = None
                nodoEliminar.izquierda = None
            
            # ! CASO 7:
            elif arriba is None and abajo is not None and derecha is not None and izquierda is None:
                CColumna = self.CColumnas.getCabecera(cc)
                CFila = self.CFilas.getCabecera(ff)
                CColumna.accesoNodo = abajo
                CFila.accesoNodo = derecha
                derecha.izquierda = None
                abajo.arriba = None
                nodoEliminar.abajo = None
                nodoEliminar.derecha = None
            
            # ! CASO 8:
            elif arriba is None and abajo is not None and derecha is not None and izquierda is not None:
                CColumna = self.CColumnas.getCabecera(cc)
                CColumna.accesoNodo = abajo
                derecha.izquierda = izquierda
                izquierda.derecha = derecha
                abajo.arriba = None
                nodoEliminar.abajo = None
                nodoEliminar.derecha = None
                nodoEliminar.izquierda = None
            
            # ! CASO 9:
            elif arriba is not None and abajo is None and derecha is None and izquierda is None:
                self.eliminarCabeceraFila(ff)
                arriba.abajo = None
                nodoEliminar.arriba = None
            
            # ! CASO 10:
            elif arriba is not None and abajo is None and derecha is None and izquierda is not None:
                arriba.abajo = None
                izquierda.derecha = None
                nodoEliminar.arriba = None
                nodoEliminar.izquierda = None
            
            # ! CASO 11:
            elif arriba is not None and abajo is None and derecha is not None and izquierda is None:
                CFila = self.CFilas.getCabecera(ff)
                CFila.accesoNodo = derecha
                arriba.abajo = None
                derecha.izquierda = None
                nodoEliminar.arriba = None
                nodoEliminar.derecha = None
            
            # ! CASO 12:
            elif arriba is not None and abajo is None and derecha is not None and izquierda is not None:
                arriba.abajo = None
                derecha.izquierda = izquierda
                izquierda.derecha = derecha
                nodoEliminar.derecha = None
                nodoEliminar.izquierda = None
                nodoEliminar.arriba = None
            
            # ! CASO 13:
            elif arriba is not None and abajo is not None and derecha is None and izquierda is None:
                self.eliminarCabeceraFila(ff)
                arriba.abajo = abajo
                abajo.arriba = arriba
                nodoEliminar.arriba = None
                nodoEliminar.abajo = None
            
            # ! CASO 14:
            elif arriba is not None and abajo is not None and derecha is None and izquierda is not None:
                arriba.abajo = abajo
                abajo.arriba = arriba
                izquierda.derecha = None
                nodoEliminar.izquierda = None
                nodoEliminar.arriba = None
                nodoEliminar.abajo = None
            
            # ! CASO 15:
            elif arriba is not None and abajo is not None and derecha is not None and izquierda is None:
                CFila = self.CFilas.getCabecera(ff)
                CFila.accesoNodo = derecha
                derecha.izquierda = None
                arriba.abajo = abajo
                abajo.arriba = arriba
                nodoEliminar.arriba = None
                nodoEliminar.abajo = None
                nodoEliminar.derecha = None
            
            # ! CASO 16:
            elif arriba is not None and abajo is not None and derecha is not None and izquierda is not None:
                arriba.abajo = abajo
                abajo.arriba = arriba
                derecha.izquierda = izquierda
                izquierda.derecha = derecha
                nodoEliminar.arriba = None
                nodoEliminar.abajo = None
                nodoEliminar.derecha = None
                nodoEliminar.izquierda =None


    def eliminarCabeceraFila(self, ff):
        CFila = self.CFilas.getCabecera(ff)
        dererecha = CFila.siguiente
        izquierda = CFila.anterior
        if izquierda is None and dererecha is not None:
            self.CFilas.setPrimero(dererecha)
        elif izquierda is not None and dererecha is None:
            izquierda.siguiente = None
        else:
            izquierda.siguiente = dererecha
            dererecha.anterior = izquierda
            CFila.siguiente = None
            CFila.anterior = None
    
    def eliminarCabeceraColumna(self, cc):
        CFila = self.CColumnas.getCabecera(cc)
        dererecha = CFila.siguiente
        izquierda = CFila.anterior
        if izquierda is None and dererecha is not None:
            self.CFilas.setPrimero(dererecha)
        elif izquierda is not None and dererecha is None:
            izquierda.siguiente = None
        else:
            izquierda.siguiente = dererecha
            dererecha.anterior = izquierda
            CFila.siguiente = None
            CFila.anterior = None

    def recorrerColumnas(self):
        CColumna = self.CColumnas.primero
        while CColumna != None:
            actual = CColumna.accesoNodo
            print("\nColumna"+str(actual.columna))
            print("Fila   dato")
            while actual != None:
                # print(str(actual.fila)+"      "+actual.dato)
                actual = actual.abajo
            CColumna = CColumna.siguiente

    def getDataFilas(self):
        CFila = self.CFilas.primero
        idFila = ""
        conectarIdFilas=""
        nodosInteriores = ""
        direccionInteriores = ""
        while CFila != None:
            Primero=True    
            actual = CFila.accesoNodo
            idFila+= "\n\t\tF"+str(actual.fila)+" [label = \""+str(actual.fila)+"\"   width = 1 style = filled, fillcolor = \"#00d2d3\", color=\"#01a3a4\" penwidth=2.5 group = 1 ];"
            if CFila.siguiente is not None:
                conectarIdFilas += "\n\t\tF"+str(actual.fila)+" -> F"+str(CFila.siguiente.accesoNodo.fila)+";"
                # conectarIdFilas += "\n\t\tF"+str(CFila.siguiente.accesoNodo.fila)+" -> F"+str(actual.fila)+";"
            direccionInteriores += "\n\t\t{ rank = same; F"+str(actual.fila)+"; "
            while actual != None:
                nodosInteriores += "\n\t\tN"+str(actual.fila)+"_L"+str(actual.columna)+" [label = \""+str(actual.listaTareas.tamanio)+"\" width = 1, style=\"filled, rounded\" fillcolor=\"#c8d6e5\" color=\"#222f3e\" penwidth=2 group = "+str(actual.columna)+" ];"
                direccionInteriores += "N"+str(actual.fila)+"_L"+str(actual.columna)+"; "
                # print(str(actual.columna)+"         "+actual.dato)
                if Primero:
                    nodosInteriores += "\n\t\tF"+str(actual.fila)+" -> N"+str(actual.fila)+"_L"+str(actual.columna)+";"
                    if actual.derecha is not None:
                        nodosInteriores += "\n\t\tN"+str(actual.fila)+"_L"+str(actual.columna)+ "-> N"+str(actual.derecha.fila)+"_L"+str(actual.derecha.columna)+";"
                        nodosInteriores += "\n\t\tN"+str(actual.derecha.fila)+"_L"+str(actual.derecha.columna)+ "-> N"+str(actual.fila)+"_L"+str(actual.columna)+";"
                    Primero=False
                else:
                    if actual.derecha is not None:
                        nodosInteriores += "\n\t\tN"+str(actual.fila)+"_L"+str(actual.columna)+ "-> N"+str(actual.derecha.fila)+"_L"+str(actual.derecha.columna)+";"
                        nodosInteriores += "\n\t\tN"+str(actual.derecha.fila)+"_L"+str(actual.derecha.columna)+ "-> N"+str(actual.fila)+"_L"+str(actual.columna)+";"
                actual = actual.derecha
            CFila = CFila.siguiente
            direccionInteriores += "}"
        self.stringGraficar+=idFila
        self.stringGraficar += "\n\t\tedge[dir=\"both\"];"
        self.stringGraficar+=conectarIdFilas
        self.stringGraficar += "\n\t\tedge[dir=\"forward\"];"
        self.getDataColumnas()
        self.stringGraficar+=nodosInteriores
        self.stringGraficar+=direccionInteriores

    def getDataColumnas(self):
        CColumna = self.CColumnas.primero
        primeroC = self.CColumnas.primero.accesoNodo.columna
        primeroF = self.CFilas.primero.accesoNodo.fila
        idColumna = ""
        conectarIdColumnas = ""
        direccion = "\n\t\t{ rank = same; Head;"
        while CColumna != None:
            primero = True
            actual = CColumna.accesoNodo
            idColumna += "\n\t\tC"+str(actual.columna)+" [label = \""+str(actual.columna)+"\"   width = 1 style = filled, fillcolor = \"#00d2d3\", color=\"#01a3a4\" penwidth=2.5 group = "+str(actual.columna)+" ];"
            direccion += "C"+str(actual.columna)+"; "
            if CColumna.siguiente is not None:
                conectarIdColumnas += "\n\t\tC"+str(actual.columna)+" -> C"+str(CColumna.siguiente.accesoNodo.columna)+";"
                conectarIdColumnas += "\n\t\tC"+str(CColumna.siguiente.accesoNodo.columna)+" -> C"+str(actual.columna)+";"
            while actual != None:
                # print(str(actual.fila)+"      "+actual.dato)
                if primero:
                    self.auxstringGraficar+= "\n\t\tC"+str(actual.columna)+" -> N"+str(actual.fila)+"_L"+str(actual.columna)+";"
                    if actual.abajo is not None:
                        self.auxstringGraficar += "\n\t\tN"+str(actual.fila)+"_L"+str(actual.columna)+ "-> N"+str(actual.abajo.fila)+"_L"+str(actual.abajo.columna)+";"
                        self.auxstringGraficar += "\n\t\tN"+str(actual.abajo.fila)+"_L"+str(actual.abajo.columna)+ "-> N"+str(actual.fila)+"_L"+str(actual.columna)+";"
                    primero=False
                else:
                    if actual.abajo is not None:
                        self.auxstringGraficar += "\n\t\tN"+str(actual.fila)+"_L"+str(actual.columna)+ "-> N"+str(actual.abajo.fila)+"_L"+str(actual.abajo.columna)+";"
                        self.auxstringGraficar += "\n\t\tN"+str(actual.abajo.fila)+"_L"+str(actual.abajo.columna)+ "-> N"+str(actual.fila)+"_L"+str(actual.columna)+";"
                actual = actual.abajo
            CColumna = CColumna.siguiente
        self.stringGraficar+=idColumna
        self.stringGraficar+=conectarIdColumnas
        self.stringGraficar+="\n\t\tHead -> F"+str(primeroF)+"; \n\t\tHead -> C"+str(primeroC)+";"
        self.stringGraficar+=direccion+"}"

    def graficar(self,mes):
        self.auxstringGraficar=""
        self.stringGraficar = """
        digraph G {
        label=\"\\n"""+mes
        self.stringGraficar +="""\" fontsize=28;
        node [shape=box, height=0.8];
        Head[ label = "Matriz", width = 1, style = "filled, rounded" fillcolor = "#ff6b6b", color="#c23616" group = 1 penwidth=2.5];
        """
        self.getDataFilas()
        self.stringGraficar+=self.auxstringGraficar
        self.stringGraficar+="\n}"
        self.generarArchivo()
    
    # def generarAchivo(self):
    #     archivo=open("Archivos_dot\\Dispersa.dot", 'w', encoding='utf8')
    #     archivo.write(self.stringGraficar)
    #     archivo.close()
    
    def generarArchivo(self):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\Reportes_F2"
        path_current = "{}{}".format(os.path.abspath(os.path.dirname(__file__)), '\\')
        path_current = path_current.replace("\\Estructuras", "")+"Archivos_dot"
        pathdot = Path(path_current)
        pathdot.mkdir(parents=True, exist_ok=True)
        path = Path(path_desktop)
        path.mkdir(parents=True, exist_ok=True)
        archivo=open("Archivos_dot\\Dispersa.dot", 'w', encoding='utf8')
        archivo.write(self.stringGraficar)
        archivo.close()
        os.system('cd Archivos_dot& dot -Tpdf Dispersa.dot -o '+path_desktop+'\\Dispersa.pdf')
        os.startfile(path_desktop+"\\Dispersa.pdf")

# n = matrizOrtogonal()
# n.append(7, 2, "5")
# n.append(7, 8, "1")
# n.append(7, 15, "14")
# n.append(10, 2, "1")
# n.append(10, 5, "3")
# n.append(15, 15, "5")
# n.recorrerFilas()