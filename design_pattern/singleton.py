'''
Ensure a class has only one instance and provides a global point of access to it
'''

# Approach 1: using a class variable
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, param):
        if not self.__initialized:
            self.param = param
            # guarantee param is used only at first time initialization
            self.__initialized = True

s1 = Singleton("s1")
s2 = Singleton("s2")
print(s2.param)


# Approach 2: use decorator
def singleton(cls):
    """
    Call only once during the class declaration.
    cls = get_instance -> instance(same lifetime with cls)
    :param cls:
    :return:
    """
    instance = None
    def get_instance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return get_instance

@singleton
class SingletonClass:
    def __init__(self, param):
        self.param = param

d1 = SingletonClass("d1")
d2 = SingletonClass("d2")
print(d2.param)
d2.param = "d2"
print(d1.param)

# Approach 3: meta class
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MySingleton(metaclass=SingletonMeta):
    def __init__(self, param):
        self.param = param

x = MySingleton("x")
y = MySingleton("y")
print(y.param)
