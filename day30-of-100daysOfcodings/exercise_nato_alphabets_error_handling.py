import pandas

data = pandas.read_csv("../days26-of-100daysOfcodings/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
def generate_phonetic():
    try:
        user_input = input("Enter a word: ").upper()
        nato_lists = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please. ")
        generate_phonetic()
    else:
        print(nato_lists)


generate_phonetic()
