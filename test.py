"""
    Module containing utility functions for basic operations.

    Functions:
        calculate_average(numbers): Calculate the average of a list of numbers.
        reverse_string(s): Reverse the given string.
        is_prime(n): Check if a number is prime.
        add(a, b): Add two numbers and return the result.

    Reads and prints the contents of 'file.txt'.
    """

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


with open("file.txt", "r") as file:
    # Read the file and print the content
    contents = file.read()
    print(contents)