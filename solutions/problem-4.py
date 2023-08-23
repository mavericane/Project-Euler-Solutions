def ispalindrome(number):
    number = str(number)
    if number == number[-1::-1]:
        return True
    else:
        return False

biggest_palindrome_number = 0
for i in range(100,999+1):
    for j in range(100,999+1):
        if ispalindrome(i*j) and (i*j) > biggest_palindrome_number:
            biggest_palindrome_number = i*j

print(biggest_palindrome_number)