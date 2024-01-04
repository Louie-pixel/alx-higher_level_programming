#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_str = "{:d} argument"
    argc = len(sys.argv) - 1

    if argc == 0:
        arg_str += 's.'
    elif argc == 1:
        arg_str += ':'
    else:
        arg_str += 's:'
    print(arg_str.format(argc))

    for i in range(1, argc + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
