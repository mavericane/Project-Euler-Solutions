import math


def prime_factor(number):
    if number < 2:
        print("Your entered number is smaller than first prime number!")
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return i
        return number


number = 600851475143

while True:
    prime = prime_factor(number)

    if prime < number:
        number //= prime
    else:
        print(number)
        break
