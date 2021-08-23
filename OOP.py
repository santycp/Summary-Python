#------ CLASESS ------

#Objects are created using classes, which are actually the focal point of OOP.
'''
Objects are created using classes, which are actually the focal point of OOP.
The class describes what the object will be, but is separate from the object itself(en si). In other words, a class can be
described as an object's blueprint (plano del objeto), description, or definition.
'''

#sintaxis

class Cat:

  def __init__(self, color, legs):

    self.color = color

    self.legs = legs



felix = Cat("ginger", 4)

rover = Cat("dog-colored", 4)

stumpy = Cat("brown", 3)

#------ __init__ ------

#This is called when an instance (object) of the class is created, using the class name as a function

#All methods must have self as their first parameter
#self refers to the instance calling the method.
#Instances of a class have attributes, which are pieces of data associated with them.
#These can be accessed by putting a dot, and the attribute name after an instance.
#In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.

#------ Methods ------

#Classes can have other methods defined to add functionality to them.
#These methods are accessed using the same dot syntax as attributes.

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name) #Fido
fido.bark() #Woof!

'''
Classes can also have class attributes, created by assigning variables within the body of the class. These can be 
accessed either from instances of the class, or the class itself. 
'''

class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs) #4
print(Dog.legs)  #4

#------ Inheritance ------

#provides a way to share functionality between classes.

#To inherit a class from another class, put the superclass name in parentheses after the class name

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color) #brown
fido.bark() #Woof!


#A class that inherits from another class is called a subclass.
#A class that is inherited from is called a superclass.
#If a class inherits from another with the same attributes or methods, it overrides them.
#(Si una clase hereda de otra con los mismos atributos o métodos, los reemplaza)

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark() #Woof
#Wolf is the superclass, Dog is the subclass.

#Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class.

class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method() #A method
c.another_method() #B method
c.third_method() #C method

'''
The function super is a useful inheritance-related function that refers to the parent class. It can be used to find the
method with a certain name in an object's superclass.
'''

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()
            #2
            #1

#------- MAGIC METHODS -------