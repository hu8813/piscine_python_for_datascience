import sys
import string
from ft_filter import ft_filter


def filter_string(s, n):
    """filter_string(string or None, integer) --> filter string

Filter words from string 's' that have a length greater than 'n'."""
    try:
        assert all(char not in string.punctuation for char in s), \
            "Input string contains special characters"

        return list(ft_filter(lambda word: len(word) > n, s.split()))
    except Exception as e:
        print(f"An error occurred during filtering: {e}")
        return []


def main():
    """Main function to filter a string based on command-line arguments.

Usage:
    python script.py <string> <integer>

Arguments:
    <string>: A string to be filtered.
    <integer>: The maximum length of the filtered string.

Raises:
    AssertionError: If the arguments are invalid or the input string contains
special characters.
    Exception: If an unexpected error occurs during execution."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
            assert all(char not in string.punctuation for char in s), \
                "Input string contains special characters"
        except ValueError:
            raise AssertionError("the arguments are bad")

        assert isinstance(n, int) and n >= 0, "the arguments are bad"

        result = filter_string(s, n)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as ve:
        print(f"An error occurred: {ve}")


if __name__ == "__main__":
    main()
