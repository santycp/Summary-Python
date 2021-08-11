#------- NONE -------
#The None object is used to represent the absence of a value.

#The None object is returned by any function that doesn't explicitly return anything else.

def some_func():
    print("Hi!")

var = some_func()
print(var) # Hi! None

#------- Dictionaries -------
# are data structures used to map arbitrary keys to values.

#Dictionaries can be indexed in the same way as lists, using square brackets containing keys

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"]) #24
print(ages["Mary"]) #42

#Each element in a dictionary is represented by a key:value pair.

#Trying to index a key that isn't part of the dictionary returns a KeyError. ********

#Only immutable objects can be used as keys to dictionaries
bad_dict = {
    [1, 2, 3]: "one two three",
} #TypeError: unhashable type: 'list'

#Just like lists, dictionary keys can be assigned to different values.
#However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares) #{1: 1, 2: 4, 3: 9, 4: 16, 8: 64}

#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums) # True
print("three" in nums) #False
print(4 not in nums) #True

#A useful dictionary method is get. It does the same thing as indexing, but if the key is not found in the dictionary it
# returns another specified value instead ('None', by default).
pairs = {1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}

print(pairs.get("orange")) #[2, 3, 4]
print(pairs.get(7)) #None
print(pairs.get(12345, "not in dictionary")) #not in dictionary

#------ TUPLES ------

#Tuples are very similar to lists, except that they are immutable
#they are created using parentheses, rather than square brackets.

words = ("spam", "eggs", "sausages",)

#access the values in the tuple with their index, just as you did with lists:
print(words[0]) #spam

#Trying to reassign a value in a tuple causes a TypeError.

#Like lists and dictionaries, tuples can be nested(anidar) within each other.

#Tuples can be created without the parentheses, by just separating the values with commas.

my_tuple = "one", "two", "three"
print(my_tuple[0]) #one

#An empty tuple is created using an empty parenthesis pair.

#Tuples are faster than lists, but they cannot be changed.****

#------- LIST SLICES ------

'''
List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list
With two colon-separated integers (dos enteros separados por dos puntos). This returns a new list containing all the values in the old list between the indices. 
'''
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) #[4, 9, 16, 25]
print(squares[3:8])#[9, 16, 25, 36, 49]
print(squares[0:1])#[0]

#NOTE : Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't

#If the first number in a slice is omitted, it is taken to be the start of the list.

print(squares[:7]) #[0, 1, 4, 9, 16, 25, 36]
print(squares[7:]) #[49, 64, 81]

# List slices can also have a third number, representing the step, to include only alternate values in the slice.

print(squares[::2]) #[0, 4, 16, 36, 64]
print(squares[2:8:3]) #[4, 25]

"""
Negative values can be used in list slicing (and normal list indexing). When negative values are used for the first and 
second values in a slice (or a normal index), they count from the end of the list. 
"""
print(squares[1:-1])#[1, 4, 9, 16, 25, 36, 49, 64]

#If a negative value is used for the step, the slice is done backwards.
#Using [::-1] as a slice is a common and idiomatic way to reverse a list.

#------- LIST COMPREHENSION -------

# are a useful way of quickly creating lists whose contents obey(cumplir) a simple rule.

cubes = [i**3 for i in range(5)]

print(cubes) #[0, 1, 8, 27, 64]

#A list comprehension can also contain an if statement to enforce (hacer cumplir) a condition on values in the list.

evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens) # [0, 4, 16, 36, 64]

#------ STRING FORMATTING ------

'''
String formatting provides a more powerful way to embed non-strings within strings. String formatting uses a string's 
format method to substitute a number of arguments in the string. 
'''
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg) # Numbers: 4 5 6

#NOTE: Each argument of the format function is placed in the string at the corresponding position, which is determined
# using the curly braces { }.

#String formatting can also be done with named arguments.
a = "{x}, {y}".format(x=5, y=12)
print(a) #5, 12

#------ STRING FUNCTIONS ------
'''
join - joins a list of strings with another string as a separator.
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
To change the case of a string, you can use lower and upper.
The method split is the opposite of join turning a string with a certain separator into a list.
'''

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"
        
#----- Numeric Funcitons -------

'''
To find the maximum or minimum of some numbers or a list, you can use max or min.
To find the distance of a number from zero (its absolute value), use abs.
To round a number to a certain number of decimal places, use round.
To find the total of a list, use sum.
'''

print(min(1, 2, 3, 4, 0, 2, 1)) # 0
print(max([1, 4, 9, 2, 5, 6, 8])) #9
print(abs(-99)) #99
print(abs(42)) #44
print(sum([1, 2, 3, 4, 5])) #15

#------ List Functions -------
'''
Often used in conditional statements, all and any take a list as an argument, and return True if all or any 
(respectively)  of their arguments evaluate to True (and False otherwise).
The function enumerate can be used to iterate through the values and indices of a list simultaneously.
'''

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5") #All larger than 5

if any([i % 2 == 0 for i in nums]):
    print("At least one is even") #At least one is even

for v in enumerate(nums):
    print(v) #(0, 55) (1, 44) (2, 33) (3, 22) (4, 11)





