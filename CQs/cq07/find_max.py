"""Holds the find_and_remove_max function."""

__author__: str = "730816144"


def find_and_remove_max(input_list: list[int]) -> int:
    """Finds the largest integer in a list of integers.
    Returns it after removing every instance of it from the list."""

    return_val: int = -1

    for temp_int in input_list:
        if temp_int > return_val:
            return_val = temp_int

    index: int = 0

    # I like how you can just skip the index increment to get to the next item when you pop the index.
    while index < len(input_list):
        if input_list[index] == return_val:
            input_list.pop(index)
        else:
            index += 1

    return return_val
