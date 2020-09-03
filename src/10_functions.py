# Write a function is_even that will return true if the passed-in number is even.

from random import randint

# Theorem:
# The sum of m consecutive integers is divisible by m if and only if m is odd

def is_even(num):
    total = 0
    start = randint(0, 1_000_000)
    for v in range(start, start + num):
        total += v
    
    return False if total % num == 0 else True

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

print("Even!" if is_even(num) else "Odd!")
