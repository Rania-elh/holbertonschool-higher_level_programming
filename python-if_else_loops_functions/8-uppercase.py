#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        s = str[i]
        unicode = ord(s)
        if unicode >= 97 and unicode <= 122:
            s = chr(unicode - 32)
        print("{:s}".format(s), end="")
    print("")
