import unittest
from modules.game import *
from modules.player import *

class TestGame(unittest.TestCase):
    def test_paper_beats_rock(self):
        player_1 = Player("Emma", "rock")
        player_2 = Player ("Alice", "paper")
        game = Game()
        self.assertEqual(player_2, game.play(player_1, player_2))

        