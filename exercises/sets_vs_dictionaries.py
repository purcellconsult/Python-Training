# dictionaries and sets in python
# -------------------------------------
# dictionaries store key/value mappings
# a set stores a unique collection of items
# dictionary keys are immutable which is why we can use strings as a key
# dictionaries order are unpredictable due to complicated fast hashing algorithm python uses

# declaring a dictionary
# ----------------------

fruit = {
    'a': 'apple',
    'b': 'blueberries',
    'c': 'cherries',
    'd': 'datefruit',
    'f': 'figs',
    'g': 'guava'
}

# common dictionary operations
# ----------------------------
# reassign values of keys
# delete keys

print(fruit)      # display the dictionary
print(fruit['a']) # print the value at 'a'
print(fruit['f']) # print the value at f

fruit['g'] = 'grapefruit'  # change the value of the dictionary at key g to grapefruit

del fruit['d']
print(fruit)

# common dictionary methods
# -------------------------
# get()
# keys()
# values()
# items()

dict_get = fruit.get('c')
dict_keys = fruit.keys()  # returns all of the keys
dict_values = fruit.values()  # returns all of the values
dict_items = fruit.items()  # returns all of the items in dict

print(dict_get)
print(dict_keys)
print(dict_values)

# how to iterate over a dictionary
# --------------------------------
# need to store the key/value mappings in two variables

for key, value in fruit.items():
    print(key, value)

# how to use a dictionary to get the counts of all in a word?

city = 'San Francisco'
letter_counts = {} # empty dictionary
for letter in city:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)


# sets in python
# --------------
# an unordered collection of objects
# sets cannot have duplicate members
# like tuples and dictionaries, sets must be 'hashable'
# there's no way to access indices in sets


# set basics in python
dummy_set = set()
dummy_set.add('cat') # adds cat to the set
dummy_set.update(['dog', 'parrot']) # adds multiple items to the set

# member test
if 'rat' in dummy_set:
   dummy_set.remove('rat')
else:
    print('No rat found!')

# get the size of the set
size = len(dummy_set)
print('The set has a length of {}'.format(size))
dummy_set.update(['cat', 'cat', 'cat', 'dog', 'alligator'])
# see no duplicates allowed
print(dummy_set)


# unique set operations
# ----------------------
# can do union, intersection, set difference, symmetric difference

venn_diagram_a = set(['a', 'b', 'c', 'd'])
venn_diagram_b = set(['c', 'd', 'e', 'f'])


union_example = venn_diagram_a.union(venn_diagram_b)
difference_example = venn_diagram_a.intersection(venn_diagram_b)
set_difference = venn_diagram_a.difference(venn_diagram_b)
symmetric_difference = venn_diagram_a.symmetric_difference(venn_diagram_b)

print('union example = {}'.format(union_example))
print('union example = {}'.format(difference_example))
print('set difference example = {}'.format(set_difference))
print('symmetric difference example = {}'.format(symmetric_difference))

