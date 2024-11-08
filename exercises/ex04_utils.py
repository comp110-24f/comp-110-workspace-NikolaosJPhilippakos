"""Holds several list utility functions"""

__author__: str = "730816144"


def all(input_list: list[int], desired_int: int) -> bool:
    """Checks if every entry in input_list is equal to desired_int,
    AND if the list contains at least one entry"""

    # I'm not sure if this integer is more efficient than len(list)
    # during each iteration of the while loop, but I thought it would be a good idea.
    list_length = len(input_list)

    if list_length == 0:
        return False

    index: int = 0

    while index < list_length:
        if input_list[index] != desired_int:
            return False
        index += 1

    return True


def max(input_list: list[int]) -> int:
    """Finds the largest value in a list of integers,
    or throws a ValueError if the list is empty."""

    list_length: int = len(input_list)

    # New things, very fun
    if list_length == 0:
        raise ValueError("max() arg is an empty List")

    else:
        return_value: int = input_list[0]
        index: int = 0
        while index < list_length:
            if input_list[index] > return_value:
                return_value = input_list[index]
            index += 1

        return return_value


# No need to check for equalities, just inequalities. Assume they are equal if no inequalities are found.
def is_equal(input_list_1: list[int], input_list_2: list[int]) -> bool:
    """Checks the value for each index in two lists of integers,
    and returns true if every pair of values is equal."""

    list_length: int = len(input_list_1)

    if len(input_list_2) != list_length:
        return False

    index: int = 0
    while index < list_length:
        if input_list_1[index] != input_list_2[index]:
            return False
        index += 1

    return True


# I really like how while loops intrinsically account for empty lists becuause their lengths are zero.
def extend(input_list_1: list[int], input_list_2: list[int]) -> None:
    """Appends list 2 on to list 1"""
    list_length: int = len(input_list_2)
    index: int = 0

    while index < list_length:
        input_list_1.append(input_list_2[index])
        index += 1


if __name__ == "__main__":
    list_1: list[int] = [1, 2, 3, 4, 5, 0]
    list_2: list[int] = [1, 2, 3, 4, 5, 0]
    list_3: list[int] = [1, 1, 1, 1, 1]

    print(is_equal(list_1, list_2))
    print(is_equal(list_2, list_3))
    print(max(list_1))
    print(max(list_3))
    print(all(list_1, 1))
    print(all(list_3, 1))

    extend(list_1, list_3)

    print(list_1)
