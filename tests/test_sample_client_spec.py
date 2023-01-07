import unittest

from solvers.sample_automated_player import SampleAutomatedPlayer

class TestSampleClientSpec(unittest.TestCase):

    def test_run_solver(self):
        solver = SampleAutomatedPlayer()
        solver.play_many(1001)

    def test_score_filename(self):
        solver = SampleAutomatedPlayer()
        self.assertEqual("SampleAutomatedPlayer.txt", solver.score_filename(solver.__class__))


if __name__ == '__main__':
    unittest.main()
