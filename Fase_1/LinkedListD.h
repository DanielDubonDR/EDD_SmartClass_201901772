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
        void showListReverse();
        void append(string, string, string, string, string, string, string, string);
        void eliminar(string);
        void modificar(string, string);
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
        cout<<"Dato: [ "<<aux->getID()<<" "<<aux->getFecha()<<" ]"<<endl;
        aux = aux->getSiguiente();
    }
}

void ListD::showListReverse()
{
    NodeDE *aux =  this->Cola;
    while(aux != NULL)
    {
        cout<<"Dato: [ "<<aux->getID()<<" ]"<<endl;
        aux = aux->getAnterior();
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

void ListD::modificar(string id, string _dato)
{
    NodeDE *aux = this->Cabeza;
    while(this->Cabeza != NULL)
    {
        if (this->Cabeza->getID() == id)
        {
            this->Cabeza->setID(_dato);
            break;
        }
        this->Cabeza = this->Cabeza->getSiguiente();
    }
    this->Cabeza = aux;
}
