def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is a letter.
    Then, checks if the first letter of word equals letter"""

    if len(letter) != 1:
        return "Your letter is not a letter!"

    if len(word) > 0:
        if word[0] == letter:
            return "match!"
        else:
            return "no match!"
    else:
        return "Your word is too short!"


print(check_first_letter("Hello", "e"))
