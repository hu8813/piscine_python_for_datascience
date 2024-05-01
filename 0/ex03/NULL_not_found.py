def NULL_not_found(obj: any) -> int:
    try:
        if obj is None:
            print("Nothing:", obj, type(obj))
        elif isinstance(obj, float) and obj != obj:
            print("Cheese:", obj, type(obj))
        elif isinstance(obj, bool):
            print("Fake:", obj, type(obj))
        elif isinstance(obj, int):
            print("Zero:", obj, type(obj))
        elif obj == '':
            print("Empty:", type(obj))
        else:
            print("Type not Found")
            return 1
    except Exception as e:
        print("An error occurred:", str(e))
        return 1
    return 0
