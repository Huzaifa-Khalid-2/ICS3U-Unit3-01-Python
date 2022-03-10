#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program shows formatting output


def main():
    # this function shows formatting output

    # input
    Number_1 = int(input("Insert any number (integers): "))
    Number_2 = int(input("Insert any number (integers): "))

    # process
    total = Number_1 + Number_2

    # output
    print("")
    print("{0} + {1} = {2}".format(Number_1, Number_2, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
