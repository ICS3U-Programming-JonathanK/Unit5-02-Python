#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 2, 2021
# This program uses user defined functions to calculate the area of a triangle


def calculate_area(base_from_user_int, height_from_user_int):
    # calculate area
    # process
    area = (base_from_user_int * height_from_user_int)/2
    # output
    print("The area is {0} cm²".format(area))


def main():
    print("Today, we will calculate the area of a triangle")
    print("")
    while True:
        # this function gets length and width
        base_from_user_string = input("Enter the base of a triangle (cm): ")

        # make sure if the user types anything but an integer, it's not valid
        try:
            base_from_user_int = float(base_from_user_string)
            print("")
            if (base_from_user_int <= 0):
                print("{} is not a"
                      " positive number". format(base_from_user_int))
            else:
                break
        except ValueError:
            print("{} is not a valid number". format(base_from_user_string))
    while True:
        # this function gets length and width
        height_from_user_string = input("Enter "
                                        "the height of a triangle (cm): ")

        # make sure if the user types anything but an integer, it's not valid
        try:
            height_from_user_int = float(height_from_user_string)
            print("")
            if (height_from_user_int <= 0):
                print("{} is not a "
                      "positive number". format(height_from_user_int))
            else:
                print("")
                break
        except ValueError:
            print("{} is not a valid number". format(height_from_user_string))
    calculate_area(base_from_user_int, height_from_user_int)


if __name__ == "__main__":
    main()
