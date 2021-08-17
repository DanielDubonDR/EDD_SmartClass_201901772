#include <iostream>

using namespace std;

class Node
{
    private:
        int id;
        string tipo;
        string descripcion;
        Node *siguiente;

    public:
        Node();
        Node(int, string, string);

        int getID();
        string getTipo();
        string getDescripcion();

        void setID(int);
        void setTipo(string);
        void setDescripcion(string);

        Node *getSiguiente();
        void setSiguiente(Node *);
};

Node::Node()
{
    this->id = 0;
    this->tipo = "";
    this->descripcion = "";
    this->siguiente = NULL;
}

Node::Node(int _id, string _tipo, string _descripcion)
{
    this->id = _id;
    this->tipo= _tipo;
    this->descripcion= _descripcion;
    this->siguiente = NULL;
}

int Node::getID()
{
    return this->id;
}

string Node::getTipo()
{
    return this->tipo;
}

string Node::getDescripcion()
{
    return this->descripcion;
}

Node *Node::getSiguiente()
{
    return this->siguiente;
}

void Node::setSiguiente(Node *_siguiente)
{
    this->siguiente = _siguiente;
}
