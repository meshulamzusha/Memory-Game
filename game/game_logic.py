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