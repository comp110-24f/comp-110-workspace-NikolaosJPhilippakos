"""Tests the find_max file."""

__author__: str = "730816144"

from find_max import find_and_remove_max

test_list: list[int] = [1, 5, 9, 4, 5, 6, 7, 8, 1, 9, 9, 9, 1, 2, 3]


def test_find_and_remove_max1() -> None:
    """Checks if the functon finds the correct value"""
    assert find_and_remove_max(test_list) == 9


def test_find_and_remove_max2() -> None:
    """Chekcs if the function removes the max values"""
    max_value = find_and_remove_max(test_list)

    flag: bool = False

    for temp_val in test_list:
        if temp_val == max_value:
            flag = True

    assert flag is False


def test_find_and_remove_max3() -> None:
    """Checks if an empty list returns -1"""
    assert find_and_remove_max([]) == -1
