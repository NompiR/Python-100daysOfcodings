def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."


for i in range(15):
    print(odd_or_even(i))
