#!/bin/python3

# ex42: Is-A, Has-A, Objects, and Classes

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    def speak(self):
        print("I'm an animal")

# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

    def speak(self):
        print("I'm " + self.name)

# Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # run the __init__ method of a parent class reliably
        #self.__init__(name)
        # super is a way to call parent but better than using the name of class.
        #super().__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a fish
class Halibut(Fish):
    pass


class Policy(Animal, Person):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary's pet is satan
mary.pet = satan

# frank is-a Employee, his salary is 120000
frank = Employee("Frank", 120000)

# frank's pet is rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()


bow = Dog('bow')
bow.speak()

brother = Policy('jaebum')
brother.speak()