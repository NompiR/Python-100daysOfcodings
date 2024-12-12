import random

from arts import logo_guess_the_number

def numbers():
    r = random.randint(1, 101)
    return r


def guessing(level):
    while True:
        print(f"You have {level} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        if level > 1:

            if guess == guessed_no:
                print(f"You got it! The answer was {guess}.")
                break
            elif guess >= guessed_no:
                print("Too high")
                print("Guess again")
            elif guess <= guessed_no:
                print("Too low")
                print("Guess again")
            else:
                print("Your guess average no")

            level -= 1
        else:
            print(f"You have run out of guesses, you lose.")
            break


print(logo_guess_the_number)
guessed_no = numbers()
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
choice = input("Choose a difficult. Type 'easy' or 'hard': ")
#print(f"your right guess: {guessed_no}")
if choice == 'easy':
    guessing(10)
else:
    guessing(5)

