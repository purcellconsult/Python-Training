# sequence types in python
# ------------------------
# lists, tuples, strings
# common operations that can be performed
# x in s, x not in s, s + t, s* n, s[i], s[i:j], len(s), min(s), max(s)
#

# list examples
x = [2, 4, 6, 8, 10]

# indexing lists
print(x[0])
print(x[4])

# python allows negative indices
print(x[-1])
print(x[-5])
print(x[len(x)-1])
# print(x[5]) gives error. doesn't exist.

# slicing lists
# -------------
# x[i:j]

y = [1, 2, 3, 4, 10, 20, 100]
print(y[0:3]) # returns [1, 2, 3]
print(y[::]) # returns the whole list
print(y[::2]) # returns [1, 3, 10, 100]
print(y[::-1]) # reverses the list

# iterating over sequences

# for loop
for x in y:
    print(x, end=' ')

print()
# check to see if a element in less is greater than 5
for x in y:
    if x > 5:
        print(x, end=' ')
print()


# while loop to print the elements in y
size = len(y)
i = 0
while i < size:
    print(y[i], end=' ')
    i += 1

print()
print(max(y))
print(min(y))

# built in methods of the list class
# append

empty = []
for x in range(1, 10):
    empty.append(x)

# creates a list with numbers 1... 9
print(empty)

# creates a second list with items in reverse
item_2 = []
for x in empty:
    last = empty.pop()
    item_2.append(last)

# pop example
print(empty.pop())


# creating lists using list comprehensions
# creates list using list comprehension
# prints a list within 1 ... 10
x = [x for x in range(1, 11)]
print(x)

even_nums = [x for x in range(20) if x % 2 == 0]
print(even_nums)

from random import randint
random_numbers = [randint(1, 100) for x in range(11)]
print(random_numbers)

some_list = [x for x in range(1, 31) if x > 20]
print(some_list)

# nested lists

nested_list = [1, 3, 6, [2, 4, 6], [10, 12, 14], 3, 7]
print(nested_list)
print(nested_list[3])

# how can we ensure that two lists have the same number of elements


# tuple
# tuple is immutuable
a = (2, 4, 6, 8)
print(a[0])
a[0] = 5

# list is mutable  
b = [0, 1, 2]
b[0] = 10
print(b)

