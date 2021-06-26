import unittest

from candidate_translator import translate_left_fold
from candidate_translator import translate_right_fold
from candidate_translator import translate_down_fold
from candidate_translator import translate_up_fold




class CandidateTranslatorSpec(unittest.TestCase):

    def test_it_translates_left_fold_candidates_with_same_candidates(self):
        self.assertEqual([[0, 3]], translate_left_fold([[0, 3]]))
        self.assertEqual([[0, 3], [1, 3]], translate_left_fold([[0, 3], [1, 3]]))
        self.assertEqual([[0, 3], [1, 3], [2, 3]], translate_left_fold([[0, 3], [1, 3], [2, 3]]))
        self.assertEqual([[0, 3], [1, 3], [2, 3], [3, 3]], translate_left_fold([[0, 3], [1, 3], [2, 3], [3, 3]]))

    def test_it_translates_right_fold_candidates_with_mirrored_candidates(self):
        self.assertEqual([[3, 0]], translate_right_fold([[0, 3]]))
        self.assertEqual([[2, 0]], translate_right_fold([[1, 3]]))
        self.assertEqual([[1, 0]], translate_right_fold([[2, 3]]))
        self.assertEqual([[0, 0]], translate_right_fold([[3, 3]]))

    def test_it_translates_down_fold_candidates(self):
        self.assertEqual([[0, 0]], translate_down_fold([[0, 3]]))
        self.assertEqual([[0, 1]], translate_down_fold([[1, 3]]))
        self.assertEqual([[0, 2]], translate_down_fold([[2, 3]]))
        self.assertEqual([[0, 3]], translate_down_fold([[3, 3]]))

    def test_it_translates_up_fold_candidates(self):
        self.assertEqual([[3, 3]], translate_up_fold([[0, 3]]))
        self.assertEqual([[3, 2]], translate_up_fold([[1, 3]]))
        self.assertEqual([[3, 1]], translate_up_fold([[2, 3]]))
        self.assertEqual([[3, 0]], translate_up_fold([[3, 3]]))
