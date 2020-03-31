import unittest

from board_creator import create_game_board

class TestBoardCreator(unittest.TestCase):

    def test_it_assigns_nine_cells_initial_value(self):
        game = create_game_board()

        self.assertEqual(self.cells_in_game(game), 9)

    def cells_in_game(self, game_state):
        cells = 0
        for row in game_state:
            for val in row:
                if val > 0:
                    cells = cells + 1
        return cells

if __name__ == '__main__':
    unittest.main()
