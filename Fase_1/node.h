#include <iostream>

using namespace std;

class Node
{
    private:
        int id;
        string tipo;
        string descripcion;
        string iderr;
        Node *siguiente;

    public:
        Node();
        Node(int, string, string, string);

        int getID();
        string getTipo();
        string getDescripcion();
        string getIdErr();

        void setID(int);
        void setTipo(string);
        void setDescripcion(string);
        void setIdErr(string);

        Node *getSiguiente();
        void setSiguiente(Node *);
};

Node::Node()
{
    this->id = 0;
    this->tipo = "";
    this->descripcion = "";
    this->iderr="";
    this->siguiente = NULL;
}

Node::Node(int _id, string _tipo, string _descripcion, string _idErr)
{
    this->id = _id;
    this->tipo= _tipo;
    this->descripcion= _descripcion;
    this->iderr= _idErr;
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

string Node::getIdErr()
{
    return this->iderr;
}

Node *Node::getSiguiente()
{
    return this->siguiente;
}

void Node::setSiguiente(Node *_siguiente)
{
    this->siguiente = _siguiente;
}
