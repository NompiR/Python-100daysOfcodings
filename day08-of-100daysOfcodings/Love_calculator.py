def calculate_love_score(name1, name2):
    word = "true"
    words = name1 + name2
    count_true1 = 0
    for i in word:
        #print(i)
        for j in words:
            count_true1 += j.count(i)
    #print(count_true)

    word = "love"
    words = name1 + name2
    count_true2 = 0
    for i in word:
        # print(i)
        for j in words:
            count_true2 += j.count(i)
    print(str(count_true1) + str(count_true2))


calculate_love_score(name1="Kanye West", name2="Kim Kardashian")
