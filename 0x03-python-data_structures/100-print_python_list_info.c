#include <Python.h>

/**
* print_python_list_info - Prints basic data about Python lists.
* @p: A PyObject list.
*/
void print_python_list_info(PyObject *p)
{
int size, alloc, i;
PyObject *obj;
size = Py_SIZE(p);
alloc = ((PyListObject *)p)->allocated;printf("[*] Size of the Python List = %d\n", size);
for (i = 0; i < size; i++)
{
printf("Element %d: ", i);
obj = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
}
