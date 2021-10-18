reserved = {
    'Elements' : 'TELEMENTS',
    'element' : 'TELEMENT',
    'type' : 'TTYPE',
    'item' : 'TITEM',
    'Carnet' : 'TCARNET',
    'DPI' : 'TDPI',
    'Nombre' : 'TNOMBRE',
    'Carrera' : 'TCARRERA',
    'Password' : 'TPASSWORD',
    'Creditos' : 'TCREDITOS',
    'Edad' : 'TEDAD',
    'Descripcion' : 'TDESCRIPCION',
    'Materia' : 'TMATERIA',
    'Fecha' : 'TFECHA',
    'Hora' : 'THORA',
    'Estado' : 'TESTADO',
    'Correo' : 'TCORREO'
 }

tokens = ['LQUESTION' ,'RQUESTION','DOLAR', 'ID', 'EQUALS', 'QUOTATION_MARKS', 'NUMBER','NORMSTRING', 'DATE', 'HOUR'] + list(reserved.values())

# ! Tokens
t_LQUESTION  = r'\¿'
t_RQUESTION  = r'\?'
t_DOLAR  = r'\$'
t_EQUALS  = r'='
t_QUOTATION_MARKS = r'\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_NORMSTRING(t):
    r'\"(\\.|[^"\\])*\"'
    return t

def t_Date(t):
    r'\s+(?=\d{2}(?:\d{2})?/\d{1,2}/\d{1,2}\b)'
    return t

def t_HORA(t):
    r'(?=(?:\b[01]\d|2[0-3]):[0-5]\d\b)'
    return t

t_ignore = ' \t\r\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
import re
lexer = lex.lex(reflags=re.IGNORECASE)
