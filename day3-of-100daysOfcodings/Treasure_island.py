print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_one = input('you\'re at a crossroad, where do you want to go? Type "left" or "right".: ').lower()
if choice_one == "left":
    choice_two = input('You\'ve come to a lake.'
    'There is an island in the middle of the lake.'
    'Type "wait" to wait for a boat.'
    'Type "swim" to swim across.: ').lower()
    if choice_two == "wait":
        choice_three = input("You arrived at the island unharmed. There is house with 3 doors. one red, one yellow, and one blue. Which color do you choose?: ").lower()
        if choice_three == "red":
            print("It\'s a room full of fire. Game Over!")
        elif choice_three == "yellow":
            print("You found the treasure. You Win!")
        elif choice_three == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You choose a door that doesn\'t exist. Game Over! ")
    else:
        print("You got attacked by an angry trout. Game over!")
else:
    print("You fell in to a hold. Game over!")
