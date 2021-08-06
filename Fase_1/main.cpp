#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

using namespace std;

//Declaracion de metodos y funcioens
int menu();
void clear();
void gotoxy(int, int);
void cargarUsuarios();

// Varialbles globales
string pathUsers;

//Programa principal
int main()
{
    system("COLOR 71");
    int op;
    do
    {
        op = menu();
        switch (op)
        {
            case 0: cargarUsuarios(); break;
            case 1: break;
            case 2: break;
            case 3: break;
            case 4: break;
        }
    } while (op != 4);
}

//Menu principal
int menu(void)
{
    char *m[5];
    m[0] = "    1. Carga de usuarios";
    m[1] = "    2. Carga de tareas";
    m[2] = "    3. Ingreso manual";
    m[3] = "    4. Reportes";
    m[4] = "    5. Salir";
    char lec;
    int aux = 0, c, pos = 0;
    while (aux != 13)
    {
        clear();
        for (c = 0; c < 5; c++)
        {
            gotoxy(10, (c+5) * 2);
            if (pos == c)
            {
                cout <<"==> ";
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

void clear()
{
    system("cls");
}

void gotoxy(int x, int y)
{
    HANDLE hCon;
    hCon = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD dwPos;
    dwPos.X = x;
    dwPos.Y = y;
    SetConsoleCursorPosition(hCon, dwPos);
}

void cargarUsuarios()
{
    clear();
    getline(cin,pathUsers);
    cout<<pathUsers;
    getch();
}
