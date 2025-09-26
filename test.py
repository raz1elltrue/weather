def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

## Function to reverse a string
def reverse_string(s):
    return s[::-1]

## Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def add(a, b):
    return a + b