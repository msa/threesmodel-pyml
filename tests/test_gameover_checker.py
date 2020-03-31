import unittest

from game_over_checker import is_game_over

class GameOverCheckerSpec(unittest.TestCase):

    def test_identifies_game_over(self):
        board = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        self.assertTrue(is_game_over(board))


    def test_a_game_with_at_least_one_empty_cell_is_not_over(self):
        board = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
        self.assertFalse(is_game_over(board))


    def test_a_game_with_one_foldable_couple_is_not_over(self):
        board = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 2]]
        self.assertFalse(is_game_over(board))

if __name__ == '__main__':
    unittest.main()
