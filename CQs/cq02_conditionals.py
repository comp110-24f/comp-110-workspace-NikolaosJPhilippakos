"""Guess the number to win!"""

__author__: str = "730816144"


def guess_a_number() -> None:
    secret: int = 7
    guess: str = input("Guess a number:")
    print("Your guess was " + str(guess))

    int_guess = int(guess)

    if int_guess == secret:
        print("You got it!")
    elif int_guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif int_guess > secret:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
