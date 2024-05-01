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

print(ARG2)
print(ARG3)
print(ARG4)
