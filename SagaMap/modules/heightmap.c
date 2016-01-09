#include <Python.h>
#include <stdio.h>
#include <stdlib.h>


typedef struct HeightMap{
	int maxX;
	int maxY;
	float** heightdata;
} HeightMap;

static PyObject*
LoadHeightMap(PyObject* self, PyObject* args){
	HeightMap* heightmap;
	FILE* file;
	char *src;
	int maxX, maxY;

	if(!PyArg_ParseTuple(args, "sii", &src, &maxX, &maxY)){
		return NULL;
	}

	file = fopen(src, "r");

	if (!file){
		return NULL;
	}

	heightmap = (HeightMap*)calloc(sizeof(HeightMap), 1);
	heightmap->maxX = maxX;
	heightmap->maxY = maxY;

	heightmap->heightdata = (float**)calloc(sizeof(float), maxY);

	int i=0, a=0;

	for(i = 0; i < maxY; i++){
		heightmap->heightdata[i] = (float*)calloc(sizeof(float), maxX);
		for(a = 0; a < maxX; a++){
			heightmap->heightdata[i][a] = 0;
		}
	}

	return NULL;
}

static PyObject*
GetZHeightMap(PyObject* self, PyObject* args){
	PyObject* heightmap;
	float z = 0;

	if(!PyArg_ParseTuple(args, "!0", &PyDict_Type, heightmap)){
		return NULL;
	}

	return Py_BuildValue("f", z);
}

static PyMethodDef heightmap_methods[] = {
	{"loadheightmap", LoadHeightMap, METH_VARARGS, "Carregar HeightMap"},
	{"getz", GetZHeightMap, METH_VARARGS, "Get Z"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef heightmap_module ={
	PyModuleDef_HEAD_INIT,
	"heightmap",
	"Doc",
	-1,
	heightmap_methods
};

PyMODINIT_FUNC
PyInit_heightmap(void{
	return PyModule_Create(&heightmap_module);
}