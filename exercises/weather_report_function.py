"""Asks for the weather, and tells you what to do!"""


def get_weather_report() -> str:
    """Prompts you for the weather, and returns it.
    Also prints helpful tips if it recognizes the input."""

    weather: str = input("What's the weather today? \n")

    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize that weather. Good luck!")
    return weather


get_weather_report()
