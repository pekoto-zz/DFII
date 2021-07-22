import random
from typing import List, Any


def shuffle(items: List[Any]) -> None:
    for i in range(1, len(items)):
        # randint is inclusive
        rand_index = random.randint(0, i)
        items[i], items[rand_index] = items[rand_index], items[i]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    shuffle(numbers)
    print(numbers)
