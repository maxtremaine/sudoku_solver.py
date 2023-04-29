from typing import Tuple
from dataclass import dataclass

@dataclass(frozen=True)
class BlankCell:
    index: int
    possible_values: Tuple[int]