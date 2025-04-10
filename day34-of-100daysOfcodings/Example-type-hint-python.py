
def police_check(age: int) -> bool:
    """if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive"""
    return age > 18

def vehicle(type_of_vehicle: str) -> bool:
    data = ['car', 'bus', 'motorbike', 'lorry', 'bicycle']
    return type_of_vehicle in data

def customer_details():
    pass

my_input_age = int(input("What is your age?: "))


if police_check(my_input_age):
    print("You can pass.")
    print(vehicle('car'))
else:
    print("Pay a fine. ")






