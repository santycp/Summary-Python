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

#Are special methods which have double underscores at the beginning and end of their names.
#They are used to create functionality that can't be represented as a normal method.

'''
One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such as + and * to be used on them. 
'''
#An example magic method is __add__ for +.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x) #8
print(result.y) #16

#More magic methods for common operators:
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |

#The expression x + y is translated into x.__add__(y).

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello) #spam
                    #============
                    #Hello world!

#Python also provides magic methods for comparisons.
#__lt__ for <
#__le__ for <=
#__eq__ for ==
#__ne__ for !=
#__gt__ for >
#__ge__ for >=

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs
'''
>spam>eggs
e>spam>ggs
eg>spam>gs
egg>spam>s
eggs>spam>

'''

#There are several magic methods for making classes act like containers.
#__len__ for len()
#__getitem__ for indexing
#__setitem__ for assigning to indexed values
#__delitem__ for deleting indexed values
#__iter__ for iteration over objects (e.g., in for loops)
#__contains__ for in

import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))#0
print(len(vague_list))#9
print(vague_list[2])#B
print(vague_list[2])#D


#------ Object Lifecycle ------

#is made up of its creation, manipulation, and destruction.

#The first stage of the life-cycle of an object is the definition of the class to which it belongs.
#The next stage is the instantiation of an instance, when __init__ is called.
'''
Memory is allocated to store the instance. Just before this occurs, the __new__ method of the class is called. 
This is usually overridden only in special cases. 
'''
#After this has happened, the object is ready to be used.
#----------!!!!
#The del statement reduces the reference count of an object by one, and this often leads to its deletion.
#The magic method for the del statement is __del__.

#------ DATA HIDING ------

'''
A key part of object-oriented programming is encapsulation, which involves packaging of related variables and functions 
into a single easy-to-use object - an instance of a class.
A related concept is data hiding, which states that implementation details of a class should be hidden, and a clean 
standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes, which block external access to 
certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all consenting adults here", meaning that you
shouldn't put arbitrary restrictions on accessing parts of a class. Hence there are no ways of enforcing a method or 
attribute be strictly private. 
'''

#Weakly private methods and attributes have a single underscore at the beginning.
#However, it is mostly only a convention, and does not stop external code from accessing them

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue) #Queue([1, 2, 3])
queue.push(0)
print(queue) #Queue([0, 1, 2, 3])
queue.pop()
print(queue)#Queue([0, 1, 2])
print(queue._hiddenlist) #[0, 1, 2]

#-------------------------------------

#Strongly private methods and attributes have a double underscore at the beginning of their names
#which means that they can't be accessed from outside the class.

'''
Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam
could be accessed externally with _Spam__privatemethod
'''

#------ CLASS METHODS ------

#Class methods are different - they are called by a class, which is passed to the cls parameter of the method.

#A common use of these are factory methods, which instantiate an instance of a class, using different parameters than
#those usually passed to the class constructor.

#Class methods are marked with a classmethod decorator.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())


#------- Static Methods ------
'''
Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to 
normal functions that belong to a class.
They are marked with the staticmethod decorator. 
'''

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


#------ Properties -------

#Properties can also be set by defining setter/getter functions.

#The setter function sets the corresponding property's value. (establece el valor)

#The getter gets the value.(obtiene el valor)

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)