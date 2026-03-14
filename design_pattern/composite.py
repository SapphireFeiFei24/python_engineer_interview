'''
Definition
Treat individual objects and compositions of objects uniformly
Representint part-whole hierarchies, i.e. tree structures
'''

from abc import ABC, abstractmethod

# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + f"File: {self.name}")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent=0):
        print(' ' * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 4)

# Client code
if __name__ == "__main__":
    root = Directory("root")
    file1 = File("file1.txt")
    file2 = File("file2.txt")

    folder1 = Directory("folder1")
    folder1.add(File("file3.txt"))
    folder1.add(File("file4.txt"))

    folder2 = Directory("folder2")
    folder2.add(File("file5.txt"))

    root.add(file1)
    root.add(file2)
    root.add(folder1)
    root.add(folder2)

    root.display()
