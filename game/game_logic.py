def is_matching(table: list[list], position_1: tuple[int, int], position_2: tuple[int, int]) -> bool:
    """Return True if the value in the positions in the table are the same, else False"""
    i1 = position_1[0]
    j1 = position_1[1]
    
    i2 = position_2[0]
    j2 = position_2[1]

    return table[i1][j1] == table[i2][j2]