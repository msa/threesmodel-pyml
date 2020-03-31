import unittest

from board_folder import fold_left
from board_folder import fold_up
from board_folder import fold_down
from board_folder import fold_right
from board_folder import can_fold_left
from board_folder import can_fold_right
from board_folder import can_fold_up
from board_folder import can_fold_down


class BoardFolderSpec(unittest.TestCase):

    def test_fold_left(self):
        board = [[1, 2, 0, 0], [1, 2, 0, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertEqual([[3, 0, 0, 0], [3, 0, 0, 0], [3, 0, 0, 0], [3, 0, 0, 0]], fold_left(board))

    def test_fold_up(self):
        board = [[3, 2, 0, 0], [3, 2, 1, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertEqual([[6, 2, 1, 0], [1, 2, 0, 0], [1, 2, 0, 0], [0, 2, 0, 0]], fold_up(board))

    def test_fold_down(self):
        board = [[3, 2, 0, 0], [3, 2, 1, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertEqual([[0, 2, 0, 0], [6, 2, 0, 0], [1, 2, 1, 0], [1, 2, 0, 0]], fold_down(board))

    def test_fold_right(self):
        board = [[3, 2, 0, 0], [3, 2, 1, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertEqual([[0, 3, 2, 0], [0, 3, 2, 1], [0, 1, 2, 0], [0, 1, 2, 0]], fold_right(board))

    def test_can_fold_left(self):
        board = [[3, 2, 0, 0], [3, 2, 1, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertTrue(can_fold_left(board))

    def test_cannot_fold_left(self):
        board = [[3, 2, 2, 3], [3, 2, 2, 0], [2, 2, 0, 0], [2, 2, 0, 0]]
        self.assertFalse(can_fold_left(board))
        self.assertTrue(can_fold_right(board))

    def test_can_fold_right(self):
        board = [[3, 2, 2, 3], [0, 2, 2, 3], [2, 2, 0, 0], [2, 2, 0, 0]]
        self.assertTrue(can_fold_right(board))

    def test_cannot_fold_right(self):
        board = [[3, 2, 6, 12], [3, 2, 2, 12], [3, 2, 3, 2], [3, 2, 2, 3]]
        self.assertFalse(can_fold_right(board))

    def test_can_fold_up(self):
        board = [[3, 2, 0, 0], [3, 1, 1, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertTrue(can_fold_up(board))

    def test_cannot_fold_up(self):
        board = [[3, 3, 3, 3], [6, 6, 6, 6], [12, 12, 12, 12], [24, 24, 0, 0]]
        self.assertFalse(can_fold_up(board))

    def test_can_fold_down(self):
        board = [[3, 2, 0, 0], [3, 2, 1, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertTrue(can_fold_down(board))

    def test_cannot_fold_down(self):
        board = [[3, 2, 0, 0], [6, 2, 0, 0], [1, 2, 0, 0], [1, 2, 0, 0]]
        self.assertFalse(can_fold_down(board))


if __name__ == '__main__':
    unittest.main()
