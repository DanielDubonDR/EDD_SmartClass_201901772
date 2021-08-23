#include <iostream>
#include "nodeD.h"

using namespace std;

class ListD
{
    private:
        NodeDE *Cabeza;
        NodeDE *Cola;

    public:
        ListD();

        bool isEmpty();
        int size();

        void showList();
        bool verificarEspacio(string);
        void append(string, string, string, string, string, string, string, string);
        void eliminar(string);
        void modificar(string, string, string, string, string, string, string, string);
        void mostrarTarea(string id);
        void modificarCarnet(string, string);
        void modificarTarea(string, string);
        void modificarDescripcion(string, string);
        void modificarMateria(string, string);
        void modificarFechaHora(string, string);
        void modificarEstado(string, string);
        void cambiarInfo(string, string, string, string);
        string codigoTareas();
        string invertir(string);
        void graficar(int);
        void graficar1(int);
        void graficar2(int);
        void graficar3(int);
        void graficar4(int);
        void graficar5(int);
        void graficar6(int);
};

ListD::ListD()
{
    this->Cabeza = NULL;
}

bool ListD::isEmpty()
{
    return this->Cabeza == NULL;
}

int ListD::size()
{
    NodeDE *aux =  this->Cabeza;
    int cont = 0;
    while(aux != NULL)
    {
        cont++;
        aux = aux->getSiguiente();
    }
    return cont;
}

void ListD::showList()
{
    NodeDE *aux =  this->Cabeza;
    while(aux != NULL)
    {
        cout<<"Dato: [ "<<aux->getID()<<" "<<aux->getCarnet()<<" "<<aux->getTarea()<<" "<<aux->getDescripcion()<<" "<<aux->getMateria()<<" "<<aux->getEstado()<<" "<<aux->getFecha()<<" ]"<<endl;
        aux = aux->getSiguiente();
    }
}

void ListD::append(string _id, string _carnet, string _tarea, string _descripcion, string _materia, string _fecha, string _hora, string _estado)
{
    NodeDE *newNode = new NodeDE(_id, _carnet, _tarea, _descripcion, _materia, _fecha, _hora, _estado);
    if(isEmpty())
    {
        this->Cabeza = newNode;
        this->Cola = this->Cabeza;
    }
    else
    {
        this->Cola->setSiguiente(newNode);
        newNode->setAnterior(this->Cola);
        this->Cola=newNode;
    }
}

void ListD::eliminar(string _dato)
{
    NodeDE *aux = this->Cabeza;
    while(this->Cabeza != NULL)
    {
        if (this->Cabeza->getID() == _dato)
        {
            if(aux == this->Cabeza)
            {
                aux = this->Cabeza->getSiguiente();
                aux->setAnterior(NULL);
                break;
            }
            else if (this->Cabeza == this->Cola)
            {
                this->Cola = this->Cabeza->getAnterior();
                this->Cola->setSiguiente(NULL);
                break;
            }
            else
            {
                this->Cabeza->getSiguiente()->setAnterior(this->Cabeza->getAnterior());
                this->Cabeza->getAnterior()->setSiguiente(this->Cabeza->getSiguiente());
                break;
            }
        }
        this->Cabeza = this->Cabeza->getSiguiente();
    }
    this->Cabeza = aux;
}

void ListD::modificar(string id, string _carnet, string _tarea, string _descripcion, string _materia, string _fecha, string _hora, string _estado)
{
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            aux->setCarnet(_carnet);
            aux->setTarea(_tarea);
            aux->setDescripcion(_descripcion);
            aux->setMateria(_materia);
            aux->setFecha(_fecha);
            aux->setHora(_hora);
            aux->setEstado(_estado);
            break;
        }
        aux = aux->getSiguiente();
    }
}

bool ListD::verificarEspacio(string id)
{
    bool encontrado=false;
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            if(aux->getCarnet()=="-1")
            {
                encontrado=true;
                break;
            }
        }
        aux = aux->getSiguiente();
    }
    return encontrado;
}

