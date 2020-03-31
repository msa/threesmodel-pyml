import unittest

from board_creator import create_game_board
from next_number_determinator import select_number
from next_number_determinator import highest_number

class TestNextNumberDeterminator(unittest.TestCase):

    def test_it_can_identify_highest_number_in_newly_created_game(self):
        game = create_game_board()

        self.assertEqual(highest_number(game), 3)

    def test_it_can_identify_highest_number_in_advanced_game(self):
        game = [[1, 6, 12, 48], [24, 96, 6, 192], [768, 384, 0, 3], [3, 24, 24, 192]]

        self.assertEqual(highest_number(game), 768)

    def test_it_will_not_assign_higher_new_number_than_192_for_a_768_game(self):
        game = [[1, 6, 12, 48], [24, 96, 6, 192], [768, 384, 0, 3], [3, 24, 24, 192]]

        self.assertTrue(select_number(game) <= 192)


if __name__ == '__main__':
    unittest.main()
