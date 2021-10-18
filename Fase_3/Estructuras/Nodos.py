class Nodo_Usuario:
    def __init__(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo):
        self.carnet = carnet
        self.dpi = dpi
        self.nombre = nombre
        self.carrera = carrera
        self.password = password
        self.creditos = creditos
        self.edad = edad
        self.correo = correo
        self.siguiente = None
    
    def __str__(self):
        return str(self.carnet)+" - "+str(self.dpi)+" - "+str(self.nombre)+str("\n")

class Nodo_Tarea:
    def __init__(self, carnet, nombre, descripcion, materia, fecha, hora, estado):
        self.carnet = carnet
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.siguiente = None
    
    def __str__(self):
        return str(self.carnet)+" - "+str(self.nombre)+" - "+str(self.descripcion)+str("\n")

class Nodo_UserTask:
    def __init__(self):
        self.type = ""
        self.Carnet = ""
        self.DPI = ""
        self.Nombre = ""
        self.Carrera = ""
        self.Password = ""
        self.Creditos = 0
        self.Edad = 0
        self.Correo = ""
        self.Descripcion = ""
        self.Materia = ""
        self.Fecha = ""
        self.Hora = ""
        self.Estado = ""

    def reset(self):
        self.type = ""
        self.Carnet = ""
        self.DPI = ""
        self.Nombre = ""
        self.Carrera = ""
        self.Password = ""
        self.Creditos = 0
        self.Edad = 0
        self.Correo = ""
        self.Descripcion = ""
        self.Materia = ""
        self.Fecha = ""
        self.Hora = ""
        self.Estado = ""