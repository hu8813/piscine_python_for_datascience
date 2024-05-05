import sys

def count_characters(text):
    """
    Count the number of upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces in the given text.
    """
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punct_count = sum(1 for char in text if not char.isalnum() and char != ' ')
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace() and char != '\n')

    # Adjust punctuation count to exclude newline character
    punct_count -= text.count('\n')

    return upper_count, lower_count, punct_count, digit_count, space_count

def main():
    """
    Main function of the program. Takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, punctuation
    characters, digits, and spaces. If no argument is provided, prompts the
    user to input a string.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("More than one argument provided")

        if len(sys.argv) == 1 or not sys.argv[1]:
            print("What is the text to count?")
            text = False
            while not text:
                text = input("")
        else:
            text = sys.argv[1]

        upper_count, lower_count, punct_count, digit_count, space_count = count_characters(text)
        total_chars = len(text)
        
        print(f"The text contains {total_chars} characters:")
        print(f"{upper_count} upper letters")
        print(f"{lower_count} lower letters")
        print(f"{punct_count} punctuation marks")
        print(f"{space_count} spaces")
        print(f"{digit_count} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

