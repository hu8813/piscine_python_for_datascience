def ft_filter(func, items=None):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    try:
        if items is None:
            raise ValueError("No items provided")

        if func:
            return (item for item in items if func(item))
        else:
            return (item for item in items if item)
    except TypeError:
        raise TypeError("func must be callable")


def main():
    """Main function of the program.
Tests 3 cases, returns results via ft_filter and filter
for comparison."""
    try:
        # Test cases
        nbrs = [1, 2, 3, 4, 5]
        words = ["apple", "banana", "kiwi", "orange"]
        people = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 17},
            {"name": "Charlie", "age": 30},
            {"name": "David", "age": 20}
        ]

        print("Test Case 1:")
        print("Using filter:", list(filter(lambda x: x % 2 == 0, nbrs)))
        print("Using ft_filter:", list(ft_filter(lambda x: x % 2 == 0, nbrs)))

        print("Test Case 2:")
        print("Using filter:", list(filter(lambda x: len(x) > 3, words)))
        print("Using ft_filter:", list(ft_filter(lambda x: len(x) > 3, words)))

        print("Test Case 3:")
        print("Using filter:",
              list(filter(lambda person: person['age'] > 18, people)))
        print("Using ft_filter:",
              list(ft_filter(lambda person: person['age'] > 18, people)))

    except TypeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
