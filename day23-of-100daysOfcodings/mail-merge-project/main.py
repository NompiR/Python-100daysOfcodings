PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as f_names:
    txt_names = f_names.readlines()

with open("Input/Letters/starting_letter.docx", "r") as f:
    txt = f.read()
    for name in txt_names:
        stripped_names = name.strip()
        txt_s = txt.replace(PLACEHOLDER, stripped_names)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as file_write:
            file_write.write(txt_s)
            #print(txt_names)













"""txt_file = str(txt).strip("[ ' ', '\n',]")
with open(f"./Output/ReadyToSend/exampl-at.txt", "w") as file_write:
    file_write.write(txt_file)

f_names = open("./Input/Names/invited_names.txt", "r")
txt_names = f_names.readlines()
print(txt_file)
"""
