from Estructuras.Arbol_BPensum import ArbolB

class Nodo:
    def __init__(self, semestre):
        self.semestre = semestre
        self.cursos = ArbolB()
        self.siguiente = None
    
    def __str__(self):
        return str(self.semestre)

class Lista_Simple:
    def __init__(self):
        self.cabeza = self.cola = None
        self.tamanio = 0
    
    def isEmpy(self):
        if self.cabeza == None and self.cola ==None:
            return True
        else:
            return False
            
    def append(self, semestre):
        newNode = Nodo(semestre)
        if self.isEmpy():
            self.cabeza = self.cola = newNode
            self.tamanio += 1
        else:
            self.cola.siguiente = newNode
            self.cola = newNode
            self.tamanio += 1
    
    def search(self, semestre):
        if self.isEmpy() == False:
            nodeAux = self.cabeza
            encontrado = False
            while nodeAux != None:
                if nodeAux.semestre == semestre:
                    encontrado = True
                nodeAux = nodeAux.siguiente
            return encontrado
        else:
            return False
    

    def getCursosSemestre(self, semestre):
        nodeAux = self.cabeza
        while nodeAux != None:
            if nodeAux.semestre == semestre:
                return nodeAux.cursos
            nodeAux = nodeAux.siguiente
        return None

    def __str__(self):
        string = ""
        nodeAux = self.cabeza
        while nodeAux != None:
            string += str(nodeAux)
            nodeAux = nodeAux.siguiente
        return string