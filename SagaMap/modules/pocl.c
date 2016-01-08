#include <pthread.h>
#include <Python.h>
#include <math.h>
/*const char* calcule_distance = "__kernel
void vec3DISTANCE(
    __global float* position,

    float x0,
    float y0,
    float z0,

    float x1,
    float y1,
    float z1){
    
    float x, y, z, sqrt;
    x = x0 - x1;
    y = y0 - y1;
    z = z0 - z1;
    
    sqrt = (x*x) + (y*y) + (z*z);
}
";*/

PyObject* KEY_MAP = NULL;
PyObject* KEY_MOBS = NULL;
PyObject* KEY_POS = NULL;

float vec3DISTANCE(float x0, float y0, float z0, float x1, float y1, float z1){
    return sqrt(pow(x0-x1, 2) + pow(y0-y1, 2) + pow(z0-z1, 2));
}

static PyObject*
init_opencl(PyObject* self, PyObject* args){
    PyObject* arc;
}

static PyObject*
calcule_ia(PyObject* self, PyObject* args){
    PyObject* dictionary;
    int length = 0, i = 0;

    if(!PyArg_ParseTuple(args, "O!", &PyDict_Type, &dictionary)){
        return NULL;
    }

    PyObject* maps = PyDict_GetItem(dictionary, KEY_MAP);
    length = PySequence_Size(maps);

    PyObject* item;
    PyObject* mobs;

    for(i = 0; i < length; i++){
        item = PyList_GetItem(maps, i);
        mobs = PyDict_GetItem(item, KEY_MOBS);

        if(PyList_Check(mobs)){
            int len = PySequence_Size(mobs);
            int a = 0;

            PyObject* mob;
            int *pos;

            for (a = 0; a < len; a++){
                mob = PyList_GetItem(mobs, i);
                pos = (int*)PyArg_ParseTuple(PyDict_GetItem(mob, KEY_POS), "iii", pos);
            }
        }
    }
}

static PyMethodDef calcule_methods[] = {
    {"calcule", calcule_ia, METH_VARARGS, "Calcula interligencia artificial"},
    {NULL, NULL, 0, NULL},
};

static PyModuleDef mod_calculeia = {
    PyModuleDef_HEAD_INIT,
    "calculeia",
    "Calculo de IA",
    -1,
    calcule_methods
};

PyMODINIT_FUNC
PyInit_calculeia(void){
    KEY_MAP = Py_BuildValue("s", "maps");
    KEY_MOBS = Py_BuildValue("s", "mobs");
    KEY_POS = Py_BuildValue("s", "pos");

    return PyModule_Create(&mod_calculeia);
}