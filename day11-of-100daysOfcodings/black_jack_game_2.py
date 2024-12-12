import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) >= 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw "
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "Opponent went over, You Win!"
    elif u_score > c_score:
        return "You Win! :-D"
    else:
        return "You lose "


user_card = []
computer_card = []
computer_score = -1
user_score = -1

is_game_over = False


for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)


    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer card {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_deal = input("Type y to get another card, n to pass: ")[0]
        if user_deal == 'y':
            user_card.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)
    #print(f"Comp score {computer_score}")


print(f"Your final cards: {user_card} Your final score: {user_score}")
print(f"Computer's final cards: {computer_card} Computer's final score: {computer_score}")
print(compare(user_score, computer_score))


    
