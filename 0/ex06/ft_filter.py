def ft_filter(func, items=None):
    """
    Returns an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
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
    try:
        # Test cases
        numbers = [1, 2, 3, 4, 5]
        words = ["apple", "banana", "kiwi", "orange"]
        people = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 17},
            {"name": "Charlie", "age": 30},
            {"name": "David", "age": 20}
        ]
        
        # Test case 1: Filter even numbers
        print("Test Case 1:")
        print("Using filter:", list(filter(lambda x: x % 2 == 0, numbers)))
        print("Using ft_filter:", list(ft_filter(lambda x: x % 2 == 0, numbers)))
        
        # Test case 2: Filter strings longer than 3 characters
        print("Test Case 2:")
        print("Using filter:", list(filter(lambda x: len(x) > 3, words)))
        print("Using ft_filter:", list(ft_filter(lambda x: len(x) > 3, words)))
        
        # Test case 3: Filter people over 18
        print("Test Case 3:")
        print("Using filter:", list(filter(lambda person: person['age'] > 18, people)))
        print("Using ft_filter:", list(ft_filter(lambda person: person['age'] > 18, people)))
    
    except TypeError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

