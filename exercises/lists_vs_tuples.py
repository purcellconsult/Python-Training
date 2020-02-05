# lists are mutable in memory
# they can be modified

x = [2, 4, 7]
x.append(1)


# tuples are immutuable
# there are no methods to add or remove items from a list

y = (0, 2, 5, 10)

# the items in a list can be reassigned

list_items = [1, 2, 3]
list_items[0] = 100

# the items in a tuple can't be reassigned or less an error happens

tuple_items = (2, 4, 6, 8)
# tuple_items[0] = 10 NOT ALLOWED

# but that's strange, why can this happen?
tuple_items = (0, 1)
print(tuple_items)

# we're not changing the values, just the location in memory
# we can inspect this using id(). This gives us an object's location in memory

# tuple 1
tup_1 = (0, 1, 2)
print(id((tup_1))) # 11021648

tup_2 = (4, 5)
print(id(tup_2)) # 11019848

# this means that the locations are different!
# this means that the original tuple is still in memory
# in the background a new tuple was created, and the variable points to it

# which one is better to use? lists or tuples?
# short answer, if you need to modify a data structure use list
# if you don't need the data structure to change use tuple

# which one has better performance? Let's test
# tuples are better for saving space since they don't need overallocate memory
# lists tend to overallocate to make up for the append operations.
#
# >>> sys.getsizeof(tuple(iter(range(100))))
# 428
# >>> sys.getsizeof(list(iter(range(100))))
# 508
#