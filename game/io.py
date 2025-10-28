from utils import utils

def start_game_message() -> None:
    """prints a message for game starting"""
    print("Welcome to the memory game.\n"
          "Please select the board size.(type a number and press Enter)\n"
          "The game board will be size x size.")


def get_table_size() -> int:
    """gets the size of game table size"""
    size = int(input())
    return size


def display_table(table: list[list]) -> None:
    """prints a table in a user-friendly way"""
    for row in table:
        print(' '.join(map(str,row)))