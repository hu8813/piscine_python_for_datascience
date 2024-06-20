import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D array and returns the truncated version based on
    start and end.

    Args:
        family (list): 2D list to be sliced.
        start (int): Starting index for slicing.
        end (int): Ending index for slicing.

    Returns:
        list: Sliced 2D list.
    """
    assert isinstance(family, list), "Input must be a list"
    assert all(isinstance(row, list) for row in family), \
        "Input must be a 2D list"
    row_length = len(family[0])
    assert all(len(row) == row_length for row in family), \
        "All rows must have the same length"
    assert -len(family) <= start < len(family), "Invalid start index"
    assert -len(family) <= end <= len(family), "Invalid end index"
   

    try:
        family_np = np.array(family)
        print("My shape is:", family_np.shape)

        sliced_family_np = family_np[start:end]
        print("My new shape is:", sliced_family_np.shape)

        return sliced_family_np.tolist()
    except Exception as e:
        print("Error occurred during slicing:", e)
        return []


def main():
    pass


if __name__ == "__main__":
    main()
