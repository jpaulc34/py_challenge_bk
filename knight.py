from dataclasses import dataclass, field
from item import Item
from position import Pos
STATUS_OPTS = ('LIVE', 'DEAD', 'DROWNED')


@dataclass
class Knight:
    clr: str
    name: str
    pos: Pos
    status: str = STATUS_OPTS[0]
    item: Item = None
    base_attack: int = 1
    base_defence: int = 1

    def getAttackScore(self):
        if self.item:
            return self.base_attack + self.item.attack
        else:
            return self.base_attack

    def getDefenceScore(self):
        if self.item:
            return self.base_defence + self.item.defence
        else:
            return self.base_defence

    def update_status(self, idx):
        self.status = STATUS_OPTS[idx]
