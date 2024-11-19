from abc import ABC, abstractmethod
class xyz(ABC):
    def print(self, x):
        print(x)
    def task(self):
        print("We are inside xyz class.")
class test(xyz):
    def task(self):
        print("We are inside test class.")
obj= test()
obj.task()
obj.print(15)