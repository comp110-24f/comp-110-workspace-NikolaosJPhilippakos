"""Mutating functions."""

__author__: str = "730816144"


# Completely redundant, I have no idea why you would ever make this function.
def manual_append(input_list: list[int], integer: int) -> None:
    """Adds the integer to the list!"""
    input_list.append(integer)


# Very straightforward. It gets the value at each index and sets the value at that
# index to double the original value.
def double(input_list: list[int]) -> None:
    """Doubles every value in a list."""
    index: int = 0

    while index < len(input_list):
        input_list[index] = input_list[index] * 2
        index += 1


# I'm not sure if I'm supposed to submit this but here goes
if __name__ == "__main__":
    list1: list[int] = [1, 2, 3]
    list2: list[int] = list1

    double(list1)
    print(list1)
    print(list2)
