#include <iostream>
#include "nodeDD.h"

using namespace std;

class ListDC
{
    private:
        NodeD *Cabeza;
        NodeD *Cola;

    public:
        ListDC();

        bool isEmpty();
        int size();

        void showList();
        void append(int dato);
        void eliminar(int);
        void borrar(int);
        void modificar(int, int);
};

ListDC::ListDC()
{
    this->Cabeza = NULL;
}

bool ListDC::isEmpty()
{
    return this->Cabeza == NULL;
}

int ListDC::size()
{
    NodeD *aux =  this->Cabeza;
    int cont = 0;
    while(aux != NULL)
    {
        cont++;
        aux = aux->getSiguiente();
    }
    return cont;
}

void ListDC::showList()
{
    NodeD *aux =  this->Cabeza;
    do
    {
        cout<<"Dato: [ "<<aux->getDato()<<" ]"<<endl;
        aux = aux->getSiguiente();
    }
    while(aux != this->Cabeza);
}

void ListDC::append(int _dato)
{
    NodeD *newNode = new NodeD(_dato);
    if(isEmpty())
    {
        this->Cabeza = newNode;
        this->Cola = newNode;
        this->Cabeza->setSiguiente(this->Cabeza);
        this->Cabeza->setAnterior(this->Cola);
    }
    else
    {
        this->Cola->setSiguiente(newNode);
        newNode->setAnterior(this->Cola);
        this->Cola=newNode;
        this->Cola->setSiguiente(this->Cabeza);
        this->Cabeza->setAnterior(this->Cola);
    }
}

void ListDC::eliminar(int _dato)
{
    NodeD *aux = this->Cabeza;
    while(this->Cabeza != NULL)
    {
        if (this->Cabeza->getDato() == _dato)
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

void ListDC::modificar(int id, int _dato)
{
    NodeD *aux = this->Cabeza;
    do
    {
        if (aux->getDato() == id)
        {
            aux->setDato(_dato);
            break;
        }
        aux = aux->getSiguiente();
    }
    while(aux != this->Cabeza);
}

void ListDC::borrar(int id)
{
    NodeD *aux = this->Cabeza;
    do
    {
        if (aux->getDato() == id)
        {
            if(aux == this->Cabeza)
            {
                this->Cabeza = this->Cabeza->getSiguiente();
                this->Cabeza->setAnterior(this->Cola);
                this->Cola->setSiguiente(this->Cabeza);
                break;
            }
            else if(aux == this->Cola)
            {
                this->Cola = this->Cola->getAnterior();
                this->Cola->setSiguiente(this->Cabeza);
                this->Cabeza->setAnterior(this->Cola);
                break;
            }
            else
            {
                aux->getSiguiente()->setAnterior(aux->getAnterior());
                aux->getAnterior()->setSiguiente(aux->getSiguiente());
                break;
            }
        }
        aux = aux->getSiguiente();
    }
    while(aux != this->Cabeza);
}
