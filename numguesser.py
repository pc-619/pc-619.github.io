### PNAME: Number-Guessing Game
### DESCRIPTION: Simple number guessing game written in Python.
### DATE: 2024-12-21

from random import *

# initialize variables
attempt = 1
guess = 0
response = ''
rnum = randint(1,1000)

while(response.upper() != 'N'):

    # check every time while loop resets to see if user exceeded attempt limit
    if attempt > 10:
        print("You lose!")
        while(response != 'Y' and response != 'N'):
            print("The number was ", rnum, ". Play again? (Y/N) ", sep='', end='')
            response = str(input()).upper()
            if response == 'Y':
                response = ''
                rnum = random.randint(1,1000)
                attempt = 1
                break
            elif response == 'N':
                break
            else:
                print("Invalid response.")

    # start game
    if attempt <= 10:
        print("GUESS #", attempt, sep='')
        guess = int(input("Guess the number from 1-1000: "))

    if guess > 1000 or guess < 1:
        print("Invalid input. Please limit your guess to 1-1000.")
        
    elif guess > rnum and attempt <= 10:
        print("Lower.")
        attempt += 1

    elif guess < rnum and attempt <= 10:
        attempt += 1
        print("Higher.")
        
    elif guess == rnum and attempt <= 10:
        print("You win!")
        while(response != 'Y' and response != 'N'):
            print("The number was ", rnum, ". Play again? (Y/N) ", sep='', end='')
            response = str(input()).upper()
            if response == 'Y':
                response = ''
                rnum = randint(1,1000)
                attempt = 1
                break
            elif response == 'N':
                break
            else:
                print("Invalid response.")
