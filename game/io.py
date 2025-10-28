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


def get_cards_index() -> tuple[tuple[int, int], tuple[int, int]]:
    """Returns a tuple of tow tuples for users card flipping"""
    position_1 = input(f'Enter the first card position that you want to flip in the following format i comma j: ')
    position_2 = input(f'Enter the other card position that you want to flip in the following format i comma j: ')

    return utils.convert_input_type(position_1), utils.convert_input_type(position_2)