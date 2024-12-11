import random
words = ["Dog", "Cow", "Horse", "Goat", "Jackal", "Armadillo", "Eel", "Goose", "Wolf", "Beagle", "Gorilla", "Monkey", "Beaver", "Orangutan", "Bat"]
computer_choose_word = random.choice(words).lower()

word_length = len(computer_choose_word)

empty_word = "_" * word_length

#print( computer_choose_word)

is_hangman_game_true = True

correct_letter = []
count_of_lives = 6

while is_hangman_game_true:
    guessed = ""

   print(f"********* {count_of_lives}/6 LIVE LEFT **********")
    print(f"Word to guess: {empty_word}")
    guess = input("Guess a letter: ")
    for letters in computer_choose_word:
        if letters == guess:
            guessed += letters
            correct_letter.append(guess)

        elif letters in correct_letter:
            guessed += letters

        else:
            guessed += "_"

    if "_" not in guessed:
        print("You Saved Lives!")
        is_hangman_game_true = False

    if guess not in computer_choose_word:
        count_of_lives -= 1
        if count_of_lives == 0:
            print(f"**************************IT WAS {computer_choose_word} YOU LOST*************************")
            is_hangman_game_true = False

    print(f"Correct guessed ", {guessed})
