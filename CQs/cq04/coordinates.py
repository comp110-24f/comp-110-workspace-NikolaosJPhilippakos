"""Has a function to print coordinates"""

__author__ = "730816144"


def get_coords(xs: str, ys: str) -> None:
    """Prints every combination of the x array and y array"""
    max_x: int = len(xs)
    max_y: int = len(ys)

    index_x: int = 0
    index_y: int = 0

    # I forgot to update the index_y variable after each iteration.
    # This mistake took a while to find.
    while index_x < max_x:
        while index_y < max_y:
            print("(" + xs[index_x] + "," + ys[index_y] + ")")
            index_y += 1
        index_y = 0
        index_x += 1


if __name__ == "__main__":
    get_coords("1234", "random_text")
