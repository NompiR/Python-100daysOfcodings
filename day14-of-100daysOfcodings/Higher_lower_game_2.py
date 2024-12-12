import random
from arts import logo_higher_lower_game, logo_higher_lower_vs_game
from game_data import data

def choice_play(my_data):
    '''Choice random data from dict'''
    return random.choice(my_data)

#choices = random.choice(data)

def display_data(index, my_display_data):
    ''' Display each dict lists '''
    return f"{my_display_data[index]['name']}, a {my_display_data[index]['description']}, from {my_display_data[index]['country']}"


my_choices = []
for i in range(0, len(data)):
    my_choices.append(data[i]['name'])



def play():
    is_play = False
    count = 0
    index2 = random.randint(0, len(my_choices) - 1)
    while not is_play:


        index1 = index2
        index2 = random.randint(0, len(my_choices) - 1)



        while index1 == index2:
            index2 = random.randint(0, len(my_choices) - 1)


        #print(my_choices[index1])
        print(logo_higher_lower_game)
        print(display_data(index1, data))

        print(logo_higher_lower_vs_game)

        #print(my_choices[index2])
        print(display_data(index2, data))
        print('\n')

        #clear_console()

        who_ab = input("Who is more follower 'A' or , 'B': ").upper()[0]

        print('\n' * 20)


        if who_ab == 'A':

            if data[index1]['follower_count'] > data[index2]['follower_count'] and who_ab == 'A':
                count += 1
                print('\n')
                print(f"Yes, You ara right, current score {count}")
                #print('\n' * 20)

            else:
                print(f"No Sorry that is wrong, final score {count}")
                is_play = True
        else:
            #print(data[index1]['follower_count'])
            #print(data[index2]['follower_count'])
            if data[index2]['follower_count'] > data[index1]['follower_count']:
                count += 1
                print('\n')
                print(f"Yes, You ara right, current score {count}")


            else:
                print(f"No Sorry that is wrong, final score {count}")
                is_play = True


play()
