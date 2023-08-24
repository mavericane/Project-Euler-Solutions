import math

lcm = 1
for number in range(1,20+1):
    lcm *= number // math.gcd(number, lcm)

print(lcm)