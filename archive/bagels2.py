### PNAME: Bagels
### DESCRIPTION: A letter sequence-guessing game built with Python.
###              This game was adapted from a previous program to use letters
###              instead of numbers. This specific program was made with the
###              help of Al Sweigart's book, "The Big Book of Small Python
###              Projects".
### DATE: 2024-12-24

import random

NUM_LETTERS = 3
MAX_GUESSES = 20

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com


I am thinking of a {}-sized letter sequence with no repeated letters.
Try to guess what it is. Here are some clues:
  Pico      One letter is correct but in the wrong position.
  Fermi     One letter is correct and in the right position.
  Bagels    No letter is correct.

For example, if the secret letter was BDH and your guess was HDC, the
clues would be Fermi Pico.'''.format(NUM_LETTERS))

    while True: # Main game loop
        # This stores the secret number the player needs to guess:
        secretLetter = getSecretLetter()
        print("I have thought up a letter sequence.")
        print(" You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_LETTERS or not guess.isalpha():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")

            guess = guess.upper()
            clues = getClues(guess, secretLetter)
            print(clues)
            numGuesses += 1

            if guess == secretLetter:
                break # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretLetter))

        # Ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith('y'):
            break
        print("Thanks for playing!")


def getSecretLetter():
    """Returns a string made up of NUM_LETTERS unique random letters."""
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # Create a list of letters A to Z.
    random.shuffle(letters) # Shuffle them into random order.

    # Get the first NUM_LETTERS digits in the list for the secret number:
    secretLetter = ''
    for i in range(NUM_LETTERS):
        secretLetter += str(letters[i])
    return secretLetter


def getClues(guess, secretLetter):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret letter pair."""
    if guess == secretLetter:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretLetter[i]:
            # A correct letter is in the correct place.
            clues.append("Fermi")
        elif guess[i] in secretLetter:
            # A correct letter is in the incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # There are no correct letters at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
        
