class Nodo:
    def __init__(self, fila, columna, dato):
        self.fila = fila
        self.columna = columna
        self.dato =  dato
        self.derecha = None
        self.abajo = None
        self.izquierda = None
        self.arriba = None

class nCabecera:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None