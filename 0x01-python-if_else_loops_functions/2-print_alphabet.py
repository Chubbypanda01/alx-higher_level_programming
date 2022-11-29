#!/usr/bin/python3
for char in range(26):
    print("{:s}".format(char(char + ord("a"))), end="")
