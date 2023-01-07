import unittest

from solvers.incomplete_solver import IncompleteSolver


class TestIncompleteSolver(unittest.TestCase):

    def test_something(self):
        solver = IncompleteSolver()
        self.assertEqual("Hello!", solver.something())

    def test_run_solver(self):
        solver = IncompleteSolver()
        with self.assertRaises(Exception) as context:
            solver.play_many()
        self.assertTrue("Please override the play(game) method" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
