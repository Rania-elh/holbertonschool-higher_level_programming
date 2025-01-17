#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        display = ""
        if (i % 3) == 0:
            display += "Fizz"
        if (i % 5) == 0:
            display += "Buzz"

        print("{}".format(display if display else i), end=" ")
