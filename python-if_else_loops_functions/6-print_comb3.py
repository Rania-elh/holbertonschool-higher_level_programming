#!/usr/bin/python3
for numberfirst in range(0, 9):
    for numbersecond in range(numberfirst + 1, 10):
        if (numberfirst != 8 or numbersecond != 9):
            print("{}{}".format(numberfirst, numbersecond), end=", ")
        else:
            print("{}{}".format(numberfirst, numbersecond))
