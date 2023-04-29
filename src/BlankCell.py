from typing import Tuple
from dataclasses import dataclass

@dataclass(frozen=True)
class BlankCell:
    index: int
    possible_values: Tuple[int]