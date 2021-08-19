#include <iostream>
#include "node.h"

using namespace std;

class Queue
{
    private:
        Node *Cabeza;

    public:
        Queue();

        bool isEmpty();
        int size();

        void showQueue();
        void Enqueue(int, string, string);
        void Dequeue();
        void graficar();
};

Queue::Queue()
{
    this->Cabeza = NULL;
}

bool Queue::isEmpty()
{
    return this->Cabeza == NULL;
}

int Queue::size()
{
    Node *aux =  this->Cabeza;
    int cont = 0;
    while(aux != NULL)
    {
        cont++;
        aux = aux->getSiguiente();
    }
    return cont;
}

void Queue::showQueue()
{
    if(isEmpty())
    {
        cout<<"                                      -  LA COLA ESTA VACIA";
    }
    else
    {
        Node *aux =  this->Cabeza;
        while(aux != NULL)
        {
            cout<<"    ID: [ "<<aux->getID()<<" ]"<<endl<<"    Tipo: [ "<<aux->getTipo()<<" ]"<<endl<<"    Descripcion:  "<<aux->getDescripcion()<<endl<<"             |"<<endl<<"             v"<<endl;
            aux = aux->getSiguiente();
        }
    }
}

void Queue::Enqueue(int _id, string _tipo, string _descripcion)
{
    Node *newNode = new Node(_id, _tipo, _descripcion);
    if(isEmpty())
    {
        this->Cabeza=newNode;
    }
    else
    {
        Node *aux =  this->Cabeza;
        while(this->Cabeza->getSiguiente() != NULL)
        {
            this->Cabeza = this->Cabeza->getSiguiente();
        }
        this->Cabeza->setSiguiente(newNode);
        this->Cabeza=aux;
    }
}

void Queue::Dequeue()
{
    if(isEmpty())
    {
        cout<<"\n\n\n\n\n\n\n\n\n\n\n\n                                      -  LA COLA ESTA VACIA";
    }
    else
    {
        cout<<"\n\n\n\n\n\n\n\n\n\n                                  DATOS DESENCOLADOS:"<<endl<<endl;
        cout<<"                    >  ID: [ "<<this->Cabeza->getID()<<" ]"<<endl<<"                    >  Tipo: [ "<<this->Cabeza->getTipo()<<" ]"<<endl<<"                    >  Tipo: [ "<<this->Cabeza->getDescripcion()<<" ]";
        Node *aux =  this->Cabeza->getSiguiente();
        this->Cabeza=aux;
        cout<<"\n\n                    -  Se ha desencolado con exito";
    }
}

void Queue::graficar()
{
    Node *aux =  this->Cabeza;
    int cont=0;
    string dataNode="", dataEdge="";
    string grafica="digraph Errores {\n rankdir=LR;\n label=\"COLA DE ERRORES\";\n  node [shape = note, color=\"#c0392b\", style=filled, fillcolor=\"#ff7979\"];\n";
    while(aux != NULL)
    {
        dataNode+= "N"+to_string(cont)+"[label=\"ID: "+to_string(aux->getID())+" \\lTipo: "+aux->getTipo()+" \\lDescripcion: "+aux->getDescripcion()+"\"];\n";
        if(aux->getSiguiente() != NULL)
        {
            dataEdge += "N" + to_string(cont+1) + "->N" + to_string(cont) + ";\n";
        }
        aux = aux->getSiguiente();
        cont++;
    }
    dataNode+="aux[label=\"Salida\", shape=none, style=none];\n aux1[label=\"Llegada\", shape=none, style=none];\n";
    dataEdge+="N0->aux; \n aux1->N"+to_string(cont-1)+";";
    grafica += dataNode;
    grafica += dataEdge;
    grafica += "\n}";
    try
    {
        string path = "..\\Reportes\\";
        ofstream file;
        file.open(path + "ColaErrores.dot",std::ios::out);
        if(file.fail())
        {
            exit(1);
        }
        file<<grafica;
        file.close();
        string command = "dot -Tpng " + path + "ColaErrores.dot -o  " + path + "ColaErrores.png";
        system(command.c_str());
    }
    catch(exception e)
    {
        cout<<"Ocurrio un error"<<endl;
    }
}