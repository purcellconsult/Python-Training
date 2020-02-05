#  Strings in python
# -------------------------------------------------------
# Strings are a sequence data type in python
# Strings are immutable like tuples. Once created
# they can't be modified.
#
# Can create strings with single, double, or triple quotes
#
###########################################################

import string
import re

lang = 'python'

# testing membership
test_1 = 'a' in lang    # False
test_2 = 'y' in lang    # True

# concatenating or combing
test_3 = lang + 'language' # print(test_3)

# can multiple strings

test_4 = lang * 4

print(test_1)
print(test_2)
print(test_3)
print(test_4)


# iterating over strings with for loop
for x in lang:
    print(x)

i = 0
while i < len(lang):
    print(lang[i])
    i += 1

# built in string functions
# -------------------------
# chr(): converts to character
# ord(): converts character to an integer
# str(): returns a string representation of object

num = 263728
print(type(num))  # <class 'int'>

num = str(num)  # converts to a string
print(type(num)) # <class 'str'>

# test the ord function
# corresponds to their ascii values: https://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html

print(ord('a'))
code = '087'

# print the character by passing the ascii code into the chr() function
code = chr(102)
print(code)


# common string operations
# ------------------------

sport = 'basketball'
print(sport[0] + sport[-1]) # bl
print(sport[0:6]) # returns basket
print(sport[6:10]) # returns ball

# common string methods
# ---------------------

mes = 'Hello World'
print(mes.capitalize())
print(mes.count('o')) # returns number of occurrence for that string
print(mes.find('W')) # returns the index of the string
print(mes.casefold()) # converts string to all lowercase
print(mes.isalpha()) # returns true if all characters in string are in alphabet


nasty_string = " shdjkddjjd kdkdk  "
print(nasty_string.strip()) # strips leading and trailing characters

message = 'hello-world'
x = message.split('-') # splits string around a delimiter
print(x)


# common regular expressions
# ---------------------------
# re module docs in python: https://docs.python.org/3/library/re.html
#
# an old computer science joke. I have a problem I need to solve with
# regex. I now have two two problems!
#
# allows you to retrieve specific parts of a string or substring
# a builtin module in python.
#
# import re
# create our regex pattern
# * is a wildcard which means we can have 0 or more characters
# we can use search to compare our pattern to a string we want to inspect
# if a match is found the range of indices are returned, if not None is returned
# we can compile our pattern so we can reuse it multiple times in our program

p1 = re.compile('abc*')
test_1 = re.search(p1, 'gskjsks')
test_2 = re.search(p1, 'aaaa')
test_3 = re.search(p1, 'aaaabc')
test_4 = re.search(p1, 'aaaaacccccccbbb')
test_5 = re.search(p1, 'shaushuashquhs8181ababababcajsjdchciwiccwhwc')

print(test_1)
print(test_2)
print(test_3)
print(test_4)
print(test_5)


# there's built in character classes in regex

p2 = re.compile('[a-z][A-Z][0-9]*')
test_6 = re.search(p2, 'a')
test_7 = re.search(p2, 'aZ')
test_8 = re.search(p2, 'abC')
test_9 = re.search(p2, '37373793aC297239972')
test_10 = re.search(p2,'/./9822y7ey72heuGVTDagyag91' )

print(test_6)
print(test_7)
print(test_8)
print(test_9)
print(test_10)

# ??? how  can we write a regex to verify a phone number in this syntax?
#  ###-###-####
# test your input against these numbers
#

# escaping characters in strings
# ------------------------------
# can wrap double quotes around single quotes
# can use the backslash \ symbol in front of the escaped symbol

song = "ain't no body stopping us now"
song = 'ain\'t no body stopping us now'
song = "'ain\'t no body stopping us now'"
print()

# ?? fix this example!
# keep the double quotes ("") around the title monty python
# ---------------------

# messy_string = 'I'm so happy that everyone likes this song of mines titled "monty python"'""

# the format method
# --------------------
# another way to format strings

string_1 = 'item number {} {} and {}'.format(1, 2, 3)
string_2 = "{} + {} = {}".format(5, 10, 5 + 10)
string_3 = "There are {} days in the week.".format(7)
string_4 = "{1}, {0}, {2}".format(5, 10, 15)

print(string_1)
print(string_2)
print(string_3)
print(string_4)
print()

# random password generator
# ---------------------------
# create a random password with default length of 15
# the password length can be modified by the user. But can't be less than 15 or greater than 30
# the password can have ascii letters, digits, and punctuation
#  create a function called random_password_generator()
# -----------------------------------------------------

# methods that may be helpful from the string class
print(string.ascii_letters) # returns all of the ascii letters in the alphabet
print(string.digits) # returns only digits
print(string.punctuation) # returns only punctuation marks


# random person generator
# -----------------------
# create a random person with the following details
# a name
# a gender
# a phone number
# city of residence
# favorite food
# male names = 'Adam', "Ben', 'Charles', 'Dan', 'Eric'
# female names - 'Alice', 'Beth, 'Cindy', 'Danica', 'Evora'
# create a module called random person
# create a function for each feature
# create a function that returns the results as a dictionary

# tips
# ----
# think about data structure to use
# ---------------------------------------
# use the choice function from random module
# female = ['Alice', 'Beth', 'Cindy', 'Danica, 'Evora']
# name = choice(female)
# >>> name
# 'Alice'





