# ------ REGULAT EXPRESION ------

'''

Regular expressions are a powerful tool for various kinds of string manipulation.
They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python.
They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format of an email address),
- performing substitutions in a string (such as changing all American spellings to British ones).

'''

# Regular expressions in Python can be accessed using the re module, which is part of the standard library.
# After you've defined a regular expression, the re.match function can be used to determine whether it matches at the
# beginning of a string.

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")  # result
else:
    print("No match")

# Other functions to match patterns are re.search and re.findall.
# The function re.search finds a match of a pattern anywhere in the string.
# The function re.findall returns a list of all substrings that match a pattern.

import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")  # result

if re.search(pattern, "eggspamsausagespam"):  # The search function found a match in the string.
    print("Match")  # result
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))  # ['spam', 'spam']

# The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
# _-----------------------_____________________


# The regex search returns an object with several methods that give details about it.

import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())  # group which returns the string matched   pam
    print(match.start())  # return the start positions of the first match    4
    print(match.end())  # return the end positions of the first match     7
    print(match.span())  # returns the start and end positions of the first match as a tuple.     (4, 7)

    # ¡¡¡¡ SON FUNCIONES !!!!!

# ------ Search & Replace ------

# SUB
# re.sub(pattern, repl, string, count=0) SINTAX

'''
This method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless count
provided. This method returns the modified string. 
'''

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)  # My name is Amy. Hi Amy.

# ------ Methacaracteres -------

# is a normal string with an "r" in front of it

# metacharacter .(dot):
# This matches any character, other than a new line(que no sea una nueva línea.).

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")  # result

if re.match(pattern, "gray"):
    print("Match 2")  # result

if re.match(pattern, "blue"):
    print("Match 3")  # no result

# metacharacter ^ and $:
# These match the start and end of a string, respectively.

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")  # result

if re.match(pattern, "gray"):
    print("Match 2")  # result

if re.match(pattern, "stingray"):
    print("Match 3")

# The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline,
# and end with y

# ------ Characterer Classes -------

# provide a way to match only one of a specific set of characters.

import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")  # result

if re.search(pattern, "qwertyuiop"):
    print("Match 2")  # result

if re.search(pattern, "rhythm myths"):
    print("Match 3")  # no result

# The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

'''
Character classes can also match ranges of characters.
Some examples:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit.
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case. 
'''

import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")  # result

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")

# The pattern in the example above matches strings that contain two alphabetic uppercase letters followed by a digit.
# _---------_

# Place a ^ at the start of a character class to invert it.
# Esto hace que coincida con cualquier carácter que no sean los incluidos.
# The metacharacter ^ has no meaning unless it is the first character in a class.

import re

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")  # result

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")

# ------ Metacharacters ------
# The metacharacter * means "zero or more repetitions of the previous thing".

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

# The example above matches strings that start with "egg" and follow with zero or more "spam"s.
# ----------------------------------------------------------------------
# The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more
# repetitions".

import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")  # result

if re.match(pattern, "gggggggggggggg"):
    print("Match 2")  # result

if re.match(pattern, "abc"):
    print("Match 3")

'''
To summarize:
* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression.
'''

# The metacharacter ? means "zero or one repetitions".

import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")  # result

if re.match(pattern, "icecream"):
    print("Match 2")  # result

if re.match(pattern, "sausages"):
    print("Match 3")

if re.match(pattern, "ice--ice"):
    print("Match 4")

# ------ Curly Braces ------

# can be used to represent the number of repetitions between two numbers.

import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")  # result

if re.match(pattern, "999"):
    print("Match 2")  # result

if re.match(pattern, "9999"):
    print("Match 3")

# "9{1,3}$" matches string that have 1 to 3 nines.

# ------ Groups -------

'''
A group can be created by surrounding part of a regular expression with parentheses.
This means that a group can be given as an argument to metacharacters such as * and ?. 
'''

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")  # result

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")  # result

if re.match(pattern, "spam"):
    print("Match 3")

# (spam) represents a group in the example pattern shown above.

# ---------------------------------------------------------

# The content of groups in a match can be accessed using the group function.

# A call of group(0) or group() returns the whole match.
# A call of group(n), where n is greater than 0, returns the nth group from the left.
# The method groups() returns all groups up from 1.

import re

pattern = r"a(bc)(de)(if(g)h)"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())  # abcdefghi
    print(match.group(0))  # abcdefghi
    print(match.group(1))  # bc
    print(match.group(2))  # de
    print(match.groups())  # ('bc', 'de', 'fgh', 'g')

# -----------------

'''
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave 
exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering. 
'''

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))  # abc
    print(match.groups())  # ('abc', 'ghi')

# -----------------------

# Another important metacharacter is |.
# This means "or", so red|blue matches either "red" or "blue".

import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Match 1")  # result

match = re.match(pattern, "grey")
if match:
    print("Match 2")  # result

match = re.match(pattern, "griy")
if match:
    print("Match 3")


#------ ESPECIAL SEQUENCES ------

#They are written as a backslash followed by another character.

import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print ("Match 1") #result

match = re.match(pattern, "?! ?!")
if match:
    print ("Match 2") #result

match = re.match(pattern, "abc cde")
if match:
    print ("Match 3")

'''
More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively.
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit. 
'''


import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1") #result

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")


"""
Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else. 
"""

import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print ("Match 1") #result

match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2") #result

match = re.search(pattern, "We scattered.")
if match:
    print ("Match 3")



#------ Email Extraction -------

import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())