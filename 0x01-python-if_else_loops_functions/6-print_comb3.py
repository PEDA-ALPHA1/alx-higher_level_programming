#!/usr/bin/python3
for num in range(0, 9):
    for comb in range(num + 1, 10):
        if num == 8:
            print("{}{}".format(num, comb))
        else:
            print("{}{}".format(num, comb), end=", ")
