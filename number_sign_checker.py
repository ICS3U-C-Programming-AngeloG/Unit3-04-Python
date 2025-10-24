#!/usr/bin/env python3

# Created by: Angelo Garcia
# Created on: October 23rd, 2025
# This program asks the user for an integer and tells if it is positive, negative, or zero


def main():
    # ask the user to enter an integer
    number = int(input("Enter an integer: "))
    print("")

    # check if the number is positive
    if number > 0:
        print(f"{number} is a positive number")
    # check if the number is negative
    elif number < 0:
        print(f"{number} is a negative number")
    # if it is neither positive nor negative, it must be zero
    else:
        print(f"{number} is just zero!")


if __name__ == "__main__":
    main()
