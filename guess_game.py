#this is a guess the number game

import random

print('Hello., what is your name?')
name=input()

print('Well, '+name+ ',I am thinking of a number in between 1 and 20.')

secretNumber = random.randint(1,20)

for guessTaken in range(1,7):
    print('Take a guess..')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess is too high., take another guess')
    elif guess < secretNumber:
        print('Your guess is too low., take another guess')
    else:
        break  # for exact guess


if guess ==secretNumber:
    print('Good job, '+name+ '! you guessed my number in '+str(guessTaken)+' guesses!')
else:
    print('Nope. The number I was thinking of was '+str(guess))
