#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

#include "Funciones.h"
#include "LinkedListDC.h"

using namespace std;

//Declaracion de metodos y funcioens
int menu();
void cargarUsuarios();
void prueba();

// Varialbles globales
string pathUsers;

//Programa principal
int main()
{
    //system("COLOR 71");
    int op;
    do
    {
        op = menu();
        switch (op)
        {
            case 0: cargarUsuarios(); break;
            case 1: prueba(); break;
            case 2: break;
            case 3: break;
            case 4: break;
        }
    } while (op != 4);

    return 0;
}

//Menu principal
int menu(void)
{
    char *m[5];
    m[0] = "   1. Carga de usuarios";
    m[1] = "   2. Carga de tareas";
    m[2] = "   3. Ingreso manual";
    m[3] = "   4. Reportes";
    m[4] = "   5. Salir";
    char lec;
    int aux = 0, c, pos = 0;
    while (aux != 13)
    {
        clear();
        titulo();
        for (c = 0; c < 5; c++)
        {
            gotoxy(15, (c+6) * 2);
            if (pos == c)
            {
                cout <<">>> ";
            }
            cout << m[c];
        }

        lec = getch();
        aux = (int)lec;
        if (aux == 72)
        {
            if (pos > 0)
            {
                pos = pos - 1;
            }
            else
            {
                pos = 4;
            }
        }
        if (aux == 80)
        {
            if (pos < 4)
            {
                pos = pos + 1;
            }
            else
            {
                pos = 0;
            }
        }
    }
    return pos;
}

void cargarUsuarios()
{
    clear();
    getline(cin,pathUsers);
    cout<<pathUsers;
    getch();
}

void prueba()
{
    clear();
    ListDC *lista = new ListDC();
    lista->append(1);
    lista->append(2);
    lista->append(3);
    lista->append(4);
    lista->append(5);
    lista->showList();
    cout<<endl;
    lista->modificar(1,11);
    lista->modificar(2,22);
    lista->modificar(3,33);
    lista->modificar(4,44);
    lista->modificar(5,55);
    lista->showList();
    cout<<endl;
    lista->borrar(33);
    lista->borrar(44);
    lista->showList();
    lista->append(31);
    cout<<endl;
    lista->showList();

    getch();
}
