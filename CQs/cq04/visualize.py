"""Visualizes function imports--the starting point of the program"""

from concatenation import concat
from coordinates import get_coords

__author__ = "730816144"

x: str = "123"
y: str = "abc"

# The starting point of the program
if __name__ == "__main__":
    print(concat(parameter1=x, parameter2=y))
    get_coords(xs=x, ys=y)
