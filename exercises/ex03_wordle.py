"""Wordle but better ;)"""

__author__ = "730816144"


# Very similar to the previous excercise. I like the while loop improvement.
def input_guess(desired_length: int) -> str:
    """Continuously requests an input of the correct length until it is provided"""

    guess: str = input(f"Enter a {desired_length} character word: ")

    while len(guess) != desired_length:
        guess = input(f"That wasn't {desired_length} chars! Try again: ")

    return guess


# Simple enough. It just loops through.
def contains_char(word_to_search: str, char_to_find: str) -> bool:
    """Checks if the first string contains the second character"""
    assert len(char_to_find) == 1

    index_at: int = 0

    # I like making my loop variables readable. I know it's slightly inefficient but readability matters.
    while index_at < len(word_to_search):
        if word_to_search[index_at] == char_to_find:
            return True
        index_at += 1

    return False


# I don't know why changing it the ways I did made it work anymore, the moment of inspiration passed.
# But it does now :)
# In all seriousness, I had initially made the mistake of checking the words backwards, as in,
# checking if "input_word" contained "secret_word."
# Which predictably led to some complications.
def emojified(input_word: str, secret_word: str) -> str:
    """Creates a list of colored boxes describing the similarities between two words:
    A white box means there is no similarity.
    A yellow box means the character matches but is misplaced.
    A green box means the character matches both in value and position."""

    assert len(input_word) == len(secret_word)
    return_str: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index_at: int = 0

    while index_at < len(secret_word):
        if contains_char(word_to_search=secret_word, char_to_find=input_word[index_at]):
            if input_word[index_at] == secret_word[index_at]:
                return_str += GREEN_BOX
            else:
                return_str += YELLOW_BOX
        else:
            return_str += WHITE_BOX

        index_at += 1

    return return_str


# I like the idea of housing the game locally in a function.
# The alternative is using global variables and having the main function interact with
# them. It would make it easier to expand the game because you could import these
# variables from other modules, but that isn't a concern, so this is much tidier.
def main(secret_word: str) -> None:
    """The entrypoint of the program"""
    tries: int = 1
    unknown_word: str = secret_word

    while tries < 7:
        print(f"=== Turn {tries}/6 ===")

        new_guess: str = input_guess(len(unknown_word))

        print(emojified(new_guess, unknown_word))

        if new_guess == unknown_word:
            print(f"You won in {tries}/6 turns!")
            return

        tries += 1

    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main("explosive")