void ListD::mostrarTarea(string id)
{
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            cout<<"\t\t\t\tCarnet: "<<aux->getCarnet()<<endl<<endl;
            cout<<"\t\t\t\tNombre de la tarea: "<<aux->getTarea()<<endl<<endl;
            cout<<"\t\t\t\tDescripcion: "<<aux->getDescripcion()<<endl<<endl;
            cout<<"\t\t\t\tMateria: "<<aux->getMateria()<<endl<<endl;
            cout<<"\t\t\t\tFecha: "<<aux->getFecha()<<endl<<endl;
            cout<<"\t\t\t\tHora: "<<aux->getHora()<<endl<<endl;
            cout<<"\t\t\t\tEstado: "<<aux->getEstado()<<endl<<endl;
            break;
        }
        aux = aux->getSiguiente();
    }
}

void ListD::modificarCarnet(string id, string _carnet)
{
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            aux->setCarnet(_carnet);
            break;
        }
        aux = aux->getSiguiente();
    }
}

void ListD::modificarTarea(string id, string _tarea)
{
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            aux->setTarea(_tarea);
            break;
        }
        aux = aux->getSiguiente();
    }
}

void ListD::modificarDescripcion(string id, string _descripcion)
{
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            aux->setDescripcion(_descripcion);
            break;
        }
        aux = aux->getSiguiente();
    }
}

void ListD::modificarMateria(string id, string _materia)
{
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            aux->setMateria(_materia);
            break;
        }
        aux = aux->getSiguiente();
    }
}

void ListD::modificarEstado(string id, string _estado)
{
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == id)
        {
            aux->setEstado(_estado);
            break;
        }
        aux = aux->getSiguiente();
    }
}

void ListD::cambiarInfo(string idViejo, string idNuevo, string hora, string fecha)
{
    string _carnet="", _tarea="", _descripcion="", _materia="", _estado="";
    NodeDE *aux = this->Cabeza;
    while(aux != NULL)
    {
        if (aux->getID() == idViejo)
        {
            _carnet=aux->getCarnet();
            _tarea=aux->getTarea();
            _descripcion=aux->getDescripcion();
            _materia=aux->getMateria();
            _estado=aux->getEstado();
            break;
        }
        aux = aux->getSiguiente();
    }

    this->modificar(idNuevo,_carnet, _tarea, _descripcion, _materia, fecha, hora, _estado);

}


string ListD::codigoTareas()
{
    string codigo="";
    NodeDE *aux =  this->Cabeza;
    while(aux != NULL)
    {
        if(aux->getCarnet()!="-1")
        {
            codigo+="\t¿element type=\"task\"?\n";
            codigo+="\t\t¿item Carnet = \""+aux->getCarnet()+"\" $?\n";
            codigo+="\t\t¿item Nombre = \""+aux->getTarea()+"\" $?\n";
            codigo+="\t\t¿item Descripcion = \""+aux->getDescripcion()+"\" $?\n";
            codigo+="\t\t¿item Materia = \""+aux->getMateria()+"\" $?\n";
            codigo+="\t\t¿item Fecha = \""+this->invertir(aux->getFecha())+"\" $?\n";
            codigo+="\t\t¿item Hora = \""+aux->getHora()+"\" $?\n";
            codigo+="\t\t¿item Estado = \""+aux->getEstado()+"\" $?\n";
            codigo+="\t¿$element?\n";
        }
        aux = aux->getSiguiente();
    }
    codigo+="¿$Elements?";
    return codigo;
}

string ListD::invertir(string cad)
{
    string dia="", mes="", anio="", aux;
    for (int i=0; i<4; i++)
    {
        anio+=cad[i];
    }
    for (int i=5; i<7; i++)
    {
        mes+=cad[i];
    }
    for (int i=8; i<10; i++)
    {
        dia+=cad[i];
    }
    aux=dia+"/"+mes+"/"+anio;
    return aux;
}

