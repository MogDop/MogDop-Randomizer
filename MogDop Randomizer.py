import random
import sys
import time

def typewriter(text, delay=0.03, newline=True):
    """Печатает текст с эффектом пишущей машинки."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def print_separator():
    print("--------------------------------")

def main_menu():
    while True:
        print_separator()
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
            num_randomizer()
        elif userchange == '2':
            word_randomizer()
        elif userchange == '3':
            dice_roller()
        elif userchange == '4':
            typewriter('Exiting the Multi-Randomizer. Goodbye!')
            print_separator()
            sys.exit(0)
        else:
            typewriter('Invalid choice. Please try again.')

def num_randomizer():
    print_separator()
    typewriter('Welcome to Number Randomizer!')
    while True:
        print()
        typewriter("Type 'exit' anytime to quit Number Randomizer.", newline=False)
        print()
        lower_input = input("Enter the lower bound: ")
        if lower_input.lower() == "exit":
            typewriter('Exiting the Randomizer. Goodbye!')
            return
        try:
            lower = int(lower_input)
        except ValueError:
            typewriter("Please enter a valid number!")
            continue

        upper_input = input("Enter the upper bound: ")
        if upper_input.lower() == "exit":
            typewriter('Exiting the Randomizer. Goodbye!')
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

def word_randomizer():
    print_separator()
    typewriter('Welcome to Word Randomizer!')
    while True:
        print()
        typewriter("Type 'exit' anytime to quit Word Randomizer.", newline=False)
        print()
        words_input = input("Enter words separated by commas: ")
        if words_input.lower() == "exit":
            typewriter('Exiting the Randomizer. Goodbye!')
            print_separator()
            return

        words = [word.strip() for word in words_input.split(',') if word.strip()]
        if not words:
            typewriter("You must enter at least one word!")
            continue

        typewriter('Generating a random word from your list...')
        typewriter(random.choice(words))

def dice_roller():
    print_separator()
    typewriter('Welcome to Dice Roller!')
    while True:
        print()
        typewriter("Type 'exit' for Exit Dice Roller.", newline=False)
        print()

        num_dice_input = input("Enter the number of dice (1-100): ")
        if num_dice_input.lower() == 'exit':
            return
        try:
            num_dice = int(num_dice_input)
            if not 1 <= num_dice <= 100:
                typewriter("Number of dice must be between 1 and 100!")
                continue
        except ValueError:
            typewriter("Please enter a valid number!")
            continue

        num_sides_input = input("Enter the number of sides per die (2-1000): ")
        if num_sides_input.lower() == 'exit':
            return
        try:
            num_sides = int(num_sides_input)
            if not 2 <= num_sides <= 1000:
                typewriter("Number of sides must be between 2 and 1000!")
                continue
        except ValueError:
            typewriter("Please enter a valid number!")
            continue

        typewriter(f'Rolling {num_dice}d{num_sides}...')
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        typewriter('You rolled: ' + ', '.join(map(str, rolls)))

if __name__ == "__main__":
    main_menu()