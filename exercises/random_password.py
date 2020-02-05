# generates random password
# uses ascii letters
# uses punctuation
# uses digits

import string
from random import choice

glyphs = [] # creates empty list
password = '' # password to be created
glyphs.extend(string.ascii_letters) # add ascii letters to list
glyphs.extend(string.digits) # adds digits to list
glyphs.extend(string.punctuation) # adds punctuation to list

for x in range(16):
    randomly_selected = choice(glyphs) # randomly selects character
    password += randomly_selected
print(password)


