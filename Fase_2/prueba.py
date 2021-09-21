from Analizador.Syntactic import parser
from Analizador.Syntactic import lista_usuarios, lista_tareas

if __name__ == '__main__':
    f = open('Estudiantes.txt',"r", encoding="utf-8")
    mensaje = f.read()
    f.close()

    parser.parse(mensaje)

    print(lista_usuarios)
    print("------------------------")
    print(lista_tareas)