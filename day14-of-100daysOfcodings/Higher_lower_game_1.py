import random
from game_data import data

def display_fields(accounts):
    accounts_name = accounts['name']
    accounts_disc = accounts["description"]
    accounts_count = accounts['country']
    return f"{accounts_name}, a {accounts_disc} from {accounts_count}"

def check_win(u_guess, a, b):
    if a > b:
        return u_guess == "a"
    else:
        return  u_guess == "b"

score = 0
is_game_continue = True
account_b = random.choice(data)

while is_game_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {display_fields(account_a)}")
    print("VS")
    print(f"Against B: {display_fields(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()[0]

    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']

    is_check = check_win(guess, follower_count_a, follower_count_b)
    print('\n' * 20)
    if is_check:
        score += 1
        print(f"You are right! Current score {score}")
    else:
        print(f"You are wrong. Final score {score}")
        is_game_continue = False


