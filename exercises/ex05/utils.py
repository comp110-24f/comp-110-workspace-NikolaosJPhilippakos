"""Holds a few list utility functions."""

__author__: str = "730816144"


def only_evens(input_list: list[int]) -> list[int]:
    """Takes a list of integers as input, and constructs and returns a new list
    of all the even elements of the input list."""

    return_list: list[int] = []

    # No comment, nothing interesting here.
    for temp_int in input_list:
        if temp_int % 2 == 0:
            return_list.append(temp_int)

    return return_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Cuts out a part of the input list, and returns it. The beggining and end of that
    part are given by the start_index (inclusive) and end_index (exclusive) parameters. \n \n
    If the list is shorter than the indexes provided, only the overlap between the input list and indexes will be returned.
    """

    return_list: list[int] = []

    index: int = start_index

    if index < 0:
        index = 0

    # Very straightfoward, I'm happy about this one.

    while index < len(input_list) and index < end_index:
        return_list.append(input_list[index])
        index += 1

    return return_list


def add_at_index(input_list: list[int], element: int, index_to_add_at: int) -> None:
    """Adds the element to the provided list by mutating it in at that index."""

    if index_to_add_at > len(input_list) or index_to_add_at < 0:
        raise IndexError("Index is out of bounds for the input list")

    # As stated in the assignment, make space, then shift over using the [] operators,
    # then finally add the new int at the index.
    input_list.append(0)

    index: int = len(input_list) - 1

    # It took me a while to realize what the problem was here.
    # You can't really "push" the elements over from behind because the next one in the list gets lost.
    # So you get a bunch of duplicates.
    # Pulling them one by one from the right resolves that problem.
    while index > index_to_add_at:
        input_list[index] = input_list[index - 1]
        index -= 1

    input_list[index_to_add_at] = element
