def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return True

#isprime = is_prime(73)
if not is_prime(75):
    print("Prime")
else:
    print("Not prime")
