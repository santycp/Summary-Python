#------- Functional Programming -------
#Higher-order functions take other functions as arguments, or return them as results.
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10)) #20

#Pure Functions

#Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that
#depends only on their arguments.

#Pure function:

def pure_function(x, y):

  temp = x + 2*y

  return temp / (2*x + y)

#Impure function:

some_list = []

def impure(arg):

  some_list.append(arg)

#------ LAMBDAS ------


def my_func(f, arg):

  return f(arg)

my_func(lambda x: 2*x*x, 5)

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#Lambda functions can be assigned to variables, and used like normal functions
double = lambda x: x * 2
print(double(7)) #14

#------ MAP -------
'''
The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects 
called iterables).
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to 
each argument. 
'''

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result) #16, 27, 38, 49, 60]

#We could have achieved the same result more easily by using lambda syntax.
result = list(map(lambda x: x+5, nums))
print(result) #[16, 27, 38, 49, 60]

#------ FILTER -------
#The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res) #[22, 44]

#NOTE: Like map, the result has to be explicitly converted to a list if you want to print it.

#------ GENERATORS -------

# are a type of iterable, like lists or tuples.
'''
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
They can be created using functions and the yield statement. 
'''

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)


#allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

#Finite generators can be converted into lists by passing them as arguments to the list function.
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11))) #[0, 2, 4, 6, 8, 10]

'''
Using generators results in improved performance, which is the result of the lazy (on demand) generation of values,
which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been generated
before we start to use them. 
'''


#------ DECORATORS ------

'''
Decorators provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions that you don't want to modify. 
'''

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

#NOTE:print_text corresponds to our decorated version.

'''
Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name
and the @ symbol.
'''

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text();

#NOTE: A single function can have multiple decorators.

#------ RECURSION -------

'''
The fundamental part of recursion is self-reference - functions calling themselves. It is used to solve problems that 
can be broken up into easier sub-problems of the same type. 
'''

def factorial(x):
    if x == 1:
        return 1  #case base
    else:
        return x * factorial(x-1)

print(factorial(5))

#NOTE: The "base case" acts as the exit condition of the recursion.

#Recursive functions can be infinite, just like infinite while loops. These often occur when you forget to implement
# the base case.

def factorial(x):
    return x * factorial(x-1)

print(factorial(5))

'''
Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on.
This can occur with any number of functions.
'''
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(17)) #True
print(is_even(23)) #False

#------ SETS -------
'''
They are created using curly braces, or the set function. They share some functionality with lists, such as the use of 
in to check whether they contain a particular item.
'''
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set) #True
print("spam" not in word_set)#False

#NOTE: To create an empty set, you must use set(), as {} creates an empty dictionary.

#Sets differ from lists in several ways, but share several list operations such as len.
#They are unordered, which means that they can't be indexed.
#They cannot contain duplicate elements.
#Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
#Instead of using append to add to a set, use add.
#The method remove removes a specific element from a set; pop removes an arbitrary element

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums) #{1, 2, 3, 4, 5, 6}
nums.add(-7)
nums.remove(3)
print(nums) #{1, 2, 4, 5, 6, -7}

#Basic uses of sets include membership testing and the elimination of duplicate entries.


'''
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both. 
'''

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) #{4, 5, 6}
print(first - second) #{1, 2, 3}
print(second - first) #{8, 9, 7}
print(first ^ second) #{1, 2, 3, 7, 8, 9}


#------ FIBONACCI   -------


num = int(input())


def fibonacci(n):
    if n <= 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

for i in range(num):
    print(fibonacci(i + 1))



