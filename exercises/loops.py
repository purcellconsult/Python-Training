

# print even numbers from range 1-100
# from odd numbers from range 1-100
# print numbers from range 1- 100. If # is divisible by 3 print 'hello', if divisible by 7 print 'world'
# sum the numbers from 1-100. Use a while loop
# write a python program that prints the numbers from 1-10 except 3 and 6
# write a python program that prints integers from 1-50. For multiples of 3 print 'Fizz'. For multiples of 5 print Buzz. For multiples of 3 and 5 print 'FizzBuzz.'

# prints even numbers in range of 1-100
for x in range(101):
    if x % 2 == 0:
        print(x, end=' ')

print()
# prints odd numbers in range of 1-100
for x in range(101):
    if x % 2 is not 0:
        print(x, end=' ')

print()
for x in range(1, 101):
    if x % 3 == 0:
        print('hello', end=' ')
    elif x % 7 == 0:
        print('world', end=' ')
    else:
        print(x, end=' ')

print()

# sum the numbers from 1..100
i = 1
sum = 0
while i < 101:
    sum += i
    i += 1
print('sum of 1-100 =', sum)

# prints numbers from 1-10 except 3 and 6. Use a for loop.
for x in range(1, 11):
    if x == 3 or x == 6:
        continue
    else:
        print(x, end=' ')

print()
# write a program that prints the numbers from 1-50
# for multiples of 3 print 'Fizz'
# for multiples of 5 print 'Buzz'
# for multiples of 3 and 5 print 'FizzBuzz'
# a popular interview question

for x in range(1, 51):
    if x % 3 ==0 and x % 5 == 0:
        print('FizzBuzz', end=' ')
    elif x % 3 == 0:
        print('Fizz', end=' ')
    elif x % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(x, end=' ')

print()
# generate 100 random numbers in the range of 1-100
# use the randint function from the random module
# >>> from random import randint
# >>> randint(1, 100)

from random import randint
for x in range(100):
    ran_num = randint(1, 100)
    print(ran_num, end=' ')
print()

# nested loops examples
# print the following pattern
# * * *
# * * *
# * * *

for x in range(3):
    for y in range(3):
        print('*', end=' ')
    print()
print()

# print the following pattern
# *
# * *
# * * *
# * * * *

for x in range(1, 5):
    for y in range(x):
        print('*', end=' ')
    print()

# print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for x in range(1, 6):
    for y in range(1, x):
        print(y, end=' ')
    print()
