class Node:
    def __init__(self, dato, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior
    
    def __str__(self):
        return str(self.dato)+str("\n")

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
    
    def prepend(self, dato):
        newNode = Node(dato)
        if self.isEmpty():
            self.cabeza = self.cola = newNode
        else:
            self.cabeza.anterior = newNode
            newNode.siguiente = self.cabeza
            self.cabeza = newNode
        self.size += 1

    def append(self, dato):
        newNode = Node(dato)
        if self.isEmpty():
            self.cabeza = self.cola = newNode
        else:
            newNode.anterior = self.cola
            self.cola.siguiente = newNode
            self.cola = newNode
        self.size += 1

    def shift(self):
        if self.size == 1:
            self.cabeza = self.cola = None
            self.size = 0
            # print("Esta vacio")
        # elif self.isEmpty():
        #     print("Esta vacio")
        else:
            nodeAux = self.cabeza
            self.cabeza = nodeAux.siguiente
            nodeAux.siguiente = None
            self.size-=1
    
    def pop(self):
        if self.size == 1:
            self.cabeza = self.cola = None
            self.size -= 1
        #     print("Esta vacio")
        # elif self.isEmpty():
        #     print("Esta vacio")
        else:
            nodeAux = self.cola.anterior
            self.cola = nodeAux
            self.cola.siguiente = None
            self.size-=1

    def get(self, id):
        nodeAux = self.cabeza
        while nodeAux != None:
            if nodeAux.dato == id:
                return nodeAux
            nodeAux = nodeAux.siguiente

    def delete(self, id):
        nodeAux = self.cabeza
        while nodeAux != None:
            if nodeAux.dato == id:
                if nodeAux == self.cabeza:
                    self.shift()
                    break
                elif nodeAux == self.cola:
                    self.pop()
                    break
                else:
                    nodeAux.anterior.siguiente = nodeAux.siguiente
                    nodeAux.siguiente.anterior = nodeAux.anterior
                    nodeAux.siguiente = None
                    nodeAux.anterior = None
                    break
            nodeAux = nodeAux.siguiente
    
    def update(self, id, dato):
        nodeAux = self.get(id)
        nodeAux.dato=dato

    # TODO: realizar el metodo de insertar

    def __str__(self):
        string = ""
        nodeAux = self.cabeza
        while nodeAux != None:
            string += str(nodeAux)
            nodeAux = nodeAux.siguiente
        return string

prueba = DoubleList()
prueba.append(1)
prueba.append(2)
prueba.append(3)
prueba.append(4)
prueba.append(5)
print(prueba)
prueba.delete(2)
print(prueba)
prueba.delete(5)
print(prueba)