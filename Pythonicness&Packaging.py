import this

#------ FUCTION ARGUMENTS -------

'''
Python allows to have function with varying number of arguments.
Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments
are then accessible as the tuple args in the body of the function. 
'''

def function(named_arg, *args):
    print(named_arg) #1
    print(args) #(2, 3, 4, 5)

function(1, 2, 3, 4, 5)

#The parameter *args must come after the named parameters to a function.
#The name args is just a convention; you can choose to use anothe

#------ Default Values ------

'''
Named parameters to a function can be made optional by giving them a default value.
These must come after named parameters without a default value.
'''

def function(x, y, food="spam"):
    print(food)

function(1, 2) #spam
function(3, 4, "egg") #egg

#In case the argument is passed in, the default value is ignored.
#If the argument is not passed in, the default value is used.

#------ Function Arguments ------
'''
**kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values. 
'''
def my_func(x, y=7, *args, **kwargs):
    print(kwargs) #{'a': 7, 'b': 8}

my_func(2, 3, 4, 5, 6, a=7, b=8)

#The arguments returned by **kwargs are not included in *args.


#------ Tuple Unpacking -------

#Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.

numbers = (1, 2, 3)
a, b, c = numbers
print(a) #1
print(b) #2
print(c) #3

'''
This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the tuple (b, a) 
which is then unpacked.
'''

'''
Una variable que está precedida por un asterisco (*) toma todos los valores del iterable que quedan de las otras variables. 
'''
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) #1
print(b) #2
print(c) #[3, 4, 5, 6, 7, 8]
print(d) #9

#------ Ternary Operator ------

'''
Conditional expressions provide the functionality of if statements while using less code. They shouldn't be overused, as they can easily reduce readability, but they are often useful when assigning variables.
Conditional expressions are also known as applications of the ternary operator. 
'''

a = 4
b = 1 if a >= 5 else 42
print(b) #42

#The ternary operator checks the condition and returns the corresponding value.

status  = 1
msg = "Logout" if status == 1 else "Login"

print(msg) #Logout

#The ternary operator is so called because, unlike most operators, it takes three arguments. !!!!!


#------ ELSE -------

"""
The else statement is most commonly used along with the if statement, but it can also follow a for or while loop, which gives it a different meaning.
With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop). 
"""

for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

"""
The else statement can also be used with try/except statements.
In this case, the code within it is only executed if no error occurs in the try statement. 
"""

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

#------ __main__ ------

"""
Most Python code is either a module to be imported, or a script that does something.
However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
To do this, place script code inside if __name__ == "__main__".
This ensures that it won't be run if the file is imported. 
"""
