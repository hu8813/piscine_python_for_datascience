import sys


def count_characters(text):
    """
    Count the number of upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces in the given text.
    """
    upper_c = sum(1 for char in text if char.isupper())
    lower_c = sum(1 for char in text if char.islower())
    punct_c = sum(1 for char in text if not char.isalnum() and char != ' ')
    digit_c = sum(1 for char in text if char.isdigit())
    space_c = sum(1 for char in text if char.isspace() and char != '\n')

    punct_c -= text.count('\n')

    return upper_c, lower_c, punct_c, digit_c, space_c


def main():
    """
    Main function of the program. Takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, punctuation
    characters, digits, and spaces. If no argument is provided, prompts the
    user to input a string.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument provided")

        if len(sys.argv) == 1 or not sys.argv[1]:
            print("What is the text to count?")
            text = False
            while not text:
                text = sys.stdin.readline()
        else:
            text = sys.argv[1]

        upper_c, lower_c, punct_c, digit_c, space_c = count_characters(text)
        total_chars = len(text)

        print(f"The text contains {total_chars} characters:")
        print(f"{upper_c} upper letters")
        print(f"{lower_c} lower letters")
        print(f"{punct_c} punctuation marks")
        print(f"{space_c} spaces")
        print(f"{digit_c} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
