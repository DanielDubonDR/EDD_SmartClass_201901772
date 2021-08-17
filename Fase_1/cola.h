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
            cout<<"    ID: [ "<<aux->getID()<<" ]"<<endl<<"    Tipo: [ "<<aux->getTipo()<<" ]"<<endl<<"    Descripcion: [ "<<aux->getDescripcion()<<" ]"<<endl<<"             |"<<endl<<"             v"<<endl;
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
        cout<<"\n\n\n\n\n\n\n\n\n\n\n\n\                                      -  LA COLA ESTA VACIA";
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