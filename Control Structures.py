# ------ BOOLEAN ------
# There are two Boolean values: True and False.
#They can be created by comparing values, for instance by using the equal operator ==.

# ------ COMPARASION ------
'''
Another comparison operator, the not equal operator (!=),
evaluates to True if the items being compared aren't equal, and False if they are.

Python also has operators that determine whether one number (float or integer) is greater than or smaller than another.
these operators are > and < respectively.

The greater than or equal to, and smaller than or equal to operators are >= and <=.

Greater than and smaller than operators can also be used to compare strings lexicographically (the alphabetical order
 of words is based on the alphabetical order of their component letters).
'''
print("Annie" > "Andy") #True

#------ if STATEMENT -------

#If an expression evaluates to True, some statements are carried out. Otherwise, they aren't carried out.

if 10 > 5:
    print("10 greater than 5")

print("Program ended")

#NOTE
#Indentation is used to define the level of nesting.

#------ else STATEMENT -------

x = 4
if x == 5:
    print("Yes")
else:
    print("No")

#NOTE
#Indentation determines which if/else statements the code blocks belong to.

#------ elif STATEMENT -------
#The elif (short for else if) statement is a shortcut to use when chaining if and else statements, making the code shorter.
num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")


#------- OPERATOR PRECEDENCE ------
'''
Python's order of operations is the same as that of normal mathematics: parentheses first, then exponentiation,
then multiplication/division, and then addition/subtraction.
'''

#------- LIST ------

#Lists are used to store items.
#A list is created using square brackets with commas separating items.

words = ["Hello", "world", "!"]

#A certain item in the list can be accessed by using its index in square brackets.

print(words[0])
print(words[1])
print(words[2])

#NOTE:
#The first list item's index is 0, rather than 1, as might be expected.
#In some code samples you might see a comma after the last item in the list. It's not mandatory, but perfectly valid.



#Typically, a list will contain items of a single item type, but it is also possible to include several different types.
#Lists can also be nested within other lists

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])

#Some types, such as strings, can be indexed like lists.

str = "Hello world!"
print(str[6])

#NOTE: Space (" ") is also a symbol and has an index.

#------- LIST operations------

#The item at a certain index in a list can be reassigned.
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums) # output:  [7, 7, 5, 7, 7]

#NOTE: You can replace the item with an item of a different type.

#Lists can be added and multiplied in the same way as strings.

nums = [1, 2, 3]
print(nums + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print(nums * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#To check if an item is in a list, the in operator can be used.
#It returns True if the item occurs one or more times in the list, and False if it doesn't.
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words) #True
print("egg" in words) #True
print("tomato" in words)#False

#------- LIST functions ------

#The "append" method adds an item to the end of an existing list.
nums = [1, 2, 3]
nums.append(4)
print(nums) #[1, 2, 3, 4]
#NOTE: the dot before append is there because it is a method of the list class.

#To get the number of items in a list, you can use the "len" function.

nums = [1, 3, 5, 2, 4]
print(len(nums)) #5

#Unlike the index of the items, len does not start with 0. So, the list above contains 5 items,
# meaning len will return 5.
#NOTE: len is written before the list it is being called on, without a dot.


#The "insert" method is similar to "append", except that it allows you to insert a new item at any position in the list,
# as opposed to just at the end.

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words) #['Python', 'is', 'fun']

#NOTE: Elements, that are after the inserted item, are shifted to the right.


#The index method finds the first occurrence of a list item and returns its index.
#If the item isn't in the list, it raises a ValueError.

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r')) #2
print(letters.index('p')) #0
print(letters.index('z')) #ValueError

'''
There are a few more useful functions and methods for lists.
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(item): Returns a count of how many times an item occurs in a list
list.remove(item): Removes an object from a list
list.reverse(): Reverses items in a list. 
'''
# example:
#For example, you can count how many 42s are there in the list using:
#items.count(42)
#where items is the name of our list.

#------- while LOOPS ------

#A while loop is used to repeat a block of code multiple times.
i = 1
while i <=5:
    print(i)
    i = i + 1

print("Finished!")

#You can use multiple statements in the while loop.

x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1

#NOTE:you can stop the program's execution by using the Ctrl-C

#------- break ------

#To end a while loop prematurely, the break statement can be used.

i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

#------- continue ------

#Unlike break, continue jumps back to the top of the loop, rather than stopping it. Basically, the continue statement
# stops the current iteration and continues with the next one.

i = 1
while i<=5:
  print(i)
  i += 1
  if i==3:
    print("Skipping 3")
    continue

#------- for LOOP ------

#The for loop is used to iterate over a given sequence, such as lists or strings.

words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")
                        #hello!
                        #world!
                        #spam!
                        #eggs!
#Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump
# to the next iteration

#------- RANGE ------

#The range() function returns a sequence of numbers.
#By default, it starts from 0, increments by 1 and stops before the specified number.
numbers = list(range(10))
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#NOTE: In order to output the range as a list, we need to explicitly convert it to a list, using the list() function.

#If it is called with two arguments, it produces values from the first to the second.

numbers = list(range(3, 8))
print(numbers) #[3, 4, 5, 6, 7]

print(range(20) == range(0, 20)) #True

#range can have a third argument, which determines the interval of the sequence produced, also called the step

numbers = list(range(5, 20, 2))
print(numbers) #[5, 7, 9, 11, 13, 15, 17, 19]

'''
PROBLEM (FIZZBUZZ)

The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn". 

'''

n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 2 == 0:
        continue
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")

    else:
        print(x)
