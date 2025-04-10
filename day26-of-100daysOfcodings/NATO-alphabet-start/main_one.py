import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_alphabets = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabets)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [nato_alphabets[letter] for letter in word]
print(output_list)
