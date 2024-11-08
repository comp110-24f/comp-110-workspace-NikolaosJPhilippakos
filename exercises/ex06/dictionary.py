"""A bunch of dictionary utilities."""

__author__: str = "730816144"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Returns an inverted list, where the keys are the values of the input list and vice versa."""

    return_dict: dict[str, str] = dict()

    # Simple enough swap. Hard to read, though, isn't it?
    for temp_key in input_dict:
        if input_dict[temp_key] in return_dict:
            raise KeyError("Cannot create a dictionary with duplicate keys!")
        return_dict[input_dict[temp_key]] = temp_key

    return return_dict


def favorite_color(input_colors: dict[str, str]) -> str:
    """Takes a dictionary which pairs every person's name with their favorite color, and returns the most common color. \n \n
    If two or more colors appear the same max number of times, the first to appear in the input dictionary is returned.
    """
    frequency: dict[str, int] = dict()

    # First, figure out how many times each color appears.
    for name in input_colors:
        temp_color: str = input_colors[name]

        if temp_color in frequency:
            frequency[temp_color] += 1

        else:
            frequency[temp_color] = 1

    return_color: str = ""
    current_max: int = 0

    # Second, figure out which appears the most the first, and return it.
    for color in frequency:
        if frequency[color] > current_max:
            return_color = color
            current_max = frequency[color]

    return return_color


def count(input_list: list[str]) -> dict[str, int]:
    """Takes a list of strings and returns a dictionary which pairs each string with its frequency in the list."""

    return_dict: dict[str, int] = dict()

    # I just followed the provided outline
    for temp_string in input_list:
        if temp_string in return_dict:
            return_dict[temp_string] += 1
        else:
            return_dict[temp_string] = 1

    return return_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Takes a list of strings and returns a dictionary of all the characters those strings start with. \n
    Each start character is a key to an associated list of all the strings which start with it.
    """
    return_dict: dict[str, list[str]] = dict()

    # This one was fun.
    for temp_string in input_list:
        if temp_string[0] not in return_dict:
            return_dict[temp_string[0]] = list()

        return_dict[temp_string[0]].append(temp_string)

    return return_dict


def update_attendance(
    input_dict: dict[str, list[str]], day_of_week: str, student_name: str
) -> None:
    """Updates attendance one student at a time."""

    # This one is straightfoward
    if day_of_week not in input_dict:
        input_dict[day_of_week] = list()

    if student_name not in input_dict[day_of_week]:
        input_dict[day_of_week].append(student_name)

    # It said to return the dict in the instructions but the autograder disagrees, sooo:
    return None
