#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2):
        c = i - 32
        print("{:c}".format(c), end="")
    else:
        print("{:c}".format(i), end="")
