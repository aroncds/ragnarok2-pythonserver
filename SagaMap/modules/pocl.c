#include <pthread.h>
#include <Python.h>
#include <CL/cl.h>
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

float vec3DISTANCE(float x0, float y0, float z0, float x1, float y1, float z1){
    return sqrt(pow(x0-x1, 2) + pow(y0-y1, 2) + pow(z0-z1, 2));
}

float vec3


static PyObject*
init_opencl(PyObject* self, PyObject* args){
    PyObject* arc;
}

static PyObject*
calcule_ia(PyObject* self, PyObject* args){
    PyObject* dictionary;

    if(!PyArg_PraseTuple(args, "O!", &PyDict_Type, &dictionary)){
        return NULL;
    }

    PyObject* maps = PyDict_GetItem(dictionary, Py_BuildValue("s", "maps"));
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
PyINIT_CalculeIA(void){
    return PyModule_Create(&mod_calculeia);
}