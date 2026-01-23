/***
Python ints are not fixed-width

- No overflow
- Addtion O(n)
- Multiplication: Karatsuba / FFT for large numbers

Slower but safer than Cpp
***/

typedef struct {
    PyObject_HEAD
    Py_ssize_t ob_size;
    digit ob_digit[1];  // base 2^30
} PyLongObject;
