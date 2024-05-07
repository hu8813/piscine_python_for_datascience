import sys
import string
from ft_filter import ft_filter

def filter_string(s, n):
    """
    Filter words from string 's' that have a length greater than 'n'.
    """
    try:
        # Check if the input string contains special characters
        assert all(char not in string.punctuation for char in s), "Input string contains special characters"

        # Split the string into words and apply the filter
        return list(ft_filter(lambda word: len(word) > n, s.split()))
    except Exception as e:
        print(f"An error occurred during filtering: {e}")
        return []

def main():
    """
    Main function of the program.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        s, n = sys.argv[1], int(sys.argv[2])
        assert isinstance(s, str) and isinstance(n, int) and n >= 0, "the arguments are bad"

        result = filter_string(s, n)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as ve:
        print(f"ValueError: {ve}")

if __name__ == "__main__":
    main()

