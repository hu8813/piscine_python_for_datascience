def count_in_list(lst, item):
    """
    Count occurrences of an item in a list.

    Parameters:
    lst (list): The list to search.
    item: The item to count occurrences of.

    Returns:
    int: The count of occurrences of the item in the list.
    """
    try:
        if not isinstance(lst, list):
            raise TypeError("Parameter 'lst' must be a list")
        if len(lst) == 0:
            raise ValueError("Parameter 'lst' cannot be empty")

        return lst.count(item)
    except TypeError as te:
        print(f"TypeError: {te}")
        return -1  # Return -1 to indicate an error
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return -1  # Return -1 to indicate an error
