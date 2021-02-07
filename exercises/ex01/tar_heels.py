"""An exercise in remainders and boolean logic."""

__author__ = "730324058"


# Begin your solution here...

x = int(input("Enter an int: "))

if (x% 2 == 0) and (x%7 == 0):
    print("TAR HEELS")
elif x%2 == 0:
    print("TAR")
elif x%7 == 0:
    print("HEELS")
else:
    print("CAROLINA")