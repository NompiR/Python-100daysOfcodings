def add(*args):
    sums = 0
    for n in args:
        sums += n
    return sums

print(add(3,4,5))


#or

def adds(*args):
    print(sum(args))

adds(3,4,5)
