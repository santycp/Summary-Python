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