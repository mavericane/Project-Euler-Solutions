sum_of_squares = 0
sum = 0
for number in range(100 + 1):
    sum += number
    sum_of_squares += number**2

square_of_sum = sum**2

result = square_of_sum - sum_of_squares

print(result)
