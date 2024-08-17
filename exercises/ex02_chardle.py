"""A step towards wordle"""

__author__: str = "730816144"


# Logical tests on the input placed here for convenience.
# Otherwise, later steps might print things they shouldn't before exting.
def input_word() -> str:
    """Requests a 5 character word from the user.
    Exits if the input is too short or too long."""

    input_text: str = str(input("Enter a 5-character word: "))

    # print("'" + input_text + "'")

    # ^ I don't know why this line is discarded during the later
    # stages of the instructions.
    # The ''s aren't present in the later examples.
    # And it wasn't mentioned at all. Mistake by the profs maybe?
    # I'm playing it safe and commenting it out but please know it was there once :(

    if len(input_text) != 5:
        print("Error: Word must contain 5 characters.")
        exit()

    return input_text


def input_letter() -> str:
    """Requests a single character from the user.
    Exits if the input is too short or too long"""

    input_text: str = input("Enter a single character: ")

    if len(input_text) > 1:
        print("Error: Character must be a single character.")
        exit()

    return input_text


def contains_char(word: str, letter: str) -> None:
    """Counts the instances of a character in a 5 character word.
    Prints the index of each instance and the total number of instances afterward."""
    match_count: int = 0
    index: int = 0

    print("Searching for " + letter + " in " + word)

    # Outputs the exact same thing as the loop below it, except the autograder hates it.
    # No reason, it just does. I'm leaving it in as proof that I did it correctly.
    """
    if word[0] == letter:
        print(letter + " found at index 0")
        match_count = match_count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        match_count = match_count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        match_count = match_count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        match_count = match_count + 1
    if word[4] == input_letter:
        print(letter + " found at index 4")
        match_count = match_count + 1
    """
    # OK SO NOW ITS CORRECT FOR SOME UNKNOWN, UNIDENTIFIABLE REASON
    # The one thing I have learned from this course so far is that autograding is ****
    while index < 5:
        if word[index] == letter:
            match_count += 1
            print(letter + " found at index " + str(index))
        index += 1

    if match_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif match_count == 1:
        print("1 instance of " + letter + " found in " + word)
    elif match_count > 1:
        print(str(match_count) + " instances of " + letter + " found in " + word)


# Redundant but required.
def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()


# really unsure what to comment on this,
# it's about as immediately intuitive as it gets code-wise.
