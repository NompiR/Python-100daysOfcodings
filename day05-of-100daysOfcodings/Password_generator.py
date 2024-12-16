import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""EASY LEVEL"""

random_gen = ""
for _ in range(nr_letters):
    random_gen += random.choice(letters)

for _ in range(nr_symbols):
    random_gen += random.choice(symbols)

for _ in range(nr_numbers):
    random_gen += random.choice(numbers)

#Sequence of unordered lists of set of unique lists
random_Set_pass_generator = list(set(random_gen))
print(f"Unordered set of unique lists: {random_Set_pass_generator}")

#Unordered lists
random_Set_pass_generator_lists = list(random_gen)
print(f"Unordered lists: {random_Set_pass_generator_lists}")

#Random ordered lists using sorted lists
random_Set_pass_generator = list(sorted(random_gen))
print(f"Ordered lists by sorted: {random_Set_pass_generator}")


#Random shuffles
random.shuffle(random_Set_pass_generator_lists)
print(f"Random shuffle lists: {random_Set_pass_generator_lists}")


your_pass = ""
for i in range(len(random_Set_pass_generator)):
    your_pass += random_Set_pass_generator_lists[i]


print(f"Your password is: {your_pass}")


"""HARD LEVEL"""

def random_shuffles(pass_list):
    random.shuffle(pass_list)
    return pass_list


password_lists = []
for _ in range(nr_letters):
    password_lists.append(random.choice(letters))

for _ in range(nr_symbols):
    password_lists.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_lists.append(random.choice(numbers))


print(password_lists)
password_random_shuffles = random_shuffles(pass_list=password_lists)
print(password_random_shuffles)

password = ""

for char in password_random_shuffles:
    password += char


print(f"Your password is: {password}")

