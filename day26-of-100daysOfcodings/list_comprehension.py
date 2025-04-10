numbers = [2, 3, 4]

new_list = [n + 1 for n in numbers]

print(new_list)


#Just like that

new_lists = []

for n in numbers:
    add_1s = n + 1
    new_lists.append(add_1s)

print(new_lists)


#Just like range(1, 5)
new_range_list = [n * 2 for n in range(1, 5)]
print(new_range_list)


#Just like Alphabet to letters
name = "Nompi"
new_letter_list = [n for n in name]
print(new_letter_list)


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
#new_lists_of_names = [word for word in names if word == 'Elanor']
new_lists_of_names = [word.upper() for word in names if len(word) > 5]
print(new_lists_of_names)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)


file_path = "file1.txt"
file_path2 = "file2.txt"
file = open(file_path, "r")
file1 = open(file_path2, "r")
content = file.readlines()
content1 = file1.readlines()
list1 = []
list2 = []
for n in content1:
    list1.append(n.strip())
for n1 in content:
    list2.append(n1.strip())

num1_list = [int(num) for num in list1]
num2_list = [int(num) for num in list2]

result = list(set(num1_list).intersection(set(num2_list)))
print('result: ', result)

#similar to the above code but this one is ordered lists

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)
