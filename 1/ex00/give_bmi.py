def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Calculate the BMI (body mass index) of a list of people.

    Args:
        height (list[int | float]): Height of the people.
        weight (list[int | float]): Weight of the people.

    Returns:
        list[int | float]: List of BMI values.
    """
    try:
        assert len(height) == len(weight), (
            "The number of heights and weights must be the same"
        )
        assert all(
            isinstance(i, (int, float)) and i > 0 for i in height
        ), "All heights must be positive integers or floats"
        assert all(
            isinstance(i, (int, float)) and i > 0 for i in weight
        ), "All weights must be positive integers or floats"
    except Exception as e:
        print(e)
        return []
    return [weight[i] / height[i] ** 2 for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI of a list of people.

    Args:
        bmi (list[int | float]): BMI of the people.
        limit (int): Limit to apply.

    Returns:
        list[bool]: Return True if the BMI is greater than the limit,
                    False otherwise.
    """
    try:
        assert all(
            isinstance(i, (int, float)) and i > 0 for i in bmi
        ), "All BMI values must be positive integers or floats"
        assert isinstance(limit, int) and limit > 0, (
            "The limit must be a positive integer"
        )
    except Exception as e:
        print(e)
        return []
    return [True if i > limit else False for i in bmi]


def main():
    pass


if __name__ == "__main__":
    main()
