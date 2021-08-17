#include <iostream>

using namespace std;

class NodeDC
{
    private:
        int dato;
        NodeDC *siguiente;
        NodeDC *anterior;
    public:
        NodeDC();
        NodeDC(int);
        NodeDC(int, NodeDC *, NodeDC *);

        int getDato();
        void setDato(int);

        NodeDC *getSiguiente();
        void setSiguiente(NodeDC *);
        NodeDC *getAnterior();
        void setAnterior(NodeDC *);
};

NodeDC::NodeDC()
{
    this->dato = 0;
    this->siguiente = NULL;
    this->anterior = NULL;
}

NodeDC::NodeDC(int _dato)
{
    this->dato = _dato;
    this->siguiente = NULL;
    this->anterior = NULL;
}

NodeDC::NodeDC(int _dato, NodeDC *_siguiente, NodeDC *_anterior)
{
    this->dato = _dato;
    this->siguiente = _siguiente;
    this->anterior = _anterior;
}

int NodeDC::getDato()
{
    return this->dato;
}

NodeDC *NodeDC::getSiguiente()
{
    return this->siguiente;
}

NodeDC *NodeDC::getAnterior()
{
    return this->anterior;
}

void NodeDC::setDato(int _dato)
{
    this->dato = _dato;
}

void NodeDC::setSiguiente(NodeDC *_siguiente)
{
    this->siguiente = _siguiente;
}

void NodeDC::setAnterior(NodeDC *_anterior)
{
    this->anterior = _anterior;
}
