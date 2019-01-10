## Animal is-a object. pass is a way to continue without python giving you an error
class Animal(object):
    pass

## Dog is-a Animal that has-a function with parameters self and name
class Dog(Animal):

    def __init__(self, name):
        ## from self get the name attribute and set it to name (dog has-a attribute named name)
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## from self get the name attribute and set it to name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## from self get the name attribute and set it to name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person that has a function with parameters self, name, and salary
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## from self get the salary attribute and set it to salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary get attribute pet and set it to satan
mary.pet = satan

## frank is an Employee with parameters 120000
frank = Employee("Frank", 120000)

## from frank get attribute pet and set it to rover
frank.pet = rover

## set flipper to Fish
flipper = Fish()

## set crouse to Salmon
crouse = Salmon()

## set harry to Halibut()
harry = Halibut
