#include <iostream>
#include "nodeDD.h"

using namespace std;

class ListDC
{
    private:
        NodeDC *Cabeza;
        NodeDC *Cola;

    public:
        ListDC();

        bool isEmpty();
        int size();
        bool buscar(string);

        void showList();
        void append(string, string, string, string, string, string, string, string);
        void eliminar(string);
        void modificar(string, string);
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
    NodeDC *aux =  this->Cabeza;
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
    NodeDC *aux =  this->Cabeza;
    do
    {
        cout<<"Alumno: [ "<<aux->getCarnet()<<" "<<aux->getDPI()<<" "<<aux->getNombre()<<" "<<aux->getCarrera()<<" "<<aux->getPassword()<<" "<<aux->getCreditos()<<" "<<aux->getEdad()<<" "<<aux->getEmail()<<" ]"<<endl;
        aux = aux->getSiguiente();
    }
    while(aux != this->Cabeza);
}

void ListDC::append(string _carnet, string _dpi, string _nombre, string _carrera, string _password, string _creditos, string _edad, string _email)
{
    NodeDC *newNode = new NodeDC(_carnet, _dpi, _nombre, _carrera, _password, _creditos, _edad, _email);
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

void ListDC::modificar(string dpi, string _dato)
{
    NodeDC *aux = this->Cabeza;
    do
    {
        if (aux->getDPI() == dpi)
        {
            aux->setDPI(_dato);
            break;
        }
        aux = aux->getSiguiente();
    }
    while(aux != this->Cabeza);
}

bool ListDC::buscar(string dpi)
{
    bool encontrado=false;
    NodeDC *aux = this->Cabeza;
    do
    {
        if (aux->getDPI() == dpi)
        {
            encontrado=true;
            break;
        }
        aux = aux->getSiguiente();
    }
    while(aux != this->Cabeza);
    return encontrado;
}

void ListDC::eliminar(string dpi)
{
    NodeDC *aux = this->Cabeza;
    do
    {
        if (aux->getDPI() == dpi)
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
