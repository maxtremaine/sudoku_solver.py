from dataclasses import dataclass

@dataclass(frozen=True)
class BlankCell:
    index: int
    possible_values: tuple[int]