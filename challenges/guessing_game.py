# This is a Guess the Number game by Mr. Tibor
import random

continue_game = True

print('Hello! What is your name?')
my_name = input()

while continue_game:
    number = random.randint(1, 21)
    print('Well, ' + my_name + ', I am thinking of a number between 1 and 20.')
    guesses_taken = 0

    while guesses_taken < 6:
        print('Take a guess.')  # Four spaces in front of "print".
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print('Your guess is too low.')  # Eight spaces in front of "print"

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guesses_taken = str(guesses_taken + 1)
        print('Good job, ' + my_name + '! You guessed my number in ' + guesses_taken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')

    while continue_game not in ('y', 'n'):
        continue_game = input('Do you want to play again? (Y/N)').lower()

    if continue_game.lower() == 'y':
        continue_game = True
    elif continue_game.lower() == 'n':
        continue_game = False

print('Thanks for playing!')
