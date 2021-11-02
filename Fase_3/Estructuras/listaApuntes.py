class Nodo:
    def __init__(self, id, titulo, contenido):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.siguiente = None
    
    def __str__(self):
        return str(self.titulo)+str("\n")

class notesList:
    def __init__(self):
        self.cabeza = self.cola = None
        self.tamanio = 0
    
    def isEmpy(self):
        if self.cabeza == None and self.cola ==None:
            return True
        else:
            return False
            
    def append(self, titulo, contenido):
        newNode = Nodo(self.tamanio +1, titulo, contenido)
        if self.isEmpy():
            self.cabeza = self.cola = newNode
            self.tamanio += 1
        else:
            self.cola.siguiente = newNode
            self.cola = newNode
            self.tamanio += 1
    
    def get(self, id):
        nodeAux = self.cabeza
        while nodeAux != None:
            if nodeAux.id == id:
                return nodeAux
            nodeAux = nodeAux.siguiente
    
    def iterar(self):
        nodeAux = self.cabeza
        while nodeAux != None:
            yield nodeAux
            nodeAux = nodeAux.siguiente

    def __str__(self):
        string = ""
        nodeAux = self.cabeza
        while nodeAux != None:
            string += str(nodeAux)
            nodeAux = nodeAux.siguiente
        return string