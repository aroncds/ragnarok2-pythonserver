#include "hm/heightmap.h"
#include <stdio.h>
#include <stdlib.h>

double
det(double a, double b, double c, double d, double e, double f, double g, double h, double i){
    return a * e * i + b * f * g + c * d * h - c * e * g - f * h * a - i * b * d;
}

double
z(double a1, double a2, double a3, double b1, double b2, double b3, double c1, double c2, double c3, double x, double y){

    return (det(a1, b1, c1, a2, b2, c2, a3, b3, c3) - x * det(a2, b2, c2, a3, b3, c3, 1, 1, 1)
    + y * det(a1, b1, c1, a3, b3, c3, 1, 1, 1)) / det(a1, b1, c1, a2, b2, c2, 1, 1, 1);
}

static PyObject*
LoadHeightMap(PyObject* self, PyObject* args){
	char *src;
	int maxX, maxY;

	if(!PyArg_ParseTuple(args, "sii", &src, &maxX, &maxY)){
		printf("iii falho");
		return NULL;
	}

	HeightMap* hm;
	FILE* file;

	printf("%s\n", src);

	file = fopen(src, "r");

	if (!file){
		printf("Teste\n");
		return NULL;
	}

	printf("cole brow\n");

	hm = (HeightMap*)calloc(sizeof(HeightMap), 1);
	hm->maxX = maxX;
	hm->maxY = maxY;

	hm->heightdata = (float**)calloc(sizeof(float), maxY);

	int i=0, a=0;

	for(i = 0; i < maxY; i++){
		hm->heightdata[i] = (float*)calloc(sizeof(float), maxX);
		for(a = 0; a < maxX; a++){
			hm->heightdata[i][a] = 0;
		}
	}

	return PyHeightMap_FromHeightMap(hm, 1);
}

static PyObject*
GetZHeightMap(PyObject* self, PyObject* args){
	PyObject* pmap;
	float z = 0;

	if(!PyArg_ParseTuple(args, "O", &pmap)){
		return NULL;
	}

	HeightMap* hm = PyHeightMap_AsHeightMap(pmap);

	printf("hehee\n");
	printf("%d", hm->maxX);

	return Py_BuildValue("f", z);
}

static PyMethodDef heightmap_methods[] = {
	{"load", LoadHeightMap, METH_VARARGS, "Carregar HeightMap"},
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

_HeightMapAPIMethods _heightmap_api = {
	PyHeightMap_AsHeightMap,
	PyHeightMap_FromHeightMap,
};

PyMODINIT_FUNC
PyInit_heightmap(void){
	PyObject* m = PyModule_Create(&heightmap_module);
	PyObject* py_heightmap_api;

	if (m == NULL)
		return m;

	py_heightmap_api = PyCapsule_New((void *) &_heightmap_api, "heightmap._heightmap_api", NULL);

	if(py_heightmap_api){
		PyModule_AddObject(m, "_heightmap_api", py_heightmap_api);
	}

	return m;
}
