#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program converts celsius to fahrenheit

import random


def fahrenheit():

    # input
    print("This program converts degrees celsius to degrees fahrenheit.")
    str_cel = input("Enter degrees in celsius: ")

    # process
    try:
        int_cel = int(str_cel)
        fahrenheit = (9 / 5) * int_cel + 32
        print("{0}°C is equal to {1}°F.".format(int_cel, fahrenheit))
    except ValueError:
        print("Invalid integer.")
    finally:
        print("Thanks for playing!")
    # output

    print("\nDone.")


def main():
    # this function calls the fahrenheit function

    fahrenheit()


if __name__ == "__main__":
    main()
