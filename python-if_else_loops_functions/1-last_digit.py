#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# pour obtenir le dernier numéro
if number >= 0:
    last_di = number % 10
else:
    last_di = number % -10

# affiche un message approprié en fonction de la  valeur de last_digit.
if last_di > 5:
    result = "greater than 5"
elif last_di == 0:
    result = "0"
else:
    result = "less than 6 and not 0"

print(f"Last digit of {number} is {last_di} and is {result}")
