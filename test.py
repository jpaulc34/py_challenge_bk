import unittest

from board import ArenaBoard


class TestCase(unittest.TestCase):
    _arena = ArenaBoard()

    def setUp(self):
        self._arena.getArenaBoard()
        self._arena.renderArenaBoard()

    def testMovements(self):
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')

        self.assertEqual(self._arena.R.pos.to_json()[0], 2)
        self.assertEqual(self._arena.R.pos.to_json()[1], 3)
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'N')

        self.assertEqual(self._arena.B.pos.to_json()[0], 4)
        self.assertEqual(self._arena.B.pos.to_json()[1], 0)

        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')

        self.assertEqual(self._arena.G.pos.to_json()[0], 7)
        self.assertEqual(self._arena.G.pos.to_json()[1], 4)

        self._arena.moveKnightInArenaBoard(self._arena.Y.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.Y.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.Y.name, 'S')

        self.assertEqual(self._arena.Y.pos.to_json()[0], 3)
        self.assertEqual(self._arena.Y.pos.to_json()[1], 7)

    def testLivingStatus(self):
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'S')

        self.assertEqual(self._arena.B.status, 'DROWNED')
        self.assertEqual(self._arena.R.status, 'LIVE')
        self.assertEqual(self._arena.G.status, 'LIVE')
        self.assertEqual(self._arena.Y.status, 'LIVE')

    def testBattlingAndPositions(self):

        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'E')

        self.assertEqual(self._arena.R.pos.to_json()[0], 0)
        self.assertEqual(self._arena.R.pos.to_json()[1], 7)
        self.assertEqual(self._arena.G.status, 'DROWNED')
        self.assertEqual(self._arena.R.status, 'LIVE')
        self.assertEqual(self._arena.B.status, 'LIVE')
        self.assertEqual(self._arena.Y.status, 'DEAD')

    def testAttackAndDefenceScore(self):
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'E')

        self.assertEqual(self._arena.R.base_attack, 1)
        self.assertEqual(self._arena.R.base_defence, 1)
        self.assertEqual(self._arena.Y.base_attack, 0)
        self.assertEqual(self._arena.Y.base_defence, 0)
        self.assertEqual(self._arena.G.base_attack, 0)
        self.assertEqual(self._arena.G.base_defence, 0)
        self.assertEqual(self._arena.B.base_attack, 1)
        self.assertEqual(self._arena.B.base_defence, 1)

    def testAttacking(self):
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'E')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.B.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')
        self._arena.moveKnightInArenaBoard(self._arena.R.name, 'S')

        self.assertEqual(self._arena.R.status, 'LIVE')
        self.assertEqual(self._arena.B.status, 'DEAD')
        self.assertEqual(self._arena.R.base_attack, 1)
        self.assertEqual(self._arena.R.base_defence, 1)
        self.assertEqual(self._arena.B.base_attack, 0)
        self.assertEqual(self._arena.B.base_defence, 0)

    def testKillingKnight(self):
        self._arena.killTheKnight(self._arena.G, 1)
        self.assertEqual(self._arena.G.status, 'DEAD')
        self.assertEqual(self._arena.G.base_attack, 0)
        self.assertEqual(self._arena.G.base_defence, 0)
        self.assertEqual(self._arena.G.item, None)
        self.assertEqual(self._arena.G.pos.to_json(), [7, 7])

    def testGreenNotAbleToPickMagic(self):
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'N')

        self.assertEqual(self._arena.G.item, None)

    def testBlueAbleToPickMagic(self):
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'W')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'N')
        self._arena.moveKnightInArenaBoard(self._arena.G.name, 'N')

        self.assertEqual(self._arena.G.item, None)

if __name__ == '__main__':
    unittest.main(verbosity=5)
