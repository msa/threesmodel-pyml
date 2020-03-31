import unittest

from board_rotator import rotate

class BoardRotatorSpec(unittest.TestCase):
    def test_single_clockwise_rotation(self):
        self.assertEqual([['m', 'i', 'e', 'a'],
                          ['n', 'j', 'f', 'b'],
                          ['o', 'k', 'g', 'c'],
                          ['p', 'l', 'h', 'd']],
                         rotate([
                             ['a', 'b', 'c', 'd'],
                             ['e', 'f', 'g', 'h'],
                             ['i', 'j', 'k', 'l'],
                             ['m', 'n', 'o', 'p']], 1))

    def test_full_lap_rotation(self):
        self.assertEqual([['a', 'b', 'c', 'd'],
                          ['e', 'f', 'g', 'h'],
                          ['i', 'j', 'k', 'l'],
                          ['m', 'n', 'o', 'p']],
                         rotate([
                             ['a', 'b', 'c', 'd'],
                             ['e', 'f', 'g', 'h'],
                             ['i', 'j', 'k', 'l'],
                             ['m', 'n', 'o', 'p']], 4))



if __name__ == '__main__':
    unittest.main()
