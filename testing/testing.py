numbers: list[float] = []

numbers.append(1.5)
numbers.pop()
numbers.append(0.1)
numbers.append(0.1)
numbers.insert(1, 0.5)
numbers[0] = numbers[-1]

# print(len(numbers))
# print(numbers)

nulls: list[None] = [None, None, None, None]
nulls.pop()

# print(nulls)

pets: list[str] = ["Louie", "Bo", "Bear"]

for temp_str in pets:
    # print("Good boy, " + temp_str + "!")
    break

# print(type(range(1, 500, 99)))

ages: dict[str, int] = {"Niko": 19, "Daphne": 13, "Ari": 17}
# print(ages["Mom"])
# print(type(ages))


class Line:
    start_point: int
    end_point: int

    def __init__(self, start_point: int, end_point: int):
        self.start_point = start_point
        self.end_point = end_point
