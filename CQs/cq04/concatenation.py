"""Has a function to add two strings!"""

__author__ = "730816144"


def concat(parameter1: str, parameter2: str) -> str:
    """Adds two strings together"""
    return parameter1 + parameter2


word1: str = "happy"

word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(parameter1=word1, parameter2=word2))
