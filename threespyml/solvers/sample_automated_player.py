from base_game_automation import BaseGameAutomation
from game_over_checker import is_game_over


class SampleAutomatedPlayer(BaseGameAutomation):

    def play(self, game):
        while not is_game_over(game["game"]):
            game = self.game_controller.fold_right(game["id"])
            game = self.game_controller.fold_up(game["id"])
            game = self.game_controller.fold_left(game["id"])
            game = self.game_controller.fold_down(game["id"])
        return game
