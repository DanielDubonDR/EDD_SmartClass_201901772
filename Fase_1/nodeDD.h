#include <iostream>

using namespace std;

class NodeD
{
    private:
        int dato;
        NodeD *siguiente;
        NodeD *anterior;
    public:
        NodeD();
        NodeD(int);
        NodeD(int, NodeD *, NodeD *);

        int getDato();
        void setDato(int);

        NodeD *getSiguiente();
        void setSiguiente(NodeD *);
        NodeD *getAnterior();
        void setAnterior(NodeD *);
};

NodeD::NodeD()
{
    this->dato = 0;
    this->siguiente = NULL;
    this->anterior = NULL;
}

NodeD::NodeD(int _dato)
{
    this->dato = _dato;
    this->siguiente = NULL;
    this->anterior = NULL;
}

NodeD::NodeD(int _dato, NodeD *_siguiente, NodeD *_anterior)
{
    this->dato = _dato;
    this->siguiente = _siguiente;
    this->anterior = _anterior;
}

int NodeD::getDato()
{
    return this->dato;
}

NodeD *NodeD::getSiguiente()
{
    return this->siguiente;
}

NodeD *NodeD::getAnterior()
{
    return this->anterior;
}

void NodeD::setDato(int _dato)
{
    this->dato = _dato;
}

void NodeD::setSiguiente(NodeD *_siguiente)
{
    this->siguiente = _siguiente;
}

void NodeD::setAnterior(NodeD *_anterior)
{
    this->anterior = _anterior;
}
