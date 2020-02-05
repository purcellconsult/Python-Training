# loop exercises to help understand loops in python
# -------------------------------------------------


# break statement
i = 0
while i < 20:
    i += 1
    if i == 11:
        break
    else:
        print('i =', i, end=' ')
print()
# continue statement

i = 0
while i < 20:
    i += 1
    if i == 11:
        continue
    else:
        print('i =', i, end=' ')

print()
# loop exercise: generate numbers in range of 1 - 20
# only print numbers divisible by 2 and 3
# hint: use % operator to see if there's a remainder

i = 1
while i <= 20:
    i += 1
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=' ')

print()
# loop exercise: print even numbers in range of 1 - 100 using for loop
for x in range(1, 101):
    if x % 2 == 0:
        print(x, end=' ')

print()
# loop exercise: print even numbers in range of 1 - 100 using while loop

counter = 1
while counter < 100:
    if counter % 2 == 0:
        print(counter, end=' ')
    counter += 1

print()

# loop exercise: write a loop that counts the even numbers between 1 - 155

i, sum = 1, 0
while i <= 155:
    if i % 2 == 0:
        sum += 1
    i+= 1
print(sum)

print()
# nested for loops in python
for x in range(2):
    for y in range(2):
        print(y, end=' ')
    print()

print()
# star grid pattern
for x in range(4):
    for y in range(4):
        print('*', end=' ')
    print()

# print triangle pattern
for row in range(5):
    for col in range(row):
        print('*', end=' ')
    print()