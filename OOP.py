import abc
from abc import ABC

class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class Pet(ABC):
    age = NonNegative()
    __default_name = 'default name'
    __default_master = 'default master'
    def __init__(self, name, age, master):
        self.__name = name if not name is None else self.__default_name
        self.age = age
        self.__master = master if not master is None else self.__default_master
    def jump(self):
        print(f"jump")
    def run(self):
        print(f"run")
    def birthday(self):
        self.age += 1
    def sleep(self):
        print(f"sleep")
    @property
    def master(self):
        return self.__master
    @master.setter
    def master(self, value):
        if value is None:
            self.__master = self.__default_master
        else:
            self.__master = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value is None:
            value = self.__default_name
        else:
            self.__name = value
    @abc.abstractmethod
    def voice(self):
        pass

#HT_14_1
class Dog(Pet):
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        Pet.__init__(self, name, age, master)
    def __bark(self):
        print(f"bark")
    def change_name(self, new_name):
        self.name = new_name
    def voice(self):
        self.__bark()

dog  = Dog(1,2,'Dog', 4, None)
dog.jump()
dog.run()
dog.voice()
dog.sleep()
print(dog.height)
print(dog.weight)
print(dog.name)
print(dog.age)
print(dog.master)

#HT14_2
dog.change_name('New_dog')
print(dog.name)

#14.5
class Cat(Pet):
    def __init__(self, name, age, master):
        Pet.__init__(self, name, age, master)
    def __meow(self):
        print(f"meow")
    def voice(self):
        self.__meow()

class Parrot(Pet):
    def __init__(self, name, age, master):
        Pet.__init__(self, name, age, master)
    def fly(self):
        print(f"fly")
    def voice(self):
        print(f"piu")



#14.6
cat = Cat(None, 1, 'Cat_human')
print(cat.name)
cat.voice()
cat.jump()
cat.run()
cat.birthday()
print(cat.age)

parrot = Parrot("Parrot", 2, 'Parrot_human')
parrot.fly()
parrot.jump()
parrot.voice()
parrot.run()
parrot.birthday()
print(parrot.age)
