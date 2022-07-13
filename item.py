from dataclasses import dataclass
from position import Pos


@dataclass
class Item:
    name: str
    power: int
    pos: Pos
    attack: int
    defence: int
