class Node:
    def __init__ (self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.siguiente = None
        self.anterior = None

class List:
    def __init__ (self):
        self.cabeza = None
        self.cola = None
        self.controlList = []

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
        auxList = []
        while aux is not None:
            auxList.append(Node(aux.codigo, aux.nombre,  aux.creditos))
            aux = aux.siguiente
        return auxList

    def insert(self, codigo, nombre, creditos):
        newNode = Node (codigo, nombre, creditos)

        if self.isEmpy():
            self.cola = newNode
            self.cabeza = self.cola
        else:
            self.cola.siguiente = newNode
            newNode.anterior = self.cola
            self.cola = newNode