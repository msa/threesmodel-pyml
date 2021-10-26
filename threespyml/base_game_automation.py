from board_folder import *
from score_calculator import *
from game_controller import GameController


class BaseGameAutomation:
    def __init__(self):
        self.game_controller = GameController()
        self.scores = []
        self.highest_cell_value_histogram = {3: 0, 6: 0, 12: 0, 24: 0, 48: 0, 96: 0,
                                             192: 0, 384: 0, 768: 0, 1536: 0, 3072: 0, 6144: 0}
        self.best_game = None

    def play(self, game):
        print("Please override the play(game) method")
        raise

    def score_filename(self):
        return self.__class__.__name__ + ".txt"

    def play_many(self, times=100):
        max_score = 0
        iteration = 1
        for i in range(1, times):
            game = self.game_controller.start_new_game()
            game = self.play(game)
            score = score_for(game["game"])
            if score > max_score:
                max_score = score
                print(game)
                self.best_game = game["game"]
            self.scores.append(score)
            if iteration % 1000 == 0:
                print(".")
            self.update_highest_value_histogram(game["game"])
            iteration += 1
        print("Done!")
        print(max_score)
        print(self.highest_cell_value_histogram)

#        f = open(self.score_filename(), "a")
#        f.write(" ".join(self.scores))

        print("Best game is:")
        print(self.best_game)

    def update_highest_value_histogram(self, game_board):
        highest_cell_value = max(max(game_board))
        self.highest_cell_value_histogram[highest_cell_value] = self.highest_cell_value_histogram[highest_cell_value] + 1
