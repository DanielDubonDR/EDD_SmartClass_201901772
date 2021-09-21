from Analizador.Lex import tokens
from Estructuras.simpleList import Lista_Simple
from Estructuras.Nodos import Nodo_Usuario, Nodo_Tarea, Nodo_UserTask

# Lists for save the information about users and tasks
lista_usuarios = Lista_Simple()
lista_tareas = Lista_Simple()

# This node allows to store information about one user or task
datos = Nodo_UserTask()

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    # print('Ok')

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

    if t[3] == "user":
        nodeAux = Nodo_Usuario(datos.Carnet, datos.DPI, datos.Nombre, datos.Carrera, datos.Password,datos.Creditos, datos.Edad, datos.Correo)
        lista_usuarios.prepend(nodeAux)
    else:
        nodeAux = Nodo_Tarea(datos.Carnet, datos.Nombre, datos.Descripcion, datos.Materia, datos.Fecha, datos.Hora, datos.Estado)
        lista_tareas.prepend(nodeAux)
    datos.reset()

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    t[0] = t[3].replace('"', '').replace(' ', '')


def p_items(t):
    """items : items item
    """
    t[0] = t[2]

def p_items_2(t):
    """items : item
    """
    t[0] = t[1]

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    if t[3].lower() == "carnet":
        datos.Carnet = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "dpi":
        datos.DPI = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "nombre":
        datos.Nombre = t[5].replace('"', '')
    elif t[3].lower() == "carrera":
        datos.Carrera = t[5].replace('"', '')
    elif t[3].lower() == "password":
        datos.Password = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "creditos":
        datos.Creditos = t[5]
    elif t[3].lower() == "edad":
        datos.Edad = t[5]
    elif t[3].lower() == "correo":
        datos.Correo = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "descripcion":
        datos.Descripcion = t[5].replace('"', '')
    elif t[3].lower() == "materia":
        datos.Materia = t[5].replace('"', '')
    elif t[3].lower() == "fecha":
        datos.Fecha = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "hora":
        datos.Hora = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "estado":
        datos.Estado = t[5].replace('"', '').replace(' ', '')

    t[0] = datos

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                | TCORREO
                """
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()