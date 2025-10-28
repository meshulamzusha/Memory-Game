import random

def convert_input_type(user_input: str) -> tuple[int, int]:
    """Returns a tuple of coordinates converted from string to int"""
    coordinates = user_input.split(',')
    return int(coordinates[1]), int(coordinates[2])


def create_cards_table(size: int) -> list[list]:
    """create a list of lists with elements for game cards represents the game table"""
    table = []

    for i in range(size):
        row = list(range((i * size) + 1, (i + 1) * size))
        table.append(row)

    return table


def shuffle_table(table: list[list]) -> list[list]:
    """Shuffle the game table and return it"""
    random.shuffle(table)
    for row in table:
        random.shuffle(row)

    return table


def create_player_table(size: int) -> list[list]:
    """creates and returns a table thet will be update every turn and displayed for user"""
    user_table = []
    for i in range(size):
        row = ['*'] * size
        user_table.append(row)

    return user_table