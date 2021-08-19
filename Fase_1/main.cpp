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
void ingresoManual();
int menuManual();
void opcionEstudiantes();
int menuEstudiante();
void ingresoEstudiantes();
void opcionModificar();
int menuModificarEstudiante();


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
            case 1: Estudiantes->graficar(); getch(); break;
            case 2: ingresoManual(); break;
            case 3: Estudiantes->showList(); getch(); break;
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

void ingresoManual()
{
    int op;
    do
    {
        op = menuManual();
        switch (op)
        {
            case 0: opcionEstudiantes(); break;
            case 1: break;
            case 2: break;
        }
    } while (op != 2);

}

int menuManual(void)
{
    string m[3];
    m[0] = "   1. Estudiantes";
    m[1] = "   2. Tareas";
    m[2] = "   3. Regresar";
    char lec;
    int aux = 0, c, pos = 0;
    while (aux != 13)
    {
        clear();
        tituloManual();
        for (c = 0; c < 3; c++)
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
                pos = 2;
            }
        }
        if (aux == 80)
        {
            if (pos < 2)
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

void opcionEstudiantes()
{
    int op;
    do
    {
        op = menuEstudiante();
        switch (op)
        {
            case 0: ingresoEstudiantes(); break;
            case 1: opcionModificar(); break;
            case 2:
            {
                string auxDPI;
                clear();
                tituloEliminar();
                gotoxy(41, 10); cout<<"Ingrese el DPI: ";
                getline(cin, auxDPI);

                if(Estudiantes->buscar(auxDPI))
                {
                    int decision;
                    cout<<endl;
                    Estudiantes->mostrarInfo(auxDPI);
                    cout<<"\n\n                                 - Esta seguro de eliminarlo? 1. Si 2. No : ";
                    cin>>decision;
                    if(decision==1)
                    {
                        Estudiantes->eliminar(auxDPI);
                        cout<<"\n\n                                 - Se ha eliminado con exito";
                    }
                    else if(decision==2)
                    {
                        cout<<"\n\n                                 - No se ha eliminado";
                    }
                    else
                    {
                        cout<<"\n\n                                 - Opcion incorrecta";
                    }
                    getch();
                }
                else
                {
                    gotoxy(36, 12); cout<<"INFORMACION: El DPI ingresado no se encuentra registrado";
                    getch();
                }
            } break;
            case 3: break;
        }
    } while (op != 3);

}

int menuEstudiante(void)
{
    string m[4];
    m[0] = "   1. Ingresar";
    m[1] = "   2. Modificar";
    m[2] = "   3. Eliminar";
    m[3] = "   4. Regresar";
    char lec;
    int aux = 0, c, pos = 0;
    while (aux != 13)
    {
        clear();
        tituloEstudiantes2();
        for (c = 0; c < 4; c++)
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
                pos = 3;
            }
        }
        if (aux == 80)
        {
            if (pos < 3)
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

void opcionModificar()
{
    string auxDPI;
    clear();
    gotoxy(36, 13); cout<<"Ingrese el DPI acutal: ";
    getline(cin, auxDPI);

    if(Estudiantes->buscar(auxDPI))
    {
        int op;
        do
        {
            op = menuModificarEstudiante();
            switch (op)
            {
                case 0:
                {
                    clear();
                    string nuevoCarne;
                    gotoxy(36, 12); cout<<"Ingrese el nuevo carnet: ";
                    getline(cin, nuevoCarne);
                    if(verificarCarnet(nuevoCarne))
                    {
                        Estudiantes->modificarCarne(auxDPI, nuevoCarne);
                        gotoxy(36, 14); cout<<" - Se ha modificado el carnet con exito";
                    }
                    else
                    {
                        gotoxy(36, 14); cout<<"- ERROR: El carnet ingresado no cumple con el fomrato debido";
                    }
                    getch();
                } break;
                case 1:
                {
                    clear();
                    string nuevoDPI;
                    gotoxy(36, 12); cout<<"Ingrese el nuevo DPI: ";
                    getline(cin, nuevoDPI);
                    if(verificarDPI(nuevoDPI))
                    {
                        Estudiantes->modificarDPI(auxDPI, nuevoDPI);
                        gotoxy(36, 14); cout<<" - Se ha modificado el DPI con exito";
                        op=8;
                    }
                    else
                    {
                        gotoxy(36, 14); cout<<"- ERROR: El DPI ingresado no cumple con el fomrato debido";
                    }
                    getch();
                } break;
                case 2:
                {
                    clear();
                    string nuevoNombre;
                    gotoxy(36, 12); cout<<"Ingrese el nuevo nombre: ";
                    getline(cin, nuevoNombre);
                    Estudiantes->modificarNombre(auxDPI, nuevoNombre);
                    gotoxy(36, 14); cout<<" - Se ha modificado el nombre con exito";
                    getch();
                } break;
                case 3:
                {
                    clear();
                    string nuevoCarrera;
                    gotoxy(36, 12); cout<<"Ingrese la carrera: ";
                    getline(cin, nuevoCarrera);
                    Estudiantes->modificarCarrera(auxDPI, nuevoCarrera);
                    gotoxy(36, 14); cout<<" - Se ha modificado la carrera con exito";
                    getch();
                } break;
                case 4:
                {
                    clear();
                    string nuevoPassword;
                    gotoxy(36, 12); cout<<"Ingrese el nuevo password: ";
                    getline(cin, nuevoPassword);
                    Estudiantes->modificarPassword(auxDPI, nuevoPassword);
                    gotoxy(36, 14); cout<<" - Se ha modificado el password con exito";
                    getch();
                } break;
                case 5:
                {
                    clear();
                    string nuevoCredito;
                    gotoxy(36, 12); cout<<"Ingrese los creditos: ";
                    getline(cin, nuevoCredito);
                    Estudiantes->modificarCreditos(auxDPI, nuevoCredito);
                    gotoxy(36, 14); cout<<" - Se ha modificado los creditos con exito";
                    getch();
                } break;
                case 6:
                {
                    clear();
                    string nuevoEdad;
                    gotoxy(36, 12); cout<<"Ingrese la edad: ";
                    getline(cin, nuevoEdad);
                    Estudiantes->modificarEdad(auxDPI, nuevoEdad);
                    gotoxy(36, 14); cout<<" - Se ha modificado la edad con exito";
                    getch();
                } break;
                case 7:
                {
                    clear();
                    string nuevoEmail;
                    gotoxy(36, 12); cout<<"Ingrese el correo: ";
                    getline(cin, nuevoEmail);
                    if(verificarEmail(nuevoEmail))
                    {
                        Estudiantes->modificarEmail(auxDPI, nuevoEmail);
                        gotoxy(36, 14); cout<<" - Se ha modificado el correo con exito";
                    }
                    else
                    {
                        gotoxy(36, 14); cout<<"- ERROR: El correo ingresado no cumple con el fomrato debido";
                    }
                    getch();
                } break;
                case 8: break;
            }
        } while (op != 8);
    }
    else
    {
        gotoxy(30, 13); cout<<"INFORMACION: El DPI ingresado no se encuentra registrado";
        getch();
    }

}

int menuModificarEstudiante(void)
{
    string m[9];
    m[0] = "   1. Modificar Carnet";
    m[1] = "   2. Modificar DPI";
    m[2] = "   3. Modificar Nombre";
    m[3] = "   4. Modificar Carrera";
    m[4] = "   5. Modificar Password";
    m[5] = "   6. Modificar Creditos";
    m[6] = "   7. Modificar Edad";
    m[7] = "   8. Modificar Correo";
    m[8] = "   9. Regresar";
    char lec;
    int aux = 0, c, pos = 0;
    while (aux != 13)
    {
        clear();
        tituloModificar();
        for (c = 0; c < 9; c++)
        {
            gotoxy(15, (c+5) * 2);
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
                pos = 8;
            }
        }
        if (aux == 80)
        {
            if (pos < 8)
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

void ingresoEstudiantes()
{
    clear();
    string carnet, dpi, nombre, carrera, password, creditos, edad, email;
    tituloIngreso();
    gotoxy(21, 10); cout<<"Carnet: ";
    gotoxy(21, 12); cout<<"DPI: ";
    gotoxy(21, 14); cout<<"Nombre: ";
    gotoxy(21, 16); cout<<"Carrera: ";
    gotoxy(21, 18); cout<<"Password: ";
    gotoxy(21, 20); cout<<"Creditos: ";
    gotoxy(21, 22); cout<<"Edad: ";
    gotoxy(21, 24); cout<<"Correo: ";
    gotoxy(33, 10); getline(cin, carnet);
    if(verificarCarnet(carnet))
    {
        gotoxy(33, 12); getline(cin, dpi);
        if(verificarDPI(dpi))
        {
            gotoxy(33, 14); getline(cin, nombre);
            gotoxy(33, 16); getline(cin, carrera);
            gotoxy(33, 18); getline(cin, password);
            gotoxy(33, 20); getline(cin, creditos);
            gotoxy(33, 22); getline(cin, edad);
            gotoxy(33, 24); getline(cin, email);
            if(verificarEmail(email))
            {
                Estudiantes->append(carnet, dpi, nombre, carrera, password, creditos, edad, email);
                gotoxy(21, 26); cout<<"- Se han registrado los datos correctamente";
            }
            else
            {
                gotoxy(21, 26); cout<<"- ERROR: El correo no cumple con el formato debido";
            }
        }
        else
        {
            gotoxy(21, 26); cout<<"- ERROR: El dpi no cumple con el formato debido";
        }
    }
    else
    {
        gotoxy(21, 26); cout<<"- ERROR: El carnet no cumple con el formato debido";
    }
    getch();
}
