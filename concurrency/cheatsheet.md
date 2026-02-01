# Concurrency in Python
## GIL (Global Interpreter Lock)
> A mutex that allows only one thread to execute Python bytecode at a time \
> Exists in CPython
### Why
* Simpler memory management
* Faster single-threaded performance

### Consequences
* I/O-bound tasks benefit from threading
* CPU-bound tasks may not see performance gains with threading, need multiprocessing

### GIL is Released When
* I/O operations (file, network)
* Some C extensions (e.g., NumPy, PyTorch)

## Multi Threading
> Use for I/O-bound tasks
```python
from threading import Thread

def task():
    ...

t = Thread(target=task)
t.start()
t.join() # main thread waiting for result
```

### Race Conditions
> Can still happen when GIL is released

#### Use Locks to Prevent
```python
from threading import Thread, Lock
lock = Lock()
counter = 0
def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
threads = [Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)  # Should be 500000
```


#### Thread-Safe Data Structures
* `queue.Queue()`

#### Semaphores
> Limit access to a resource, only `value` number of threads can access at once
```python
import threading
import time
import random

# Create a semaphore that allows up to 3 threads to access the resource simultaneously
semaphore = threading.Semaphore(value=3)

def access_resource(thread_id):
    print(f"Thread {thread_id} is trying to acquire the semaphore.")
    with semaphore:
        # Critical section: only 3 threads can be in this block at once
        print(f"Thread {thread_id} has acquired the semaphore and is accessing the resource.")
        time.sleep(random.randint(1, 3)) # Simulate work
        print(f"Thread {thread_id} is releasing the semaphore.")
    # The semaphore is automatically released here

# Create and start multiple threads
threads = []
for i in range(1, 10):
    t = threading.Thread(target=access_resource, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads have finished.")
```
### AsyncIO
> Single-threaded, single-process design \
> Using asynchronous coroutines and non-blocking operations
> Cheaper than threads/processes
> Ideal for I/O-bound tasks

## Multi Processing
> * Each process has its own GIL
> * Uses multiple CPU cores
> * Used for CPU-bound tasks
> * Higher memory usage than threading
```python
import multiprocessing
# Function to square a number
def square(x):
    return x * x

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a multiprocessing pool
with multiprocessing.Pool() as pool:
    # Use the map method to apply the 'square ' function to each number in parallel
    results = pool.map(square, numbers)
# Print the results
print(results)
```

## Future
> `ThreadPoolExecutor` for I/O-bound tasks \
> `ProcessPoolExecutor` for CPU-bound tasks
```python
import concurrent.futures
import time

def task(name):
    time.sleep(1) # Simulate I/O work
    return f"Task {name} completed"

# Use ThreadPoolExecutor for I/O-bound tasks
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(5)]

    # Process results as they complete
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

```