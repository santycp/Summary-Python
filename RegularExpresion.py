#------ REGULAT EXPRESION ------

'''

Regular expressions are a powerful tool for various kinds of string manipulation.
They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python.
They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format of an email address),
- performing substitutions in a string (such as changing all American spellings to British ones).

'''

#Regular expressions in Python can be accessed using the re module, which is part of the standard library.
#After you've defined a regular expression, the re.match function can be used to determine whether it matches at the
# beginning of a string.

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match") #result
else:
    print("No match")

#Other functions to match patterns are re.search and re.findall.
#The function re.search finds a match of a pattern anywhere in the string.
#The function re.findall returns a list of all substrings that match a pattern.

import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match") #result

if re.search(pattern, "eggspamsausagespam"): #The search function found a match in the string.
    print("Match") # result
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam")) #['spam', 'spam']


#The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
#_-----------------------_____________________


#The regex search returns an object with several methods that give details about it.

import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group()) #group which returns the string matched   pam
    print(match.start()) #return the start positions of the first match    4
    print(match.end()) #return the end positions of the first match     7
    print(match.span()) #returns the start and end positions of the first match as a tuple.     (4, 7)

    #¡¡¡¡ SON FUNCIONES !!!!!



#------ Search & Replace ------

# SUB
#re.sub(pattern, repl, string, count=0) SINTAX

'''
This method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless count
provided. This method returns the modified string. 
'''

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr) #My name is Amy. Hi Amy.

#------ Methacaracteres -------

#is a normal string with an "r" in front of it

# metacharacter .(dot):
#This matches any character, other than a new line(que no sea una nueva línea.).

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1") #result

if re.match(pattern, "gray"):
    print("Match 2") #result

if re.match(pattern, "blue"):
    print("Match 3") #no result


#metacharacter ^ and $:
#These match the start and end of a string, respectively.

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1") #result

if re.match(pattern, "gray"):
    print("Match 2") #result

if re.match(pattern, "stingray"):
    print("Match 3")

#The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline,
# and end with y.