import sys


def encode_to_morse(string):
    """encode_to_morse(str) --> str

Encode a string into Morse code.

Parameters:
string (str): The string to encode.

Returns:
str: The encoded Morse code."""
    MORSE_DICT = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
        "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
        "Z": "--.. ", "0": "----- ", "1": ".---- ", "2": "..--- ",
        "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ",
        "7": "--... ", "8": "---.. ", "9": "----. "
    }
    try:
        morse_code = ""
        for char in string.upper():
            if char in MORSE_DICT:
                morse_code += MORSE_DICT[char]
            else:
                raise AssertionError("the arguments are bad")
        return morse_code.strip()
    except AssertionError as e:
        return f"AssertionError: {e}"


def main():
    try:
        assert (len(sys.argv) == 2 and isinstance(sys.argv[1], str)), \
           ("the arguments are bad")
        encoded_string = encode_to_morse(sys.argv[1])
        print(encoded_string)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
