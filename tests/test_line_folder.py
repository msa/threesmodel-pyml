import unittest

from line_folder import wall_index_of
from line_folder import can_fold
from line_folder import fold
class LineFolderSpec(unittest.TestCase):

    def test_can_find_wall_in_position_zero(self):
        self.assertEqual(wall_index_of([0, 0, 1, 2]), 0)
        self.assertEqual(wall_index_of([1, 2, 0, 0]), 0)
        self.assertEqual(wall_index_of([2, 1, 0, 0]), 0)
        self.assertEqual(wall_index_of([0, 1, 0, 0]), 0)
        self.assertEqual(wall_index_of([3, 3, 0, 0]), 0)

    def test_can_find_wall_in_position_one(self):
        self.assertEqual(wall_index_of([1, 1, 2, 2]), 1)
        self.assertEqual(wall_index_of([2, 2, 1, 2]), 1)
        self.assertEqual(wall_index_of([3, 2, 1, 2]), 1)
        self.assertEqual(wall_index_of([2, 3, 3, 2]), 1)
        self.assertEqual(wall_index_of([1, 0, 2, 2]), 1)

    def test_can_find_wall_in_position_two(self):
        self.assertEqual(wall_index_of([1, 1, 1, 2]), 2)
        self.assertEqual(wall_index_of([2, 2, 2, 1]), 2)
        self.assertEqual(wall_index_of([2, 2, 3, 3]), 2)
        self.assertEqual(wall_index_of([2, 2, 0, 3]), 2)

    def test_can_fold_when_line_has_leading_zeros(self):
        self.assertEqual(can_fold([0, 0, 1, 2]), True)

    def test_can_not_fold_when_line_is_all_zeros(self):
        self.assertEqual(can_fold([0, 0, 0, 0]), False)

    def test_can_not_fold_when_line_is_all_ones(self):
        self.assertEqual(can_fold([1, 1, 1, 1]), False)

    def test_can_not_fold_when_line_is_all_twos(self):
        self.assertEqual(can_fold([2, 2, 2, 2]), False)

    def test_can_fold_when_line_has_a_one_and_a_two_adjacent(self):
        self.assertEqual(can_fold([1, 2, 1, 1]), True)

    def test_can_fold_when_line_has_a_two_and_a_one_adjacent(self):
        self.assertEqual(can_fold([2, 1, 1, 1]), True)

    def test_can_not_fold(self):
        self.assertEqual(can_fold([2, 0, 0, 0]), False)
        self.assertEqual(can_fold([24, 3, 6, 0]), False)
        self.assertEqual(can_fold([1, 6, 2, 0]), False)
        self.assertEqual(can_fold([24, 12, 2, 3]), False)

    def test_can_not_even_fold(self):
        self.assertEqual(can_fold([6, 2, 0, 0]), False)
        self.assertEqual(can_fold([12, 6, 0, 0]), False)
        self.assertEqual(can_fold([1, 1, 3, 0]), False)
        self.assertEqual(can_fold([6, 1, 12, 2]), False)

    def test_no_folds_when_all_zeros(self):
        self.assertEqual(fold([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_folds_by_shifting_onto_leading_zeros(self):
        self.assertEqual(fold([0, 0, 1, 2]), [0, 1, 2, 0])

    def test_folds_by_shifting_onto_zeros(self):
        self.assertEqual(fold([1, 0, 1, 2]), [1, 1, 2, 0])

    def test_folds_by_adding_and_two_at_a_wall(self):
        self.assertEqual(fold([1, 2, 0, 0]), [3, 0, 0, 0])

    def test_folds_by_adding_and_two_at_a_non_foldable_cell(self):
        self.assertEqual(fold([3, 2, 1, 0]), [3, 3, 0, 0])

    def test_folds_by_adding_equal_numbers_at_a_wall(self):
        self.assertEqual(fold([3, 3, 0, 0]), [6, 0, 0, 0])

    def test_folds_by_adding_two_equal_cells_at_a_non_foldable_cell(self):
        self.assertEqual(fold([12, 6, 6, 3]), [12, 12, 3, 0])

    def test_only_folds_first_pair_of_equal_numbers(self):
        self.assertEqual(fold([12, 12, 3, 3]), [24, 3, 3, 0])

    def test_prioritizes_leftward_folds(self):
        self.assertEqual(fold([1, 2, 0, 3]), [3, 0, 3, 0])

    def test_wall_index_of_three(self):
        self.assertEqual(wall_index_of([0, 0, 0, 0]), 3)
        self.assertEqual(wall_index_of([1, 1, 1, 1]), 3)
        self.assertEqual(wall_index_of([2, 2, 2, 2]), 3)
        self.assertEqual(wall_index_of([2, 0, 0, 0]), 3)
        self.assertEqual(wall_index_of([2, 2, 0, 0]), 3)
        self.assertEqual(wall_index_of([3, 1, 1, 1]), 3)
        self.assertEqual(wall_index_of([3, 6, 1, 1]), 3)
        self.assertEqual(wall_index_of([3, 2, 2, 2]), 3)
        self.assertEqual(wall_index_of([3, 6, 2, 2]), 3)

