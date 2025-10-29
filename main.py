from game import game_logic, io
from utils import utils


def main():
    io.start_game_message()

    table_size = io.get_table_size()
    cards_table = utils.create_cards_table(table_size)
    display_table = utils.create_player_table(table_size)
    steps = 0
    matched_pairs = 0

    while matched_pairs < (table_size ** 2) // 2:
        game_logic.glay_round(cards_table, display_table)
        steps += 1

if __name__ == '__main__':
    main()