
class Node:
    def __init__(self, puntero):
        self.puntero = puntero
        self.siguiente = None
        self.anterior = None

class ListaPuntero:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
    
    def isEmpty(self):
        if self.cabeza == None and self.cola == None:
            return True
        else:
            return False

    def appendPuntero(self, puntero):
        newNode = Node(puntero)
        if self.size < 5:
            if self.isEmpty():
                self.cabeza = self.cola = newNode
            else:
                newNode.anterior = self.cola
                self.cola.siguiente = newNode
                self.cola = newNode
            self.size += 1
        else:
            print("ERROR, tamanio excedido")

    def appendPunteroPagina(self, pagina, posicion):
        nodeAux = self.cabeza
        while posicion != 0 :
            posicion -= 1
            nodeAux = nodeAux.siguiente
        nodeAux.puntero = pagina

    def get(self, posicion):
        nodeAux = self.cabeza
        while posicion != 0 :
            posicion -= 1
            nodeAux = nodeAux.siguiente
        return nodeAux