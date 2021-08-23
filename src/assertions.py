import re

def is_character(string: str) -> bool:
    return len(string) == 1

def is_sudoku_file(sudoku_file: str) -> bool:
    pattern = re.compile('^(\s|\n|\||_|-|[1-9]|[a-i]){167}$')
    if pattern.match(sudoku_file) == None:
        return False
    return True

def is_sudoku_string(sudoku_string: str) -> bool:
    """If a string is 81 digits or underscores, return True."""
    pattern = re.compile('^(_|[1-9]){81}$')
    if pattern.match(sudoku_string) == None:
        return False
    return True

