#include <iostream>

using namespace std;

class NodeDC
{
    private:
        string carnet, dpi, nombre, carrera, password, creditos, edad, email;
        NodeDC *siguiente;
        NodeDC *anterior;
    public:
        
        // Constructores
        NodeDC();
        NodeDC(string, string, string, string, string, string, string, string);

        // Getters
        string getCarnet();
        string getDPI();
        string getNombre();
        string getCarrera();
        string getPassword();
        string getCreditos();
        string getEdad();
        string getEmail();

        // Setters
        void setCarnet(string);
        void setDPI(string);
        void setNombre(string);
        void setCarrera(string);
        void setPassword(string);
        void setCreditos(string);
        void setEdad(string);
        void setEmail(string);

        NodeDC *getSiguiente();
        void setSiguiente(NodeDC *);
        NodeDC *getAnterior();
        void setAnterior(NodeDC *);
};

NodeDC::NodeDC()
{
    this->carnet = "";
    this->dpi = "";
    this->nombre = "";
    this->carrera = "";
    this->password = "";
    this->creditos = "";
    this->edad = "";
    this->email = "";

    this->siguiente = NULL;
    this->anterior = NULL;
}

NodeDC::NodeDC(string _carnet, string _dpi, string _nombre, string _carrera, string _password, string _creditos, string _edad, string _email)
{
    this->carnet = _carnet;
    this->dpi = _dpi;
    this->nombre = _nombre;
    this->carrera = _carrera;
    this->password = _password;
    this->creditos = _creditos;
    this->edad = _edad;
    this->email = _email;

    this->siguiente = NULL;
    this->anterior = NULL;
}


string NodeDC::getCarnet()
{
    return this->carnet;
}

string NodeDC::getDPI()
{
    return this->dpi;
}

string NodeDC::getNombre()
{
    return this->nombre;
}

string NodeDC::getCarrera()
{
    return this->carrera;
}

string NodeDC::getPassword()
{
    return this->password;
}

string NodeDC::getCreditos()
{
    return this->creditos;
}

string NodeDC::getEdad()
{
    return this->edad;
}

string NodeDC::getEmail()
{
    return this->email;
}

NodeDC *NodeDC::getSiguiente()
{
    return this->siguiente;
}

NodeDC *NodeDC::getAnterior()
{
    return this->anterior;
}

void NodeDC::setCarnet(string _carnet)
{
    this->carnet = _carnet;
}

void NodeDC::setDPI(string _dpi)
{
    this->dpi = _dpi;
}

void NodeDC::setNombre(string _nombre)
{
    this->nombre = _nombre;
}

void NodeDC::setCarrera(string _carrera)
{
    this->carrera = _carrera;
}

void NodeDC::setPassword(string _password)
{
    this->password = _password;
}

void NodeDC::setCreditos(string _creditos)
{
    this->creditos = _creditos;
}

void NodeDC::setEdad(string _edad)
{
    this->edad = _edad;
}

void NodeDC::setEmail(string _email)
{
    this->email = _email;
}

void NodeDC::setSiguiente(NodeDC *_siguiente)
{
    this->siguiente = _siguiente;
}

void NodeDC::setAnterior(NodeDC *_anterior)
{
    this->anterior = _anterior;
}
