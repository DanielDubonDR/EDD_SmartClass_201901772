#include <iostream>

using namespace std;

class NodeDE
{
    private:
        string ID;
        string carnet, tarea, descripcion, materia, fecha, hora, estado;
        NodeDE *siguiente;
        NodeDE *anterior;
    public:
        NodeDE();
        NodeDE(string, string, string, string, string, string, string, string);

        string getID();
        string getCarnet();        
        string getTarea();
        string getDescripcion();
        string getMateria();
        string getFecha();
        string getHora();
        string getEstado();        

        void setID(string);
        void setCarnet(string);        
        void setTarea(string);
        void setDescripcion(string);
        void setMateria(string);
        void setFecha(string);
        void setHora(string);
        void setEstado(string);    

        NodeDE *getSiguiente();
        void setSiguiente(NodeDE *);
        NodeDE *getAnterior();
        void setAnterior(NodeDE *);
};

NodeDE::NodeDE()
{
    this->ID = "";
    this->carnet="";
    this->tarea="";
    this->descripcion="";
    this->materia="";
    this->fecha="";
    this->hora="";
    this->estado="";
    this->siguiente = NULL;
    this->anterior = NULL;
}

NodeDE::NodeDE(string _id, string _carnet, string _tarea, string _descripcion, string _materia, string _fecha, string _hora, string _estado)
{
    this->ID = _id;
    this->carnet=_carnet;
    this->tarea=_tarea;
    this->descripcion=_descripcion;
    this->materia=_materia;
    this->fecha=_fecha;
    this->hora=_hora;
    this->estado=_estado;
    this->siguiente = NULL;
    this->anterior = NULL;
}


string NodeDE::getID()
{
    return this->ID;
}

string NodeDE::getCarnet()
{
    return this->carnet;
}

string NodeDE::getTarea()
{
    return this->tarea;
}

string NodeDE::getDescripcion()
{
    return this->descripcion;
}

string NodeDE::getMateria()
{
    return this->materia;
}

string NodeDE::getFecha()
{
    return this->fecha;
}

string NodeDE::getHora()
{
    return this->hora;
}

string NodeDE::getEstado()
{
    return this->estado;
}

NodeDE *NodeDE::getSiguiente()
{
    return this->siguiente;
}

NodeDE *NodeDE::getAnterior()
{
    return this->anterior;
}

void NodeDE::setID(string _ID)
{
    this->ID = _ID;
}

void NodeDE::setCarnet(string _carnet)
{
    this->carnet=_carnet;
}

void NodeDE::setTarea(string _tarea)
{
    this->tarea=_tarea;
}

void NodeDE::setDescripcion(string _descripcion)
{
    this->descripcion=_descripcion;
}

void NodeDE::setMateria(string _materia)
{
    this->materia=_materia;
}

void NodeDE::setFecha(string _fecha)
{
    this->fecha=_fecha;
}

void NodeDE::setHora(string _hora)
{
    this->hora=_hora;
}

void NodeDE::setEstado(string _estado)
{
    this->estado=_estado;
}

void NodeDE::setSiguiente(NodeDE *_siguiente)
{
    this->siguiente = _siguiente;
}

void NodeDE::setAnterior(NodeDE *_anterior)
{
    this->anterior = _anterior;
}
