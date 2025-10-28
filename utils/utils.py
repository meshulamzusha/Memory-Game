def convert_input_type(user_input: str) -> tuple[int, int]:
    """Returns a tuple of coordinates converted from string to int"""
    coordinates = user_input.split(',')
    return int(coordinates[1]), int(coordinates[2])