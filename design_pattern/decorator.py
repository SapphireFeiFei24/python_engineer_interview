'''
Definition:
Attach additional responsiblities to an object dynamically.
Provides a flexible alternative to subclassing for extending functionality

Use when there're reusuable codes that are orthogonal to the core purpose of the function
'''
from collections import OrderedDict
from functools import wraps


# one extra layer to take param for the decorator itself
def my_lru_cache(maxsize=128):
    def decorator(func):
        cache = OrderedDict()  # maintains insertion for order (used for LRU)

        @wraps(func)  # this is to keep the meta data for original func
        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)
                return cache[args]
            result = func(*args)
            cache[args] = result # always append to the end
            # print(f"args={args} curr_cache_size={len(cache)}")
            if len(cache) > maxsize:
                cache.popitem(last=False)  # pop the front(oldest) item
            return result
        return wrapper
    return decorator


@my_lru_cache(maxsize=3)
def add(a, b):
    print(f"computing {a} + {b}...")
    return a + b


if __name__ == "__main__":
    print(add(1, 2))  # Computed
    print(add(1, 2))  # Cached
    print(add(2, 3))  # Computed
    print(add(3, 4))  # Computed
    print(add(4, 5))
    print(add(1, 2))
