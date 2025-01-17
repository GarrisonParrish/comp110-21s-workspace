"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730324058"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

x = randint(0,2)
print("Your fortune cookie says...")

if x == 1:
    print("A beautiful, smart, and loving person will be coming into your life.")
elif x == 2:
    print("You will get hit by a plane.")
else:
    print("You will gain 300 IQ points.")