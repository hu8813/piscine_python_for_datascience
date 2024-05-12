import sys

try:
    if len(sys.argv) == 1:
        exit(0)
    elif len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    arg = sys.argv[1]
    if not arg.isdigit():
        raise AssertionError("argument is not an integer")

    num = int(arg)
    if isinstance(num, int):
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
        exit(0)
    else:
        raise AssertionError("argument is not an integer")

except AssertionError as e:
    print("AssertionError:", str(e))
    exit(1)
except Exception as e:
    print("An unexpected error occurred:", str(e))
    exit(1)

