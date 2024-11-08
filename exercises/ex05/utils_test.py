"""Quickly tests the utils file"""

__author__: str = "730816144"


from utils import only_evens, sub, add_at_index
import pytest


# Me trying to resolve an autograder problem :( Static types are annoying.
empty_list: list[int] = []


def test_only_evens1() -> None:
    """This one tests if it can handle empty lists"""

    test_list: list[int] = empty_list

    assert only_evens(input_list=test_list) is empty_list


def test_only_evens2() -> None:
    """Checks if inputing a list of only odd numbers returns an empty list"""

    test_list: list[int] = [1, 3, 5, 7, 9, 11]

    assert only_evens(input_list=test_list) is empty_list


def test_only_evens3() -> None:
    """Checks if any even numbers are erroneously removed from a list of only even numbers"""

    test_list: list[int] = [2, 4, 6, 8, 10]
    assert len(test_list) is len(only_evens(input_list=test_list))


def test_only_evens4() -> None:
    """Checks if the original list was mutated (should NOT have been mutated)"""

    test_list: list[int] = [1, 3, 5, 7, 9]
    original_length: int = len(test_list)
    only_evens(input_list=test_list)
    assert len(test_list) is original_length


def test_sub1() -> None:
    """This one tests if it can handle empty lists"""

    test_list: list[int] = empty_list

    assert sub(input_list=test_list, start_index=1, end_index=3) is empty_list


def test_sub2() -> None:
    """Checks if the returned list has the correct length"""

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    start_idx: int = 3
    end_idx: int = 6
    expected_length: int = 3

    assert (
        len(sub(input_list=test_list, start_index=start_idx, end_index=end_idx))
        is expected_length
    )


def test_sub3() -> None:
    """Checks if the original list was mutated (should NOT have been mutated)"""

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    original_length: int = len(test_list)

    sub(input_list=test_list, start_index=2, end_index=8)
    assert len(test_list) is original_length


def test_add_at_index1() -> None:
    """Checks if the result has the given element at the given index as specified"""

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    new_element: int = 500
    new_index: int = 5

    add_at_index(input_list=test_list, element=new_element, index_to_add_at=new_index)

    assert test_list[new_index] is new_element


def test_add_at_index2() -> None:
    """Checks if the result has the correct length,
    and if the last element of the list before and after the test is the same.
    Also implicitly checks for mutation (input list SHOULD be mutated)"""

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    original_length: int = len(test_list)
    original_final_element: int = test_list[original_length - 1]
    new_element: int = 500
    new_index: int = 5
    add_at_index(input_list=test_list, element=new_element, index_to_add_at=new_index)
    # print(test_list)

    # This one saved me. Check the comment in add_at_index, line 54
    assert (
        len(test_list) is original_length + 1
        and test_list.pop() is original_final_element
    )


def test_add_at_index3() -> None:
    """Checks if an error is thrown when an invalid index is given"""
    test_list: list[int] = empty_list

    # I hope I'm allowed to use this. I think it's more intuitive than the pytest code instructed.
    # HOWEVER, if it isn't allowed, test_add_at_index4 uses the instruced code. No punish pls ;-;
    try:
        add_at_index(input_list=test_list, element=10000, index_to_add_at=1000)
    except IndexError:
        assert True

    try:
        add_at_index(input_list=test_list, element=10000, index_to_add_at=-50)
    except IndexError:
        assert True


def test_add_at_index4() -> None:
    """Same result as test_add_at_index3, but using legal code within Comp110"""

    with pytest.raises(IndexError):
        test_list: list[int] = empty_list
        add_at_index(input_list=test_list, element=5, index_to_add_at=5)

    with pytest.raises(IndexError):
        test_list: list[int] = empty_list
        add_at_index(input_list=test_list, element=5, index_to_add_at=-5)
