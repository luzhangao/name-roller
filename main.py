import os
import random

import arrow
from dotenv import load_dotenv


load_dotenv()


def name_picker(datetime_str):
    """
    select a name from a list randomly
    Args:
        datetime_str:

    Returns:

    """
    names = os.getenv("NAMES")
    if names:
        names = names.split(',')
    else:
        raise ValueError(f"{names} is not a list!")
    print(f"{names=}")

    std_time = arrow.get(datetime_str, 'YYYY-MM-DD HH:mm:ss')
    print(f"time input: {std_time}")
    random.seed(int(std_time.timestamp()))

    chosen_name = names[random.randint(0, len(names))]
    print(f"The name chosen is {chosen_name}!")


if __name__ == '__main__':
    name_picker("2025-01-01 22:03:00")
