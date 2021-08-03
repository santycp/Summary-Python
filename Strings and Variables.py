# ------- BACKSALSH ------

# Backslashes can also be used to escape tabs, arbitrary Unicode characters,
# and various other things that can't be reliably printed

print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')

# ------- NEWLINES ------

# \n represents a new line.
# It can be used in strings to create multi-line output:

print('One\nTwo\nThree')

# Newlines will be automatically added for strings that are created using three quotes.

print("""this
is a
multiline
text""")
print('-------------------------')

# ------ CONCATENATION ------

# s with integers and floats, strings in Python can be added, using a process called concatenation,
# which can be done on any two strings.

print("X" + "D")
print('-------------------------')

# NOTE:
# Adding a string to a number produces an error, as even though they might look similar,
# they are two different entities.

# ------- STRING OPERATIONS -------

# Strings can also be multiplied by integers. This produces a repeated version of the original string.
# The order of the string and the integer doesn't matter, but the string usually comes first.

print("spam" * 3)

print(4 * '2')

print('-------------------------')

# ------- VARIABLE NAMES ------

#Certain restrictions apply in regard to the characters that may be used in Python variable names.
#The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
# Not following these rules results in errors

#NOTE
#python is case sensitive

# ------- INPUT ------
#The input function prompts the user for input,
# and returns what they enter as a string (with the contents automatically escaped).

#The input statement needs to be followed by parentheses.
#You can provide a string to input() between the parentheses, producing a prompt message.

x=input("Enter any thing")
print(x)
#NOTE:
#Even if the user enters a number as input, it is processed as a string.

#To convert it to a number, we can use the int() function:
age = int(input("enter any age"))
print(age)

#similary with string functions

#NOTE
#When input() function executes, program flow stops until a user enters some value.
print('-------------------------')

# ------- IN-PLACE OPERATORS ------

#allow you to write code like 'x = x + 3' more concisely, as 'x += 3'.
#The same thing is possible with other operators such as -, *, / and % as well.

x = 2
print(x)

x += 3
print(x)


#These operators can be used on types other than numbers, as well, such as strings

x = "spam"
print(x)

x += "eggs"
print(x)

#NOTE:
#In-place operators can be used for any numerical operation (+, -, *, /, %, **, //).

print('-------------------------')

# ------- WALRUS OPERATOR ------
#Walrus operator := allows you to assign values to variables within an expression,
# including variables that do not exist yet

#The walrus operator accomplishes these operations at once:

print(num:=int(input()))