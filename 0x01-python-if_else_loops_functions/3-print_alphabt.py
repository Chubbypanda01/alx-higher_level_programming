#!/usr/bin/python3
for char in reange(26):
    if char != 4 and char != 16:
        print("{:s}".format(char(char + ord("a"))), end="")
