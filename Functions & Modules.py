#------ FUNCTIONS ----
#you can create your own functions by using the def statement.
def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()

#You can also define functions with more than one argument; separate them with commas.

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)
print_sum_twice(5, 8)

#--- Returning from Functions---
#Certain functions, such as int or str, return a value that can be used later.
#To do this for your defined functions, you can use the return statement.

#----------------------------------------------
#Although they are created differently from normal variables, functions are just like any other kind of value.
#They can be assigned and reassigned to variables, and later referenced by those names.
def multiply(x, y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b)) #28

#Functions can also be used as arguments of other functions.
def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b)) #30

'''
MODULES 

There are three main types of modules in Python, those you write yourself, those you install from external sources, and those that are preinstalled with Python.
The last type is called the standard library, and contains many useful modules. Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

Tasks that can be done by the standard library include string parsing, data serialization, testing, debugging and manipulating dates, emails, command line arguments, and much more!


Many third-party Python modules are stored on the Python Package Index (PyPI). 
The best way to install these is using a program called pip
Using pip is the standard way of installing libraries on most operating systems, but some libraries have prebuilt binaries for Windows
 
'''

'''
EXCERCISE 
You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.
'''

celsius = int(input())


def conv(c):
    # your code goes here
    res = 9 / 5 * c + 32
    return res


fahrenheit = conv(celsius)
print(fahrenheit)