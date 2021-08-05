'''
------ Exceptions ---------

Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
'''

#------ Exception Handling ------

#To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
#The try block contains code that might throw an exception.

try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

#A try statement can have multiple different except blocks to handle different exceptions.

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")

#An except statement without any exception specified will catch all errors.

try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

#----- finally -----
#To ensure some code runs no matter what errors occur, you can use a finally statement.

try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

#Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks.

try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last")

#------ Raising Exceptions -------
#You can raise exceptions by using the raise statement.
print(1)
raise ValueError
print(2)

#Exceptions can be raised with arguments that give detail about them.

name = "123"
raise NameError("Invalid name!")

#In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.

try:
    num = 5 / 0
except:
    print("An error occurred")
    raise

#------ ASERTIONS ------

#An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
#An expression is tested, and if the result comes up false, an exception is raised.
#Assertions are carried out through use of the assert statement.

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

#The assert can take a second argument that is passed to the AssertionError raised if the assertion fails.
temp = -10
assert (temp >= 0), "Colder than absolute zero!"

#------ OPEN FILES ------

#You can use Python to read and write the contents of files

#sintaxis

myfile = open("filename.txt")

#You can specify the mode used to open a file by applying a second argument to the open function.
'''
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file. 

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files). 
'''

#NOTE:
#You can use the + sign with each of the modes above to give them extra access to files. For example,
# r+ opens the file for both reading and writing.

#Once a file has been opened and used, you should close it.
#This is done with the close method of the file object.
#This is done with the close method of the file object.
file = open("filename.txt", "w")

# do stuff to the file

file.close()

#------ Reading Files ------
#he contents of a file that has been opened in text mode can be read using the read method.

file = open("filename.txt", "r")

cont = file.read()
print(cont)

file.close()

#This will print all of the contents of the file "filename.txt".

'''
To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file. 
'''
file = open("filename.txt", "r")

print(file.read(16))

print(file.read(4))

print(file.read(4))

print(file.read())

file.close()

#Just like passing no arguments, negative values will return the entire contents.

#----- Writing Files ------

#To write to files you use the write method, which writes a string to the file.
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()
#The "w" mode will create a file, if it does not already exist.
#When a file is opened in write mode, the file's existing content is deleted.

'''
Book Titles

You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line. 
'''

lis=[]
for i in file:
    lis.append(i)

for j in lis:
    if j[-1] == '\n':
        print(j[0] + str(len(j)-1))
    else:
        print(j[0] + str(len(j)))

file.close()