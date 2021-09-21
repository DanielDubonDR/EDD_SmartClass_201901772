class Lista_Simple:
    def __init__(self):
        self.cabeza = self.cola = None
        self.tamanio = 0
    
    def isEmpy(self):
        if self.cabeza == None and self.cola ==None:
            return True
        else:
            return False
            
    def prepend(self, nodo):
        newNode = nodo
        if self.isEmpy():
            self.cabeza = self.cola = newNode
            self.tamanio += 1
        else:
            newNode.siguiente = self.cabeza
            self.cabeza = newNode
            self.tamanio += 1
            
    def pop(self):
        if self.tamanio == 1:
            nodeAux = self.cabeza
            self.cabeza = self.cola = None
            self.tamanio = 0
            return nodeAux
        else:
            nodeAux = newCola = self.cabeza
            while nodeAux.siguiente != None:
                newCola = nodeAux
                nodeAux = nodeAux.siguiente
            newCola.siguiente = None
            self.cola = newCola
            self.tamanio-=1
            return nodeAux

    def __str__(self):
        string = ""
        nodeAux = self.cabeza
        while nodeAux != None:
            string += str(nodeAux)
            nodeAux = nodeAux.siguiente
        return string

# hola = Lista_Simple()
# hola.prepend(1)
# hola.prepend(2)
# hola.prepend(3)
# hola.prepend(4)
# hola.prepend(5)
# hola.pop()
# hola.pop()
# hola.pop()
# hola.pop()
# hola.pop()
# print(hola)
# print(hola.isEmpy())