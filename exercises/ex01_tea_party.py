"""A fun calculator for your brewing adventures"""

__author__: str = "730816144"

# I decided to put these numbers up here.
# I hope it doesn't mess up the autograder
# I just couldn't bring myself to scatter the actual important inputs all over
# I probably overthought this though
teabags_per_guest: int = 2
treats_per_cuppa_tea: float = 1.5
price_of_tea_bag: float = 0.5
price_of_treat: float = 0.75


# These two are fairly self-explanatory. They just multiply two numbers together.
def tea_bags(people: int) -> int:
    """Gets the number of tea bags needed for a number of people"""
    return people * teabags_per_guest


# It casts to an int because you can't exactly buy fractional treats
# Which will be relevant below
def treats(people: int) -> int:
    """Gets the number of treats needed for a number of people drinking tea"""
    return int(tea_bags(people=people) * treats_per_cuppa_tea)


# No parenthesis is best parethesis.
def cost(tea_count: int, treat_count: int) -> float:
    """Gets the prices for the number of teas and treats, and adds them together"""
    return tea_count * price_of_tea_bag + treat_count * price_of_treat


# It does negative guests, too. Not sure if that's a problem.
# I don't think I'm allowed to use if/else checks yet though. So it is what it is.
def main_planner(guests: int) -> None:
    """This program starts here."""
    tea_bag_count: int = tea_bags(people=guests)
    treat_count: int = treats(people=guests)
    total_cost: float = cost(tea_count=tea_bag_count, treat_count=treat_count)
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bag_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + str(total_cost))


# Magic
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
