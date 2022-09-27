#!/usr/bin/python3
if __name__ == "__main__":
    import sys
a = len(sys.argv)
"""Addition of Arguments"""
Sum = 0
for index in range(1, a):
    Sum += int(sys.argv[index])

print("{}".format(Sum))