void ListD::graficar(int orden)
{
    NodeDE *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Alumnos {\n rankdir=LR;\n label=\"LISTA DE TAREAS\";\n  node [shape = note, color=\"#27ae60\", style=filled, fillcolor=\"#2ecc71\"];\n";
    while(aux->getID() != "201")
    {
        dataNode+= "N"+to_string(cont)+"[label=\"ID: "+aux->getID()+" \\lCarnet: "+aux->getCarnet()+" \\lNombre: "+aux->getTarea()+" \\lDescripcion: "+aux->getDescripcion()+" \\lMateria: "+aux->getMateria()+" \\lFecha: "+aux->getFecha()+" \\lHora: "+aux->getHora()+" \\lEstado: "+aux->getEstado()+"\"];\n";
        if(aux->getAnterior() != NULL)
        {
            dataEdge += "N" + to_string(cont-1) + "->N" + to_string(cont) + ";\n";
            dataEdge += "N" + to_string(cont) + "->N" + to_string(cont-1) + ";\n";
        }
        aux = aux->getSiguiente();
        cont++;
    }
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ListaTareas.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ListaTareas.dot -o  " + path + "ListaTareas"+to_string(orden)+".png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}

void ListD::graficar1(int orden)
{
    NodeDE *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Alumnos {\n rankdir=LR;\n label=\"LISTA DE TAREAS\";\n  node [shape = note, color=\"#27ae60\", style=filled, fillcolor=\"#2ecc71\"];\n";
    while(aux->getID()!="401")
    {
        if(stoi(aux->getID())>200)
        {
            dataNode+= "N"+to_string(cont)+"[label=\"ID: "+aux->getID()+" \\lCarnet: "+aux->getCarnet()+" \\lNombre: "+aux->getTarea()+" \\lDescripcion: "+aux->getDescripcion()+" \\lMateria: "+aux->getMateria()+" \\lFecha: "+aux->getFecha()+" \\lHora: "+aux->getHora()+" \\lEstado: "+aux->getEstado()+"\"];\n";
            if(stoi(aux->getID())>201)
            {
                dataEdge += "N" + to_string(cont-1) + "->N" + to_string(cont) + ";\n";
                dataEdge += "N" + to_string(cont) + "->N" + to_string(cont-1) + ";\n";
            }
        }
        aux = aux->getSiguiente();
        cont++;
    }
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ListaTareas.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ListaTareas.dot -o  " + path + "ListaTareas"+to_string(orden)+".png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}

void ListD::graficar2(int orden)
{
    NodeDE *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Alumnos {\n rankdir=LR;\n label=\"LISTA DE TAREAS\";\n  node [shape = note, color=\"#27ae60\", style=filled, fillcolor=\"#2ecc71\"];\n";
    while(aux->getID()!="601")
    {
        if(stoi(aux->getID())>400)
        {
            dataNode+= "N"+to_string(cont)+"[label=\"ID: "+aux->getID()+" \\lCarnet: "+aux->getCarnet()+" \\lNombre: "+aux->getTarea()+" \\lDescripcion: "+aux->getDescripcion()+" \\lMateria: "+aux->getMateria()+" \\lFecha: "+aux->getFecha()+" \\lHora: "+aux->getHora()+" \\lEstado: "+aux->getEstado()+"\"];\n";
            if(stoi(aux->getID())>401)
            {
                dataEdge += "N" + to_string(cont-1) + "->N" + to_string(cont) + ";\n";
                dataEdge += "N" + to_string(cont) + "->N" + to_string(cont-1) + ";\n";
            }
        }
        aux = aux->getSiguiente();
        cont++;
    }
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ListaTareas.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ListaTareas.dot -o  " + path + "ListaTareas"+to_string(orden)+".png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}

void ListD::graficar3(int orden)
{
    NodeDE *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Alumnos {\n rankdir=LR;\n label=\"LISTA DE TAREAS\";\n  node [shape = note, color=\"#27ae60\", style=filled, fillcolor=\"#2ecc71\"];\n";
    while(aux->getID()!="801")
    {
        if(stoi(aux->getID())>600)
        {
            dataNode+= "N"+to_string(cont)+"[label=\"ID: "+aux->getID()+" \\lCarnet: "+aux->getCarnet()+" \\lNombre: "+aux->getTarea()+" \\lDescripcion: "+aux->getDescripcion()+" \\lMateria: "+aux->getMateria()+" \\lFecha: "+aux->getFecha()+" \\lHora: "+aux->getHora()+" \\lEstado: "+aux->getEstado()+"\"];\n";
            if(stoi(aux->getID())>601)
            {
                dataEdge += "N" + to_string(cont-1) + "->N" + to_string(cont) + ";\n";
                dataEdge += "N" + to_string(cont) + "->N" + to_string(cont-1) + ";\n";
            }
        }
        aux = aux->getSiguiente();
        cont++;
    }
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ListaTareas.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ListaTareas.dot -o  " + path + "ListaTareas"+to_string(orden)+".png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}

void ListD::graficar4(int orden)
{
    NodeDE *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Alumnos {\n rankdir=LR;\n label=\"LISTA DE TAREAS\";\n  node [shape = note, color=\"#27ae60\", style=filled, fillcolor=\"#2ecc71\"];\n";
    while(aux->getID()!="1001")
    {
        if(stoi(aux->getID())>800)
        {
            dataNode+= "N"+to_string(cont)+"[label=\"ID: "+aux->getID()+" \\lCarnet: "+aux->getCarnet()+" \\lNombre: "+aux->getTarea()+" \\lDescripcion: "+aux->getDescripcion()+" \\lMateria: "+aux->getMateria()+" \\lFecha: "+aux->getFecha()+" \\lHora: "+aux->getHora()+" \\lEstado: "+aux->getEstado()+"\"];\n";
            if(stoi(aux->getID())>801)
            {
                dataEdge += "N" + to_string(cont-1) + "->N" + to_string(cont) + ";\n";
                dataEdge += "N" + to_string(cont) + "->N" + to_string(cont-1) + ";\n";
            }
        }
        aux = aux->getSiguiente();
        cont++;
    }
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ListaTareas.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ListaTareas.dot -o  " + path + "ListaTareas"+to_string(orden)+".png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}

void ListD::graficar5(int orden)
{
    NodeDE *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Alumnos {\n rankdir=LR;\n label=\"LISTA DE TAREAS\";\n  node [shape = note, color=\"#27ae60\", style=filled, fillcolor=\"#2ecc71\"];\n";
    while(aux->getID()!="1201")
    {
        if(stoi(aux->getID())>1000)
        {
            dataNode+= "N"+to_string(cont)+"[label=\"ID: "+aux->getID()+" \\lCarnet: "+aux->getCarnet()+" \\lNombre: "+aux->getTarea()+" \\lDescripcion: "+aux->getDescripcion()+" \\lMateria: "+aux->getMateria()+" \\lFecha: "+aux->getFecha()+" \\lHora: "+aux->getHora()+" \\lEstado: "+aux->getEstado()+"\"];\n";
            if(stoi(aux->getID())>1001)
            {
                dataEdge += "N" + to_string(cont-1) + "->N" + to_string(cont) + ";\n";
                dataEdge += "N" + to_string(cont) + "->N" + to_string(cont-1) + ";\n";
            }
        }
        aux = aux->getSiguiente();
        cont++;
    }
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ListaTareas.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ListaTareas.dot -o  " + path + "ListaTareas"+to_string(orden)+".png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}

void ListD::graficar6(int orden)
{
    NodeDE *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Alumnos {\n rankdir=LR;\n label=\"LISTA DE TAREAS\";\n  node [shape = note, color=\"#27ae60\", style=filled, fillcolor=\"#2ecc71\"];\n";
    while(aux != NULL)
    {
        if(stoi(aux->getID())>1200)
        {
            dataNode+= "N"+to_string(cont)+"[label=\"ID: "+aux->getID()+" \\lCarnet: "+aux->getCarnet()+" \\lNombre: "+aux->getTarea()+" \\lDescripcion: "+aux->getDescripcion()+" \\lMateria: "+aux->getMateria()+" \\lFecha: "+aux->getFecha()+" \\lHora: "+aux->getHora()+" \\lEstado: "+aux->getEstado()+"\"];\n";
            if(stoi(aux->getID())>1201)
            {
                dataEdge += "N" + to_string(cont-1) + "->N" + to_string(cont) + ";\n";
                dataEdge += "N" + to_string(cont) + "->N" + to_string(cont-1) + ";\n";
            }
        }
        aux = aux->getSiguiente();
        cont++;
    }
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ListaTareas.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ListaTareas.dot -o  " + path + "ListaTareas"+to_string(orden)+".png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}