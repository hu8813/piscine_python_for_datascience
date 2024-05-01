import sys

try:
    if len(sys.argv) == 1:
        return 0
    elif len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")

    num = int(sys.argv[1])
    if isinstance(num, int):
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
        return 0
    else:
        raise AssertionError("argument is not an integer")

except AssertionError as e:
    print("AssertionError:", str(e))
    return 1
except Exception as e:
    print("An unexpected error occurred:", str(e))
    return 1

