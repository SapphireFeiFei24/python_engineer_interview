/***
Extremely optimized: Compact + (Insertion) Ordered(since p3.6)

Two arrays
- indices(hash table)
- entries(actual key/value storage)

Why fast:
Open addressing(no linked list)
Load factor kept low
Excellent cache locality
Hash stored alongside key

Lookup O(1)
Resize O(n)
***/
typedef struct {
    PyObject *me_key;
    PyObject *me_value;
    Py_hash_t me_hash;
} PyDictKeyEntry;

typedef struct {
    Py_ssize_t dk_size;
    PyDictKeyEntry *dk_entries;
    char *dk_indices;   // sparse hash table
} PyDictKeysObject;

T lookup(key) {
    i = hash & mask;
    while (indices[i] != EMPTY) {
        if (entries[indices[i]].key == key)
            return value;
        i = (i + 1) & mask;  // open addressing
    }

}


