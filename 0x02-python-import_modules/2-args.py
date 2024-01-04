#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_args = len(argv)

    # Print the number of arguments
    print(f"{num_args} argument{'s' if num_args != 1 else ''}:", end='')

    if num_args > 0:
        print()

        # Print each argument and its position
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

    else:
        print(".")


if __name__ == "__main__":
    # Exclude the script name (sys.argv[0]) from the printed arguments
    print_arguments(sys.argv[1:])
