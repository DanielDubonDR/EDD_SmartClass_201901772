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
#include "LinkedListD.h"
#include "TaskN.h"

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
void reportes();
int menuReportes();
void cargarTareas();
void inicializarMatriz();
void verMatriz();
void linealizacion();
void opcionTareas();
int menuTareas();
void ingresoTareas();


// Varialbles globales
ListDC *Estudiantes = new ListDC();
Queue *cola = new Queue();
NodeTask *TareasM[5][30][9];
ListD *Tareas = new ListD();
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
            case 1: cargarTareas(); break;  /*Estudiantes->graficar(); getch();*/
            case 2: ingresoManual(); break;
            case 3: reportes(); break;
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
            case 1: opcionTareas(); break;
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

void reportes()
{
    int op;
    do
    {
        op = menuReportes();
        switch (op)
        {
            case 0:
            {
                clear();
                gotoxy(38, 12);
                Estudiantes->graficar();
                gotoxy(38,14); cout<<"- Reporte generado con exito";
                getch();
            } break;
            case 1: clear(); Tareas->showList(); getch(); break;
            case 2: break;
            case 3: break;
            case 4:
            {
                clear();
                gotoxy(38, 12);
                cola->graficar();
                gotoxy(38,14); cout<<"- Reporte generado con exito";
                getch();
            } break;
            case 5: break;
            case 6: break;
        }
    } while (op != 6);

}

