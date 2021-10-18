class Node:
    def __init__(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return str(self.codigo)+str("\n")

class DoubleList:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
    
    def isEmpty(self):
        if self.cabeza == None and self.cola == None:
            return True
        else:
            return False

    def append(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        newNode = Node(codigo, nombre, creditos, prerequisitos, obligatorio)
        if self.size < 4:
            if self.isEmpty():
                self.cabeza = self.cola = newNode
            else:
                newNode.anterior = self.cola
                self.cola.siguiente = newNode
                self.cola = newNode
            self.size += 1
        else:
            print("ERROR, tamanio excedido")

    def appendDato(self, codigo, posicion):
        nodeAux = self.cabeza
        while posicion != 0 :
            posicion -= 1
            nodeAux = nodeAux.siguiente
        nodeAux.codigo = codigo

    def get(self, posicion):
        nodeAux = self.cabeza
        while posicion != 0 :
            posicion -= 1
            nodeAux = nodeAux.siguiente
        return nodeAux

    def __str__(self):
        string = ""
        nodeAux = self.cabeza
        while nodeAux != None:
            string += str(nodeAux)
            nodeAux = nodeAux.siguiente
        return string