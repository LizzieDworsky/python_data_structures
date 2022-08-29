

# Problem 1 - Happy Numbers

"""
https://en.wikipedia.org/wiki/Happy_number 

A happy number is a number defined by the following process: 
Start with any positive integer
Replace the number by the sum of the squares of its digits
Repeat the process until the number equals 1. 


Write a method that determines if a number is happy or sad 

Example Input: 13
Example Output: "13 is a Happy Number!"

Example Input: 22
Example Output: "22 is a Sad Number :("
"""

def happy_number_checker(potential_happy_number):
    try:
        int(potential_happy_number)
        new_number = 0
        while new_number != 1 or new_number != potential_happy_number:
            split_numbers = []
            

    except ValueError:
        print(f"{potential_happy_number}, didn't work. Please try again:")
        happy_number_checker(input("Enter your new number here: "))

happy_number_checker(input("Enter a number to see if it is Happy: "))

# Problem 2 - Prime Numbers

"""
A prime number is a number that is only divisible by one and itself. 
Write a method that prints out all prime numbers between 1 and 100  
"""


def print_prime_numbers():
    pass


# Problem 3 - Fibonacci

"""
A Fibonacci is a series of numbers in which each number is the sum of the two preceding numbers. 
The simplest is the series 1, 1, 2, 3, 5, 8, etc. 
Write a method that does the Fibonacci sequence starting at 1 

HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs 
"""


def fibonacci():
    pass
