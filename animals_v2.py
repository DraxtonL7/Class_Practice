"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.
After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.
"""


class Animal:
    def __init__(self):
        print("Animal constructed...")

    def move(self):
        print("moves on its own...")

    def eat(self):
        print("The animal eats...")


class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(self)
        self.name = name
        self.age = age

    def move(self):
        print(self.name + " runs on all fours like a good dog...")

    def eat(self):
        return super().eat()


class Fish(Animal):
    def __init__(self, name, age):
        Animal.__init__(self)
        self.name = name
        self.age = age

    def move(self):
        print(self.name + " swims like the fastest fishy...")

    def eat(self):
        return super().eat()


class Bird(Animal):
    def __init__(self, name, age):
        Animal.__init__(self)
        self.name = name
        self.age = age

    def move(self):
        print(self.name + " soars through the sky with wind in its feathers...")

    def eat(self):
        return super().eat()


d1 = Dog("Bruno", 17)
d1.move()
d1.eat()
print()
f1 = Fish("Nemo", 3)
f1.move()
f1.eat()
print()
b1 = Bird("Polly", 83)
b1.move()
b1.eat()