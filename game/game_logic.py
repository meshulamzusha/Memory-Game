import os
import time
from game import io


def is_matching(table: list[list], position_1: tuple[int, int], position_2: tuple[int, int]) -> bool:
    """Return True if the value in the positions in the table are the same, else False"""
    i1 = position_1[0]
    j1 = position_1[1]
    
    i2 = position_2[0]
    j2 = position_2[1]

    return table[i1][j1] == table[i2][j2]


def is_flipped(table: list[list], position_1: tuple[int, int], position_2: tuple[int, int]) -> bool:
    """Return True if the 2 cards are already matched"""
    i1 = position_1[0]
    j1 = position_1[1]

    i2 = position_2[0]
    j2 = position_2[1]

    return table[i1][j1] != '*' and table[i2][j2] != '*'


def update_player_table(game_table: list[list], display_table: list[list], position_1: tuple[int, int], position_2: tuple[int, int]) -> None:
    """Update the table thet will be displayed for player"""
    i1 = position_1[0]
    j1 = position_1[1]

    i2 = position_2[0]
    j2 = position_2[1]

    display_table[i1][j1] = game_table[i1][j1]
    display_table[i2][j2] = game_table[i2][j2]


def unupdat_player_table(display_table: list[list], position_1: tuple[int, int], position_2: tuple[int, int]) -> None:
    i1 = position_1[0]
    j1 = position_1[1]

    i2 = position_2[0]
    j2 = position_2[1]

    display_table[i1][j1] = '*'
    display_table[i2][j2] = '*'


def process_mathc(game_table: list[list], display_table: list[list], positions: tuple[tuple[int, int], tuple[int, int]]) -> None:
    print('Correct match the table has been updated.')
    update_player_table(game_table, display_table, positions[0], positions[1])
    io.display_table(display_table)
    clear_screen()


def process_mismathc(game_table: list[list], display_table: list[list], positions: tuple[tuple[int, int], tuple[int, int]]) -> None:
    print('No match. You have five seconds to remember the cards you turned over.')
    update_player_table(game_table, display_table, positions[0], positions[1])
    io.display_table(display_table)
    unupdat_player_table(display_table, positions[0], positions[1])
    clear_screen()


def clear_screen() -> None:
    clear = lambda: os.system('clear')
    time.sleep(5)
    clear()


def glay_round(game_table: list[list], display_table: list[list]) -> None:
    io.display_table(display_table)
    positions = io.get_cards_index()
    is_cards_match = is_matching(game_table, positions[0], positions[1])
    cards_are_flip = is_flipped(display_table, positions[0], positions[1])

    if is_cards_match and not cards_are_flip:
        process_mathc(game_table, display_table, positions)
    else:
        process_mismathc(game_table, display_table, positions)