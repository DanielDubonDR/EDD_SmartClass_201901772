#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

#include "Funciones.h"
#include "LinkedListDC.h"
#include "cola.h"

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

    Queue *cola = new Queue();
    cola->Enqueue("Daniel",22);
    cola->Enqueue("Reginaldo",23);
    cola->Enqueue("Dubon",23);
    cola->showQueue();

    // ListDC *lista = new ListDC();
    // lista->append("201901772","3179425811504","Daniel Reginaldo Dubon Rodriguez","Sistemas","hola","120","22","danieldubon499@gmail.com");
    // lista->append("201901231","3112312333504","Pancho Francisco Doroteo","Industrial","Adios","100","32","danieldu99@gmail.com");
    // lista->showList();

    getch();
}
