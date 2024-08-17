"""While loop practice for Comp110"""

__author__: str = "730816144"


def num_instances(phrase: str, search_char: str) -> int:

    phrase_length: int = len(phrase)
    step_at: int = 0
    found_chars: int = 0

    while step_at < phrase_length:
        if phrase[step_at] == search_char:
            found_chars += 1

        step_at += 1

    return found_chars


if __name__ == "__main__":
    print(num_instances(phrase="Happy Tuesday!", search_char="z"))
