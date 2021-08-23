from typing import List

def get_missing_digits(digits: List[str]) -> List[str]:
    return [
        str(digit) for digit in range(1, 10)
        if str(digit) not in digits
    ]