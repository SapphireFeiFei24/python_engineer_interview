/***
import collections.deque

Deque is not a linked list of single nodes, instead
- Linked list of fixed-size blocks
- Each block contains multiple pointers
- Optimizes cache locality meanwhile keepig O(1) ends

- O(1) left right append
- O(1) left right pop
- O(n) random access
***/

#define BLOCKLEN 64

typedef struct BLOCK {
    struct BLOCK *left;
    struct BLOCK *right;
    PyObject *data[BLOCKLEN];
} block;

typedef struct {
    PyObject_HEAD
    block *leftblock;
    block *rightblock;
    Py_ssize_t leftindex;
    Py_ssize_t rightindex;
} dequeobject;

