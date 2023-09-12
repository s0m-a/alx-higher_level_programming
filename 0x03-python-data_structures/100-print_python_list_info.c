#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints some info about list
 * @p: pointer to PyObject struct
 */

void print_python_list_info(PyObject *p)
{
	int i;
	int size = PyList_Size(p);
	int allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, ((PyList_GetItem(p, i))->ob_type)->tp_name);
	}
}
