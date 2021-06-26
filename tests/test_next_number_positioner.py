import unittest

from next_number_positioner import select_position


class TestNextNumberPositioner(unittest.TestCase):

    def test_it_will_choose_the_one_candidate_available(self):
        self.assertEqual(select_position([[0, 1]]), [0, 1])

    def test_it_will_return_one_of_the_candidates_given_many_candidates(self):
        self.assertIn(select_position([[0, 0], [0, 1], [0, 2], [0, 3]]), [[0, 0], [0, 1], [0, 2], [0, 3]])


if __name__ == '__main__':
    unittest.main()
