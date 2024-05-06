import sys

def encode_to_morse(string):
    """
    Encode a string into Morse code.

    Parameters:
    string (str): The string to encode.

    Returns:
    str: The encoded Morse code.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ", "F": "..-. ",
        "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ",
        "S": "... ", "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
        "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
    }
    try:
        morse_code = ""
        for char in string.upper():
            if char in NESTED_MORSE:
                morse_code += NESTED_MORSE[char]
            else:
                raise AssertionError("the arguments are bad")
        return morse_code.strip()
    except AssertionError as e:
        return f"AssertionError: {e}"

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
        encoded_string = encode_to_morse(sys.argv[1])
        print(encoded_string)
        return 0
    except AssertionError as e:
        print(e)
        return 1

