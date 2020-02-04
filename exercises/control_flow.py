x = 5
if x == 5:
    print('Hello World!')

y = 10
if y > 3:
    print('Ok!')

if x > 5:
    print('a')
else:
    print('b')

# tests the and operator
# if/else statement

x, y = 5, 10
if x > y and y < 20:
    print('happy')
else:
    print('hour')


# tests the or operator
a, b = 2, 3
if a > b or b < 10:
    print('bingo!')
else:
    print('orange')


# if/else/elif
# allows you to chain conditional checks
x, y, z = 5, 10, 13

if x > y and z < z:
    print('a')
elif z > x and z > y:
    print('b')
else:
    print('c')

# nested if else statements

x, y = 5, 10
if x > y and y < 13:
    print('a')
    if x + y < 20:
        print('b')
    else:
        print('something')
else:
    print('c')

# scoping
# inner variable

x = 4
if x > 5:
    x = 20
else:
    something = 5

print(something)


