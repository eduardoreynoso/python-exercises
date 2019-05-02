# Make a game that generates a random number and allows the user to guess it
# by giving clues on how far the user is from the actual number

# 1.- Generate the random number
# 2.- Ask for user input
# 3.- Compare input to random number
# 4.- If incorrect give clue
# 5.- Go back to step 2
# 6.- If correct, terminate program with success

import time
import random

if __name__ == '__main__':

    MIN_NUM = 1
    MAX_NUM = 10
    MAX_RETRIES = 5

    print('Welcome to the Guessing game!')

    print('Generating a random number...')
    time.sleep(1)
    num_to_guess = random.randint(MIN_NUM, MAX_NUM)
    print('Done! Can you guess it?')

    guess = ''
    tries = 0
    while guess != 'exit' and tries < MAX_RETRIES:
        print('{} retries left'.format(MAX_RETRIES - tries))
        tries += 1
        guess = input()
        try:
            guess_num = int(guess)
        except ValueError:
            print('Thats not a number...')
            continue

        if guess_num == num_to_guess:
            print('You did it! It only took you {} tries'.format(tries))
            exit(0)
        if guess_num > num_to_guess:
            print('Too big! try again')
        else:
            print('Too small! try again')

    if guess == 'exit':
        print('Nobody likes quiters')
    else:
        print('Ran out of retries :(')

    exit(0)

# This is the code that we came up during the session
#
# if __name__ == '__main__':
#
#     MIN_NUM = 1
#     MAX_NUM = 10
#     MAX_RETRIES = 300
#
#     num_to_guess = random.randint(MIN_NUM, MAX_NUM)
#     print('You have to guess: {}'.format(num_to_guess))
#
#     guess = 0
#     while guess != num_to_guess and MAX_RETRIES > 0:
#         MAX_RETRIES -= 1
#         try:
#             guess = input()
#             if guess == 'exit':
#                 print('Nobody likes quitters')
#                 exit()
#             guess = int(guess)
#         except ValueError:
#             print('Thats not a valid integer!')
#             continue
#
#         # Print the clues
#         if guess < num_to_guess:
#             print('Too small!')
#         elif guess > num_to_guess:
#             print('Too big!')
#
#     if MAX_RETRIES < 1:
#         print('You lost!')
#     else:
#         print('You guessed it!')
#     exit()
