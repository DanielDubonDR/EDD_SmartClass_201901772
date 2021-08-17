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
        void Enqueue(string,int);
        void Enqueue2(string,int);
        void Dequeue();
        void Dequeue2();
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
        int cont=1;
        Node *aux =  this->Cabeza;
        while(aux != NULL)
        {
            cout<<" "<<cont<<".  Nombre: [ "<<aux->getNombre()<<" ]"<<endl<<"     Edad: [ "<<aux->getEdad()<<" ]"<<endl<<"             |"<<endl<<"             v"<<endl;
            aux = aux->getSiguiente();
            cont++;
        }
    }
}

void Queue::Enqueue(string _nombre, int _edad)
{
    Node *newNode = new Node(_nombre, _edad);
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
        cout<<"                    >  Nombre: [ "<<this->Cabeza->getNombre()<<" ]"<<endl<<"                    >  Edad: [ "<<this->Cabeza->getEdad()<<" ]";
        Node *aux =  this->Cabeza->getSiguiente();
        this->Cabeza=aux;
        cout<<"\n\n                    -  Se ha desencolado con exito";
    }
}

void Queue::Enqueue2(string _nombre, int _edad)
{
    Node *newNode = new Node(_nombre, _edad);
    if(isEmpty())
    {
        this->Cabeza=newNode;
    }
    else
    {
        newNode->setSiguiente(this->Cabeza);
        this->Cabeza=newNode;
    }
}

void Queue::Dequeue2()
{
    if(isEmpty())
    {
        cout<<"La cola esta vacia"<<endl;
    }
    else
    {
        Node *aux =  this->Cabeza;
        while(this->Cabeza->getSiguiente()->getSiguiente() != NULL)
        {
            this->Cabeza = this->Cabeza->getSiguiente();
        }
        this->Cabeza->setSiguiente(NULL);
        this->Cabeza=aux;
    }
}