int menuReportes(void)
{
    string m[7];
    m[0] = "   1. Reporte sobre la lista de estudiantes";
    m[1] = "   2. Reporte sobre la lista de tareas linealizadas";
    m[2] = "   3. Busqueda en estructura linealizada";
    m[3] = "   4. Busqueda de posicion en lista linealizada";
    m[4] = "   5. Cola de Errores";
    m[5] = "   6. Codigo generado de salida";
    m[6] = "   7. Regresar";
    char lec;
    int aux = 0, c, pos = 0;
    while (aux != 13)
    {
        clear();
        tituloReportes();
        for (c = 0; c < 7; c++)
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
                pos = 6;
            }
        }
        if (aux == 80)
        {
            if (pos < 6)
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
                descripcion+="[ El carnet no presenta el formato debido ]\\l                    ";
            }
            if(!verificarDPI(dpi))
            {
                descripcion+="[ El DPI no presenta el formato debido ]\\l                    ";
            }
            if(!verificarEmail(email))
            {
                descripcion+="[ El correo no presenta el formato debido ]\\l                    ";
            }

            if(!verificarCarnet(carnet) || !verificarDPI(dpi) || !verificarEmail(email))
            {
                descripcion+="[ Error encontrado en la linea: "+to_string(cont)+" del archivo ]";
                cola->Enqueue(idCola, "Estudiante", descripcion);
                Estudiantes->append(carnet, dpi, nombre, carrera, password, creditos, edad, email);
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

void cargarTareas()
{
    clear();
    //tituloEstudiantes();
    string pathTareas;
    gotoxy(22, 11);   cout<<"- Ingrese la ruta del archivo";
    gotoxy(25, 13);   cout<<"> ";
    getline(cin, pathTareas);
    gotoxy(22, 15);   cout<<"- Logs:";

    ifstream archivo;
    archivo.open(pathTareas, ios::in);
    if(!archivo.fail())
    {
        inicializarMatriz();
        gotoxy(25, 17); cout<<"> Archivo encontrado";
        string line;
        getline(archivo, line);
        bool errores=false;
        gotoxy(25, 18); cout<<"> Leyendo archivo";
        gotoxy(25, 19); cout<<"> Extrayendo datos";
        int cont=2;
        while(getline(archivo, line))
        {
            stringstream data(line);
            string idMes, idDia, idHora, carnet, tarea, descripcion, materia, fecha, hora, estado, descripcionERR="";

            getline(data, idMes, ',');
            getline(data, idDia, ',');
            getline(data, idHora, ',');
            getline(data, carnet, ',');
            getline(data, tarea, ',');
            getline(data, descripcion, ',');
            getline(data, materia, ',');
            getline(data, fecha, ',');
            getline(data, estado, ',');

            if(!verificarRangoMes(idMes))
            {
                descripcionERR+="[ El mes esta fuera de rango ]\\l                    ";
            }
            if(!verificarRangoDia(idDia))
            {
                descripcionERR+="[ El dia esta fuera de rango ]\\l                    ";
            }
            if(!verificarRangoHora(idHora))
            {
                descripcionERR+="[ La hora esta fuera de rango ]\\l                    ";
            }
            if(!Estudiantes->buscarCarnet(carnet))
            {
                descripcionERR+="[ El carnet del estudiante no se encuentra registrado ]\\l                    ";
            }

            if(!validarFecha(fecha))
            {
                descripcionERR+="[ La fecha no cumple con el formato debido ]\\l                    ";
            }

            if(!verificarRangoMes(idMes) || !verificarRangoDia(idDia) || !verificarRangoHora(idHora))
            {
                descripcionERR+="[ Error encontrado en la linea: "+to_string(cont)+" del archivo ]";
                cola->Enqueue(idCola, "Tarea", descripcion);
                errores=true;
                idCola++;
            }
            else
            {
                // cout<<idMes<<endl;
                // cout<<idDia<<endl;
                // cout<<idHora<<endl;
                // cout<<carnet<<endl;
                // cout<<tarea<<endl;
                // cout<<descripcion<<endl;
                // cout<<materia<<endl;
                // cout<<fecha<<endl;
                // cout<<estado<<endl<<endl;
                hora=idHora+":00";
                TareasM[indexMes(idMes)][stoi(idDia)-1][indexHora(idHora)]=new NodeTask(carnet, tarea, descripcion,materia, fecha, hora, estado);

            }
            //SEGUIR TRABAJANDO ACA
            if(!Estudiantes->buscarCarnet(carnet) || !validarFecha(fecha))
            {
                descripcionERR+="[ Error encontrado en la linea: "+to_string(cont)+" del archivo ]";
                cola->Enqueue(idCola, "Tareaa", descripcion);
                errores=true;
                idCola++;
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
    archivo.close();
    linealizacion();
    gotoxy(25, 24);
    system("pause");
}

void inicializarMatriz()
{
    for(int i=0; i<5; i++)
    {
        for (int j = 0; j < 30; j++)
        {
            for(int k=0; k<9; k++)
            {
                TareasM[i][j][k]=NULL;
            }
        }

    }
}

void verMatriz()
{
    for(int i=0; i<5; i++)
    {
        for (int j = 0; j < 30; j++)
        {
            for(int k=0; k<9; k++)
            {
                if(TareasM[i][j][k]!=NULL)
                {
                    cout<<TareasM[i][j][k]->getCarnet()<<endl;
                }
            }
        }

    }
}

void linealizacion()
{
    for(int i=0; i<5; i++)
    {
        for (int j = 0; j < 30; j++)
        {
            for(int k=0; k<9; k++)
            {
                int id=k+(9*(j+(30*i)));
                if(TareasM[i][j][k]!=NULL)
                {
                    Tareas->append(to_string(id), TareasM[i][j][k]->getCarnet(), TareasM[i][j][k]->getTarea(), TareasM[i][j][k]->getDescripcion(), TareasM[i][j][k]->getMateria(), TareasM[i][j][k]->getFecha(), TareasM[i][j][k]->getHora(), TareasM[i][j][k]->getEstado());
                }
                else
                {
                    Tareas->append(to_string(id), "-1", "-1", "-1", "-1", "-1", "-1", "-1");
                }
            }
        }

    }
}

void opcionTareas()
{
    int op;
    do
    {
        op = menuTareas();
        switch (op)
        {
            case 0: ingresoTareas(); break;
            case 1: break;
            case 2:
            {
                // string auxDPI;
                // clear();
                // tituloEliminar();
                // gotoxy(41, 10); cout<<"Ingrese el DPI: ";
                // getline(cin, auxDPI);

                // if(Estudiantes->buscar(auxDPI))
                // {
                //     int decision;
                //     cout<<endl;
                //     Estudiantes->mostrarInfo(auxDPI);
                //     cout<<"\n\n                                 - Esta seguro de eliminarlo? 1. Si 2. No : ";
                //     cin>>decision;
                //     if(decision==1)
                //     {
                //         Estudiantes->eliminar(auxDPI);
                //         cout<<"\n\n                                 - Se ha eliminado con exito";
                //     }
                //     else if(decision==2)
                //     {
                //         cout<<"\n\n                                 - No se ha eliminado";
                //     }
                //     else
                //     {
                //         cout<<"\n\n                                 - Opcion incorrecta";
                //     }
                //     getch();
                // }
                // else
                // {
                //     gotoxy(36, 12); cout<<"INFORMACION: El DPI ingresado no se encuentra registrado";
                //     getch();
                // }
            } break;
            case 3: break;
        }
    } while (op != 3);

}

int menuTareas(void)
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
        tituloTareas();
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

void ingresoTareas()
{
    clear();
    string mes, dia, hora, carnet, tarea, descripcion, materia, fecha, estado;
    tituloIngreso();
    gotoxy(21, 10); cout<<"Mes: ";
    gotoxy(21, 12); cout<<"Dia: ";
    gotoxy(21, 14); cout<<"Hora: ";
    gotoxy(21, 16); cout<<"Carnet: ";
    gotoxy(21, 18); cout<<"Tarea: ";
    gotoxy(21, 20); cout<<"Descripcion: ";
    gotoxy(21, 22); cout<<"Materia: ";
    gotoxy(21, 24); cout<<"Fecha: ";
    gotoxy(21, 26); cout<<"Estado: ";
    gotoxy(33, 10); getline(cin, mes);
    if(verificarRangoMes(mes))
    {
        gotoxy(33, 12); getline(cin, dia);
        if(verificarRangoDia(dia))
        {
            gotoxy(33, 14); getline(cin, hora);
            if(verificarRangoHora(hora))
            {
                int i = indexMes(mes);
                int j = (stoi(dia)-1);
                int k = indexHora(hora);
                int id=k+(9*(j+(30*i)));
                if(Tareas->verificarEspacio(to_string(id)))
                {
                    gotoxy(33, 16); getline(cin, carnet);
                    if(Estudiantes->buscarCarnet(carnet))
                    {
                        gotoxy(33, 18); getline(cin, tarea);
                        gotoxy(33, 20); getline(cin, descripcion);
                        gotoxy(33, 22); getline(cin, materia);
                        gotoxy(33, 24); getline(cin, fecha);
                        if(validarFecha(fecha))
                        {
                            string aux=hora+":00";
                            gotoxy(33, 26); getline(cin, estado);
                            Tareas->modificar(to_string(id), carnet, tarea, descripcion,materia,fecha,aux,estado);
                            gotoxy(21, 26); cout<<"- Se ha registrado la tarea correctamente";
                        }
                        else
                        {
                            gotoxy(21, 28); cout<<"- ERROR: La fecha no cumple con el formato establecido";
                        }
                    }
                    else
                    {
                        gotoxy(21, 28); cout<<"- ERROR: El carnet no esta registrado";
                    }
                }
                else
                {
                    gotoxy(21, 28); cout<<"- ERROR: Este horario ya esta ocupado";
                }
            }
            else
            {
                 gotoxy(21, 28); cout<<"- ERROR: La hora esta fuera de rango";
            }
        }
        else
        {
            gotoxy(21, 28); cout<<"- ERROR: El dia esta fuera de rango";
        }
    }
    else
    {
        gotoxy(21, 28); cout<<"- ERROR: El mes esta fuera del rango";
    }
    getch();
}

