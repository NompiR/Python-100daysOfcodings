def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
  
if not is_prime(75):
    print("It's a Prime number")
else:
    print("It's not prime number")
