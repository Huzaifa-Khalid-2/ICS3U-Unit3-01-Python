#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program shows formatting output


def main():
    # this function shows formatting output

    # input
    number_1 = int(input("Insert any number (integers): "))
    number_2 = int(input("Insert any number (integers): "))

    # process
    total = number_1 + number_2

    # output
    print("")
    print("{0} + {1} = {2}".format(number_1, number_2, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
