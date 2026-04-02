class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.__master = master
    def jump(self):
        print(f"jump")
    def run(self):
        print(f"run")
    def birthday(self):
        self.age += 1
    def sleep(self):
        print(f"sleep")
    def get_master(self):
        return self.__master

#HT_14_1
class Dog(Pet):
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        Pet.__init__(self, name, age, master)

    def bark(self):
        print(f"bark")
    def change_name(self, new_name):
        self.name = new_name
dog  = Dog(1,2,'Dog', 4, 'Human')
dog.jump()
dog.run()
dog.bark()
dog.sleep()
print(dog.height)
print(dog.weight)
print(dog.name)
print(dog.age)

#HT14_2
dog.change_name('New_dog')
print(dog.name)

#14_4
print(dog.get_master())

#14.5
class Cat(Pet):
    def __init__(self, name, age, master):
        Pet.__init__(self, name, age, master)
    def meow(self):
        print(f"meow")

class Parrot(Pet):
    def __init__(self, name, age, master):
        Pet.__init__(self, name, age, master)
    def fly(self):
        print(f"fly")



#14.6
cat = Cat("Cat", 1, 'Cat_human')
cat.meow()
cat.jump()
cat.run()
cat.birthday()
print(cat.age)

parrot = Parrot("Parrot", 2, 'Parrot_human')
parrot.fly()
parrot.jump()
parrot.run()
parrot.birthday()
print(parrot.age)
