import unittest

from candidate_extractor import fold_left_candidates
from candidate_extractor import fold_up_candidates
from candidate_extractor import fold_down_candidates
from candidate_extractor import fold_right_candidates


def create_unfoldable_board():
    return [[3, 1, 1, 3], [6, 1, 1, 6], [12, 1, 3, 12], [24, 1, 6, 24]]


class TestCandidateExtractor(unittest.TestCase):

    def test_it_extracts_no_candidates_from_an_unfoldable_board(self):
        game = create_unfoldable_board()
        self.assertEqual([], fold_left_candidates(game))
        self.assertEqual([], fold_right_candidates(game))
        self.assertEqual([], fold_up_candidates(game))
        self.assertEqual([], fold_down_candidates(game))

    def test_it_extracts_a_single_candidate_from_a_board_with_one_left_foldable_line(self):
        self.assertEqual([[2, 3]],  fold_left_candidates([[3, 1, 1, 3], [6, 1, 1, 6], [12, 1, 2, 12], [24, 1, 6, 24]]))

    def test_it_extracts_a_single_candidate_from_a_board_with_one_right_foldable_line(self):
        self.assertEqual([[1, 3]],  fold_right_candidates([[3, 1, 1, 3], [6, 1, 1, 6], [12, 1, 2, 12], [24, 1, 6, 24]]))

    def test_it_extracts_a_single_candidate_from_a_board_with_one_up_foldable_line(self):
        self.assertEqual([[1, 3]],  fold_up_candidates([[3, 1, 1, 3], [6, 1, 1, 6], [12, 1, 2, 12], [24, 1, 6, 24]]))

    def test_it_extracts_a_single_candidate_from_a_board_with_one_down_foldable_line(self):
        self.assertEqual([[2, 3]],  fold_down_candidates([[3, 1, 1, 3], [6, 1, 1, 6], [12, 1, 2, 12], [24, 1, 6, 24]]))

    def test_folding_board_with_two_candidates(self):
        self.assertEqual([[2, 3], [3, 3]], fold_right_candidates([[2, 0, 0, 0], [1, 1, 3, 0], [6, 1, 6, 3], [6, 1, 1, 1]]))

    def test_something(self):
        self.assertEqual([[0, 3], [2, 3], [3, 3]], fold_down_candidates([[6, 1, 3, 2], [3, 1, 6, 3], [2, 6, 1, 1], [0, 1, 0, 0]]))

    def test_extracts_all_four_candidates_from_a_board_where_all_lines_fold(self):
        self.assertEqual([[0, 3], [1, 3], [2, 3], [3, 3]], fold_left_candidates(
            [[3, 3, 1, 3], [6, 3, 3, 6], [12, 1, 12, 12], [3, 3, 3, 3]]))


if __name__ == '__main__':
    unittest.main()
