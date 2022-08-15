from typing import Tuple

@dataclass(frozen=True)
class BlankCell:
    index: int
    possible_values: Tuple[int]