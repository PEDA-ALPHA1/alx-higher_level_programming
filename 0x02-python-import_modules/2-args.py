#!/usr/bin/python3
if __name__ == "__main__":
    import sys
a = len(sys.argv)
if (a <= 1):
    print("0 arguments.".format(a))
elif (a == 2):
    print("{} argument:".format(a - 1))
else:
    print("{} arguments:".format(a - 1))
for index in range(1, a):
    print("{}: {}".format(index, sys.argv[index]))
