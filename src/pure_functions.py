from typing import List

def get_missing_digits(digits: List[str]) -> List[str]:
    return [
        str(digit) for digit in range(1, 10)
        if str(digit) not in digits
    ]

def replace_character(string: str, index: int, new_character: str):
    string_list = list(string)
    string_list[index] = new_character
    return ''.join(string_list)