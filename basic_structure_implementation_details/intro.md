# Introduction
## Python Object
> Python objects are heap-allocated C struct managed by CPython
> Everything is a pointer to PyObject
```C
typedef struct _object {
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
} PyObject;
```

## Everything is a pointer
* Aliasing bugs
* copy() matters
* Mutable defaults are dangerous