import random
import math


def number_guessing_game():
    # Get lower and upper bounds from the user
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    # Generate a random number within the specified range
    random_number = random.randint(lower_bound, upper_bound)

    # Calculate the maximum number of guesses using the formula
    max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))

    print(f"You have {max_guesses} attempts to guess the number between {lower_bound} and {upper_bound}.")

    # Initialize the number of guesses
    guess_count = 0

    while guess_count < max_guesses:
        guess = int(input("Enter your guess: "))
        guess_count += 1

        if guess > random_number:
            print("Try Again! You guessed too high.")
        elif guess < random_number:
            print("Try Again! You guessed too small.")
        else:
            print("Congratulations! You guessed the number correctly.")
            break

    if guess_count == max_guesses and guess != random_number:
        print("Better Luck Next Time! You've used all your guesses.")
    elif guess == random_number and guess_count <= max_guesses:
        print(f"Congratulations! You guessed the number in {guess_count} tries.")


#run the game
number_guessing_game()

