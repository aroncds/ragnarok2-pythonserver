#include <Python.h>

#ifndef HEIGHTMAP
#define HEIGHTMAP

typedef struct HeightMap{
	int maxX;
	int maxY;
	float** heightdata;
} HeightMap;

typedef struct {
	HeightMap* (*aspoint)(PyObject*);
	PyObject* (*frompoint)(HeightMap* ,int);
} _HeightMapAPIMethods;

void del_HeightMap(PyObject* obj);
HeightMap* PyHeightMap_AsHeightMap(PyObject* obj);
PyObject* PyHeightMap_FromHeightMap(HeightMap* p, int must_free);
PyObject* py_HeightMap(PyObject* self, PyObject* args);

#endif