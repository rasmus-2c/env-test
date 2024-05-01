'''
import sys

def print_three_arguments(arg1, arg2, arg3):
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)
    print("Argument 3:", arg3)

if __name__ == "__main__":
    # Check if exactly 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <arg1> <arg2> <arg3>")
        sys.exit(1)

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    print_three_arguments(arg1, arg2, arg3)
'''

import os

def main():
    var1 = os.environ.get('VAR1')
    var2 = os.environ.get('VAR2')
    var3 = os.environ.get('VAR3')
    
    print("VAR1:", var1)
    print("VAR2:", var2)
    print("VAR3:", var3)

if __name__ == "__main__":
    main()

