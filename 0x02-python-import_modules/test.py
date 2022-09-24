#!/usr/bin/python3
import sys
a = len(sys.argv)
r = 0
print(f"Total Command line arguments passed are:", a)
print("\nArguments that were passed:", end = "")
print("\nName of library:", sys.argv[0])
for x in r(1, a):
    print(sys.argv[x], end = "")
Sum = 0
for y in r(1, a):
    Sum += int(sys.argv[y])
print("\n\nResult:", Sum)
