def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    while True:
        n += 1
        if is_palindrome(n):
            return n

# Test the function
numbers = [13, 15]
for num in numbers:
    if is_prime(num):
        print(f"{num} is a prime number. Next palindrome is {next_palindrome(num)}")
    else:
        print(f"{num} is not a prime number")
