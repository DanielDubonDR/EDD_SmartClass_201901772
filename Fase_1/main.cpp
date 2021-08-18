#include <iostream>
#include <conio.h>
#include <string>
#include <stdlib.h>
#include <windows.h>
#include <sstream>
#include <fstream>

#include "Funciones.h"
#include "LinkedListDC.h"
#include "cola.h"

using namespace std;

//Declaracion de metodos y funcioens
int menu();
void cargarEstudiantes();
void prueba();

// Varialbles globales
ListDC *Estudiantes = new ListDC();
Queue *cola = new Queue();
int idCola=1;

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
            case 0: cargarEstudiantes(); break;
            case 1: cola->showQueue(); getch(); break;
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
    string m[5];
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

void cargarEstudiantes()
{
    clear();
    tituloEstudiantes();
    string pathEstudiantes;
    gotoxy(22, 11);   cout<<"- Ingrese la ruta del archivo";
    gotoxy(25, 13);   cout<<"> ";
    getline(cin, pathEstudiantes);
    gotoxy(22, 15);   cout<<"- Logs:";

    bool abierto;
    ifstream archivo;
    archivo.open(pathEstudiantes, ios::in);
    if(archivo.fail())
    {
        abierto=false;
    }
    else
    {
        abierto=true;
    }
    archivo.close();

    if(abierto)
    {
        gotoxy(25, 17); cout<<"> Archivo encontrado";
        int cont=2;
        ifstream file(pathEstudiantes);
        string line;
        getline(file, line);
        bool errores=false;
        gotoxy(25, 18); cout<<"> Leyendo archivo";
        gotoxy(25, 19); cout<<"> Extrayendo datos";
        while(getline(file, line))
        {
            stringstream data(line);
            string carnet, dpi, nombre, carrera, password, creditos, edad, email, descripcion="";
            getline(data, carnet, ',');
            getline(data, dpi, ',');
            getline(data, nombre, ',');
            getline(data, carrera, ',');
            getline(data, password, ',');
            getline(data, creditos, ',');
            getline(data, edad, ',');
            getline(data, email, ',');

            if(!verificarCarnet(carnet))
            {
                descripcion+="[ El carnet no presenta el formato debido ] \n\t\t  ";
            }
            if(!verificarDPI(dpi))
            {
                descripcion+="[ El DPI no presenta el formato debido ] \n\t\t  ";
            }
            if(!verificarEmail(email))
            {
                descripcion+="[ El correo no presenta el formato debido ]\n\t\t  ";
            }

            if(!verificarCarnet(carnet) || !verificarDPI(dpi) || !verificarEmail(email))
            {
                descripcion+="[ Error encontrado en la linea: "+to_string(cont)+" del archivo ]";
                cola->Enqueue(idCola, "Estudiante", descripcion);
                errores=true;
                idCola++;
            }
            else
            {
                Estudiantes->append(carnet, dpi, nombre, carrera, password, creditos, edad, email);
            }
            cont++;
        }
        gotoxy(25, 20); cout<<"> Archivo leido";
        if(errores==true)
        {
            gotoxy(25, 22); cout<<"- Se encontraron errores en el archivo, por favor revise la cola de errores";
        }
    }
    else
    {
        cout<<"Ocurrion un error, por favor verifique la ruta y estructura del archivo sean validas";
    }
    gotoxy(25, 24);
    system("pause");
}

void prueba()
{
    clear();

    // Queue *cola = new Queue();
    // cola->Enqueue(1, "Estudiante", "DPI");
    // cola->Enqueue(2, "Estudiante", "CARNE");
    // cola->Enqueue(3, "Tarea", "NI IDEA");
    // cola->showQueue();

    // ListDC *lista = new ListDC();
    // lista->append("201901772","3179425811504","Daniel Reginaldo Dubon Rodriguez","Sistemas","hola","120","22","danieldubon499@gmail.com");
    // lista->append("201901231","3112312333504","Pancho Francisco Doroteo","Industrial","Adios","100","32","danieldu99@gmail.com");
    // lista->showList();

    /*
    cout<<(verificarEmail("nicols36@hotmail.com") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("jernimo.caballero@yahoo.es") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("carolinaelizondo85@yahoo.com") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("alfonso03@hotmail..org") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("benitoarmas92@gmail.se") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("ngela.solorio86@yahoo.gt") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("carmen.#montenegro@outlook.com") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("adriana56@gmail.com") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("esperanza.meza41@hotmail.edu") ? "Valido" : "No valido")<<endl;
    cout<<(verificarEmail("horacio.tejada15@yahoo.org") ? "Valido" : "No valido")<<endl;
    string nombre="DANIEL daniel daniel ...";
    int cantidad = nombre.length();
    cout<<cantidad;
    */

    getch();
}
