#include <iostream>

using namespace std;

class NodeTask
{
    private:
        string carnet, tarea, descripcion, materia, fecha, hora, estado;

    public:
        NodeTask();
        NodeTask(string, string, string, string, string, string, string);

        string getCarnet();        
        string getTarea();
        string getDescripcion();
        string getMateria();
        string getFecha();
        string getHora();
        string getEstado();        

        void setCarnet(string);        
        void setTarea(string);
        void setDescripcion(string);
        void setMateria(string);
        void setFecha(string);
        void setHora(string);
        void setEstado(string);    
};

NodeTask::NodeTask()
{
    this->carnet="";
    this->tarea="";
    this->descripcion="";
    this->materia="";
    this->fecha="";
    this->hora="";
    this->estado="";
}

NodeTask::NodeTask(string _carnet, string _tarea, string _descripcion, string _materia, string _fecha, string _hora, string _estado)
{
    this->carnet=_carnet;
    this->tarea=_tarea;
    this->descripcion=_descripcion;
    this->materia=_materia;
    this->fecha=_fecha;
    this->hora=_hora;
    this->estado=_estado;
}



string NodeTask::getCarnet()
{
    return this->carnet;
}

string NodeTask::getTarea()
{
    return this->tarea;
}

string NodeTask::getDescripcion()
{
    return this->descripcion;
}

string NodeTask::getMateria()
{
    return this->materia;
}

string NodeTask::getFecha()
{
    return this->fecha;
}

string NodeTask::getHora()
{
    return this->hora;
}

string NodeTask::getEstado()
{
    return this->estado;
}

void NodeTask::setCarnet(string _carnet)
{
    this->carnet=_carnet;
}

void NodeTask::setTarea(string _tarea)
{
    this->tarea=_tarea;
}

void NodeTask::setDescripcion(string _descripcion)
{
    this->descripcion=_descripcion;
}

void NodeTask::setMateria(string _materia)
{
    this->materia=_materia;
}

void NodeTask::setFecha(string _fecha)
{
    this->fecha=_fecha;
}

void NodeTask::setHora(string _hora)
{
    this->hora=_hora;
}

void NodeTask::setEstado(string _estado)
{
    this->estado=_estado;
}
