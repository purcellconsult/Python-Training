# text based guessing game
# prompts the user to guess a number from 1...100
# gives the user feedback
# if user guessed correct number they won

from random import randint

# get random number in range from 1-100
rand_num = randint(1, 100)

# create an infinite loop
while True:
    user_input = int(input('Enter in a number from 1-100 '))
    # conditional checks to compare user's guess to secret number
    # checks edge case if user entered in a number outside 1-100
    if user_input > 100 or user_input < 1:
        print('Invalid input. Enter in a number from 1-100')
        print('Exiting...')
        exit(0)
    if user_input == rand_num:
        print('You Win! Secret number is', rand_num)
        print('You Win! Secret number is', rand_num)
        break
    elif user_input > rand_num:
        print(user_input, 'is too big')
    else:
        print(user_input, 'is too small')