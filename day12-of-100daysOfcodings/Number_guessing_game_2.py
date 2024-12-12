import random

EASY_LEVEL = 10
HARD_LEVEL = 5

random_guess_no = random.randint(1,100)
def guess_again():
    return "Guess again!"

def check_win(user_guess, actual_guess, turns):
    if user_guess < actual_guess:
        print("Too low")
        print(guess_again())
        return turns - 1
    elif user_guess > actual_guess:
        print("Too high")
        print(guess_again())
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_guess}")

def set_difficulty():
    levels = input("Choose a difficulty level, Type 'easy' or 'hard': ")
    if levels == 'easy':
      return EASY_LEVEL
    else:
      return HARD_LEVEL

def guessing_game():

    guess = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    level = set_difficulty()

    while guess != random_guess_no:
        print(f"You have {level} attempts remaining to guess the game")
        guess = int(input("Make a guess: "))
        level = check_win(guess, random_guess_no, level)
        if level == 0:
            print("You have run out of guessing, you lose.")
            print(f"The correct guess was: {random_guess_no}")
            return

guessing_game()
