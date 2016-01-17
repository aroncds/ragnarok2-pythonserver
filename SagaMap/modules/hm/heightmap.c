#include "heightmap.h"

void del_HeightMap(PyObject* obj){
	free(PyCapsule_GetPointer(obj, "HeightMap"));
}

HeightMap* PyHeightMap_AsHeightMap(PyObject* obj){
	return (HeightMap*)PyCapsule_GetPointer(obj, "HeightMap");
}

PyObject* PyHeightMap_FromHeightMap(HeightMap* p, int free){
	return PyCapsule_New(p, "HeightMap", free ? del_HeightMap : NULL);
}

PyObject* py_HeightMap(PyObject* self, PyObject* args){
	int x, y;

	if(PyArg_ParseTuple(args, "ii", &x, &y)){
		return NULL;
	}

	HeightMap* m = (HeightMap*)malloc(sizeof(HeightMap));
	m->maxX = x;
	m->maxY = y;

	return PyHeightMap_FromHeightMap(m, 1);
}