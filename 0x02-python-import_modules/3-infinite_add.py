#!/usr/bin/python3
import sys

def infinite_add(argv):
    result = 0
    for arg in argv:
        result += int(arg)
    print(result)

if __name__ == "__main__":
    infinite_add(sys.argv[1:])
