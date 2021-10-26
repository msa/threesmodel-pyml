import unittest

from solvers.sample_automated_player import SampleAutomatedPlayer

class TestSampleClientSpec(unittest.TestCase):

    def test_run_solver(self):
        solver = SampleAutomatedPlayer()
        solver.play_many(100000)


if __name__ == '__main__':
    unittest.main()
