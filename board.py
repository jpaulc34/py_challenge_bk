from operator import attrgetter
from pprint import pprint
from position import Pos
from item import Item
from knight import Knight
from appExceptions import Drowned


class ArenaBoard:
    arenaBoard = []
    R: Knight
    G: Knight
    B: Knight
    Y: Knight
    _axe: Item  # +2 Attack
    _dagger: Item  # +1 Attack
    _helmet: Item  # +1 Defence
    _magicStaff: Item  # +1 Attack, +1 Defence

    def __init__(self) -> None:
        self.createArenaBoardLayout()

    def createArenaBoardLayout(self):
        for y in range(0, 8):
            row = [Pos(y, x) for x in range(0, 8)]
            self.arenaBoard.append(row)

    def getArenaBoard(self):
        self.placeKnights()
        self.placeItems()
        pprint(self.arenaBoard)

    def placeKnights(self):
        self.R = Knight('Red', 'R', self.arenaBoard[0][0])
        self.G = Knight('Green', 'G', self.arenaBoard[7][7])
        self.B = Knight('Blue', 'B', self.arenaBoard[7][0])
        self.Y = Knight('Yellow', 'Y', self.arenaBoard[0][7])
        self.arenaBoard[0][0].knight = self.R
        self.arenaBoard[7][7].knight = self.G
        self.arenaBoard[7][0].knight = self.B
        self.arenaBoard[0][7].knight = self.Y

    def placeItems(self):
        self._axe = Item('Axe', 4, self.arenaBoard[2][2], 2, 0)
        self._magicStaff = Item('Magic', 3, self.arenaBoard[5][2], 1, 1)
        self._dagger = Item('Dagger', 2, self.arenaBoard[2][5], 1, 0)
        self._helmet = Item('Helmet', 1, self.arenaBoard[5][5], 0, 1)

        self.arenaBoard[2][2].items.append(self._axe)
        self.arenaBoard[2][5].items.append(self._dagger)
        self.arenaBoard[5][5].items.append(self._helmet)
        self.arenaBoard[5][2].items.append(self._magicStaff)

    def renderArenaBoard(self):
        print('')
        print('=====  BOARD  =====')
        print('')
        for row in self.arenaBoard:
            for pos in row:
                if pos.knight:
                    print(f'%{pos.knight.name}%', end='')
                elif len(pos.items):
                    print(pos.items[0].name[0] if pos.items[0] else '', end='')
                else:
                    print('  ', end='')
            print('')
        print('')

    def Attacking(self, attacker: Knight, defendant: Knight, addSurprise: bool):
        attack_score = (attacker.getAttackScore() +
                        0.5) if addSurprise else attacker.getAttackScore()
        defend_score = defendant.getDefenceScore()
        if attack_score > defend_score:
            return (attacker, defendant)
        else:
            return (defendant, attacker)

    @staticmethod
    def killTheKnight(_kn: Knight, livingStatus=1):
        knightLoot = _kn.item
        knightLastPos = _kn.pos
        _kn.update_status(livingStatus)
        _kn.pos = _kn.pos if livingStatus == 1 else None
        _kn.item = None
        _kn.base_attack = 0
        _kn.base_defence = 0
        return (knightLoot, knightLastPos)

    def moveKnightInArenaBoard(self, knight: Knight, move: str):
        tempKnight = getattr(self, knight)
        if tempKnight.status == 'DROWNED':
            print("DROWNED")
        else:
            tempKnight.pos.knight = None
            try:
                tempPos = self.makeAMove(move, tempKnight.pos)
            except Drowned:
                loot, last_pos = self.killTheKnight(tempKnight, 2)

                if self.dropWeaponsLoot(loot, last_pos):
                    print('The Loot dropped: ', loot)

            else:
                if tempPos.knight is not None:
                    attacker = tempKnight
                    defender = tempPos.knight
                    haveKnight = True if defender != None else False
                    winner, loser = self.Attacking(
                        attacker, defender, haveKnight)
                    self.movingThePosition(winner, tempPos)
                    loot, last_pos = self.killTheKnight(loser)

                    print('BATTLING')
                    print("\n")
                    print('Winner Knight => ', winner)
                    print('Lost Knight =>', loser)
                    if self.dropWeaponsLoot(loot, last_pos):
                        print('The Loot dropped: ', loot)
                    return winner

                if len(tempPos.items) == 0 and not tempPos.knight:
                    self.movingThePosition(tempKnight, tempPos)
                    print('Knight Move In Empty Position', tempKnight)
                elif len(tempPos.items) > 0:
                    self.movingThePosition(tempKnight, tempPos)
                    tempPos.items.sort(key=attrgetter('power'))
                    if not tempKnight.item:
                        popedItem = tempPos.items.pop()
                        if popedItem.name == 'Magic' and (tempKnight.name == 'R' or tempKnight.name == 'B'):
                            print(f'{tempKnight.clr} PICK the Magic')
                            tempKnight.item = popedItem
                        elif popedItem.name == 'Magic' and (tempKnight.name == 'G' or tempKnight.name == 'Y'):
                            print(f'Else IF=> {tempKnight.clr}')
                            tempPos.items.append(popedItem)
                            tempKnight.item = None
                        else:
                            tempKnight.item = popedItem


                        print(' knight equipment Acquired ', tempKnight.item)

                return tempKnight

    def dropWeaponsLoot(self, item: Item, pos: Pos):
        if item:
            item.pos = pos
            pos.items.append(item)
            pos.items.sort(key=attrgetter('power'))
            return True

    def movingThePosition(self, _kn: Knight, pos: Pos):
        pos.knight = _kn
        _kn.pos = pos
        if _kn.item:
            _kn.item.pos = pos

    def makeAMove(self, move: str, movingKnight: Pos):
        knightOldPos = movingKnight
        makeCoordinates = {
            'N': (knightOldPos.y-1, knightOldPos.x),
            'E': (knightOldPos.y, knightOldPos.x+1),
            'S': (knightOldPos.y+1, knightOldPos.x),
            'W': (knightOldPos.y, knightOldPos.x-1),
        }
        try:
            if makeCoordinates[move][0] < 0 or makeCoordinates[move][0] > 7 or makeCoordinates[move][1] < 0 or makeCoordinates[move][1] > 7:
                raise Drowned
            else:
                return self.arenaBoard[makeCoordinates[move][0]][makeCoordinates[move][1]]
        except KeyError:
            return self.arenaBoard[knightOldPos.y][knightOldPos.x]

    def getFinalResult(self):
        return self.arenaBoard
