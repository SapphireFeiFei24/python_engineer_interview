/***
Tuple: Immutable List
- Fixed size, no resize
- Slightly more memory-efficient
- Fater iteration

Why faster
- No capacity tracking
- No mutable checks
- Hashable(can be used for dict key)
***/

typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];  // actually variable length
} PyTupleObject;
