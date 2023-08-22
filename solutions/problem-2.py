fibonacci = [1,2]
sum = 2
while True:
    new_number = fibonacci[-1] + fibonacci[-2]
    if new_number <= 4000000:
        fibonacci.append(new_number)
        if new_number % 2 == 0:
            sum+=new_number
    else:
        break

print(fibonacci[-1])
print(sum)