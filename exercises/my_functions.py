
#  a list of functions to work on for practice
# max:


def maximum(x, y):
    """
    return the highest value passed
    into the function.
    if 0 is returned, x and y are equal.
    """

    if x == y:
        return 0
    if x > y:
        return x
    else:
        return y


def minimum():
    pass


def read_numbers(*args):
    """
    read in arbitary numbers and then
    we want to return the largest number
    """
    max = args[0]
    for x in args:
        if x > max:
            max = x
    return max


def summation(*args):
    """
    create a function that
    sums all of the numbers
    together.
    test case 1: summation(1,2,3) = 6
    test case 2: summation(2, 4, 6, 8, 10) = 30
    test case 3: summation(-5, -2, 0, 3, 6, 8, 10) = 20
    """
    sum = 0
    for x in args:
        sum += x
    return sum


def mean(*args):
    """
    calculates the mean of a set
    of numbers.
    test case 1: mean(4, 10, 100, 50, 30) = 38.8
    test case 2: mean(4, 10, 100, 50, 30, 100, -7, 8 , 54, 27.8) = 37.68
    test case 3: mean(1000, 0, 67) = 355.666666667
    """
    sum, count = 0, 0
    for x in args:
        sum += x
        count += 1
    return sum / count




# test cases
a = maximum(5, 10)
a1 = maximum(10, 15)
a2 = maximum(50, 70)
print(a)
print(a1)
print(a2)

print(read_numbers(1, 5, 9, 15, 2, 100, 7, 9))
print(read_numbers(2, 6, 8, 10, 2, 3, 7, 4))
print(read_numbers(5, 4, 8, 34, 23, 10))
print(read_numbers(-100, -75, -55, -23, -1, -1000))

assert maximum(100, 90) == 100

# summation test cases
print(summation(1,2,3))