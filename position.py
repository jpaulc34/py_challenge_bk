from dataclasses import dataclass, field


@dataclass
class Pos:
    y: int
    x: int
    knight: dict = None
    state: dict = None
    items: list = field(default_factory=list)

    def __repr__(self):
        return '[{}, {}]'.format(self.y, self.x)

    def to_json(self):
        return [self.y, self.x]
