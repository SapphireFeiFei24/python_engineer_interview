/***
Dynamic array

High level
- Continuous array of pointers(PyObject*)
- Over allocate to prevent frequence alloc
- O(1) append(amortized after resize)
- O(1) pop at the end
- O(n) pop in the front
- O(n) delete/insert in the middle
***/

typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;   // array of PyObject*
    Py_ssize_t allocated; // allocated capacity
} PyListObject;

static int
list_resize(PyListObject *self, Py_ssize_t newsize) {
    Py_ssize_t new_allocated = newsize + (newsize >> 3) + 6;
    self->ob_item = realloc(self->ob_item,
                             new_allocated * sizeof(PyObject *));
    self->allocated = new_allocated;
}
