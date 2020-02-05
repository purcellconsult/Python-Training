# like oop this is another style of programming
# python is not fully a functional programming lang, but does enable
# some features.
# we will work with
# lambda, map, filter, reduce

# lambda expression:
# ------------------
# lambdas are also anonymous expressions
# lambda syntax:  arguments: expression


def square(x, y):
    return x * y

square_lambda =  lambda x : x * x
print(square_lambda(5))

# filter
# takes in a function and a list of arguments

nums = [1, 3, 4, 6, 10, 15, 20]
filter_nums = list(filter(lambda nums: nums > 5, nums))
print(filter_nums)

# map function
# takes in a function and list as an argument
# a new list is returned which contains all of
# the lambda modified items returned by that function

items = [1, 2, 3, 5, 7, 10, 11, 12, 13]
mapped_items = list(map((lambda x: x * 5), items))
print(mapped_items)

# reduce function
# performs a repetitive operation over the pairs of a list
from functools import reduce

items = [x for x in range(1, 10001)]
summation = reduce((lambda x, y: x + y), items)
print(summation)
