import random


def cards():
    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    random_card = random.choice(card)
    return random_card


user_card = []
computer_card = []
u_score = -1
c_score = -1

for _ in range(2):
    user_card.append(cards())
    computer_card.append(cards())



def add_total(all_cards):
    if sum(all_cards) == 21 and len(all_cards) == 2:
        return 0
    if sum(all_cards) > 21 and 11 in all_cards:
        all_cards.remove(11)
        all_cards.append(1)

    return sum(all_cards)


def compare(c_total, u_total):
    if c_total == u_total:
        return "It's a draw"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif c_total > 21:
        return  "Dealer went over, You win"
    elif u_total > 21:
        return "You went over, you lose"
    elif u_total > c_total:
        return "You win"
    else:
        return "You lose, Dealer Win"


is_game_on = False
while not is_game_on:

    u_score = add_total(user_card)
    c_score = add_total(computer_card)


    print(f"Your cards: {user_card}, current score: {u_score}")
    print(f"Computer's first card: {computer_card[0]}")



    if u_score == 0 or c_score == 0 or u_score >= 21:
        #print(f"Your final cards: {user_card}, final score: {u_score}")
        #print(f"Computer's final card: {computer_card}, final score: {c_score}")
        is_game_on = True

    else:
        choices = input("Type Y to continue, Type n to pass: ")[0].lower()
        if choices == 'y':
            user_card.append(cards())
        else:
            is_game_on = True


while c_score != 0 and c_score < 17:
    computer_card.append(cards())
    c_score = add_total(computer_card)

print("\n")
print(f"Your final cards at hand: {user_card}, Your final score: {u_score}")
print(f"Computers final cards at hand: {computer_card},  Computer's final score: {c_score}")
print(compare(c_score, u_score))

