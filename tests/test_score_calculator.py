import unittest

from score_calculator import score_for

class MyTestCase(unittest.TestCase):

    def test_high_scoring_board(self):
        self.assertEqual(7174452, score_for([[3, 6, 12, 24],
                                             [48, 96, 192, 384],
                                             [768, 1536, 3072, 6144],
                                             [12288, 24576, 0, 0]]))

    def test_zero_scoring_boards(self):
        self.assertEqual(0, score_for([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))



if __name__ == '__main__':
    unittest.main()
