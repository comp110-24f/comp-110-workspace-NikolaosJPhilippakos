"""Summing the elements of a list using different loops"""

__author__ = "730816144"


# None of these took more than two minutes to plan or write.
def w_sum(input_list: list[float]) -> float:
    """Uses a while loop to add every value in a list of floats, and returns the result.
    I.E., a finite series"""
    return_value: float = 0.0
    index: int = 0

    while index < len(input_list):
        return_value += input_list[index]
        index += 1

    return return_value


def f_sum(input_list: list[float]) -> float:
    """Uses a for loop to add every value in a list of floats and returns the result.
    I.E., a finite series"""
    return_value: float = 0.0

    for temp_float in input_list:
        return_value += temp_float

    return return_value


def f_range_sum(input_list: list[float]) -> float:
    """Uses a for loop iterating over a range to add every value in a list of floats,
    and returns the result. I.E., a finite series"""
    return_value: float = 0.0

    for index in range(0, len(input_list), 1):
        return_value += input_list[index]

    return return_value


if __name__ == "__main__":
    float_list: list[float] = [0.1, 0.8, 10.1]
    float_list_2: list[float] = []

    print(w_sum(float_list))
    print(w_sum(float_list_2))
    print(f_sum(float_list))
    print(f_sum(float_list_2))
    print(f_range_sum(float_list))
    print(f_range_sum(float_list_2))
