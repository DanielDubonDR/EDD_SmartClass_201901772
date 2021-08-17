#include <iostream>

using namespace std;

class Node
{
    private:
        string nombre;
        int edad;
        Node *siguiente;

    public:
        Node();
        Node(string, int);

        int getEdad();
        string getNombre();

        Node *getSiguiente();
        void setSiguiente(Node *);
};

Node::Node()
{
    this->nombre = "";
    this->edad = 0;
    this->siguiente = NULL;
}

Node::Node(string _nombre, int _edad)
{
    this->nombre = _nombre;
    this->edad= _edad;
    this->siguiente = NULL;
}

string Node::getNombre()
{
    return this->nombre;
}

int Node::getEdad()
{
    return this->edad;
}

Node *Node::getSiguiente()
{
    return this->siguiente;
}

void Node::setSiguiente(Node *_siguiente)
{
    this->siguiente = _siguiente;
}
