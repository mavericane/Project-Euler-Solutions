import math


def isprime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    else:
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
        return True


counter = 0
number = 0
while True:
    if isprime(number):
        counter += 1
        if counter == 10001:
            break

    number += 1


print(number)
