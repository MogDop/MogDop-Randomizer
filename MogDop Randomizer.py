import random
import os
import sys
import time

def typewriter(text, delay=0.03, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def change():
    while True:
        print("--------------------------------")
        typewriter("Welcome to MogDop's Randomizer!")
        print()
        typewriter('Change Mode.')
        typewriter('    1 - Number Randomizer')
        typewriter('    2 - Word Randomizer')
        typewriter('    3 - Dice Roller')
        typewriter('    4 - Exit')
        typewriter('Choose a function: ', newline=False)

        userchange = input().strip()

        if userchange == '1':
            NumRandomizer()
        elif userchange == '2':
            WordRandomizer()
        elif userchange == '3':
            DiceRoller()
        elif userchange == '4':
            typewriter('Exiting the Multi-Randomizer. Goodbye!')
            print("--------------------------------")
            os._exit(0)
        else:
            typewriter('Invalid choice. Please try again.')


def NumRandomizer():
    print("--------------------------------")
    typewriter('Welcome to Number Randomizer!')
    while True:
        print()
        typewriter("Type 'exit' anytime to quit Number Randomizer.", newline=False)
        print()


        lower_input = input("Enter the lower bound: ")
        if lower_input.lower() == "exit":
            typewriter('Exiting the Randomizer. Goodbye!')
            change()
            return
        try:
            lower = int(lower_input)
        except ValueError:
            typewriter("Please enter a valid number!")
            continue

        upper_input = input("Enter the upper bound: ")
        if upper_input.lower() == "exit":
            typewriter('Exiting the Randomizer. Goodbye!')
            change()
            return
        try:
            upper = int(upper_input)
        except ValueError:
            typewriter("Please enter a valid number!")
            continue

        if upper < lower:
            typewriter("Upper bound must be greater than or equal to lower bound!")
            continue

        typewriter(f'Generating a random number between {lower} and {upper}...')
        typewriter(str(random.randint(lower, upper)))



def WordRandomizer():
    print("--------------------------------")
    typewriter('Welcome to Word Randomizer!')
    while True:
        print()
        typewriter("Type 'exit' anytime to quit Word Randomizer.", newline=False)
        print()

        words_input = input("Enter words separated by commas: ")
        if words_input.lower() == "exit":
            typewriter('Exiting the Randomizer. Goodbye!')
            print("--------------------------------")
            change()
            return

        words = [word.strip() for word in words_input.split(',') if word.strip()]
        if not words:
            typewriter("You must enter at least one word!")
            continue

        typewriter('Generating a random word from your list...')
        typewriter(random.choice(words))

def DiceRoller():
    print("--------------------------------")
    typewriter('Welcome to Dice Roller!')
    while True:
        print()
        typewriter("type 'exit' for Exit Dice Roller.", newline=False)
        print()

        num_dice_input = input("Enter the number of dice: ")
        if num_dice_input.lower() == 'exit':
            change()
            return
        try:
            num_dice = int(num_dice_input)
        except ValueError:
            typewriter("Please enter a valid number!")
            continue

        num_sides_input = input("Enter the number of sides per die: ")
        if num_sides_input.lower() == 'exit':
            change()
            return
        try:
            num_sides = int(num_sides_input)
        except ValueError:
            typewriter("Please enter a valid number!")
            continue

        typewriter(f'Rolling {num_dice}d{num_sides}...')
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        typewriter('You rolled: ' + ', '.join(map(str, rolls)))



change()
