from board_creator import create_game_board
from next_number_determinator import select_number
from game_over_checker import is_game_over
from score_calculator import score_for

from board_folder import can_fold_right
from board_folder import can_fold_left
from board_folder import can_fold_up
from board_folder import can_fold_down


from candidate_translator import translate_right_fold
from candidate_translator import translate_left_fold
from candidate_translator import translate_up_fold
from candidate_translator import translate_down_fold


from candidate_extractor import fold_right_candidates
from candidate_extractor import fold_left_candidates
from candidate_extractor import fold_up_candidates
from candidate_extractor import fold_down_candidates


from board_folder import fold_right
from board_folder import fold_left
from board_folder import fold_up
from board_folder import fold_down

from next_number_positioner import select_position

import uuid

class GameController:

    def __init__(self):
        self.games = {}
        self.next_number = {}


    def start_new_game(self):
        game_id = uuid.uuid4()
        self.games[game_id] = create_game_board()
        self.next_number[game_id] = select_number(self.games[game_id])
        return self.respond_to_player(game_id)

    def respond_to_player(self, game_id):
        return {"id": game_id, "game": self.games[game_id], "next_number": self.next_number[game_id], "game_over": is_game_over(self.games[game_id]), "score": score_for(self.games[game_id])}

    def fold_right(self, game_id):
        game = self.games[game_id]
        if not (can_fold_right(game)):
            return self.did_not_fold(game_id)
        candidates = translate_right_fold(fold_right_candidates(game))
        game = fold_right(game)
        return self.prepare_for_next_fold(candidates, game, game_id)

    def fold_left(self, game_id):
        game = self.games[game_id]
        if not (can_fold_left(game)):
            return self.did_not_fold(game_id)
        candidates = translate_left_fold(fold_left_candidates(game))
        game = fold_left(game)
        return self.prepare_for_next_fold(candidates, game, game_id)

    def fold_up(self, game_id):
        game = self.games[game_id]
        if not (can_fold_up(game)):
            return self.did_not_fold(game_id)
        candidates = translate_up_fold(fold_up_candidates(game))
        game = fold_up(game)
        return self.prepare_for_next_fold(candidates, game, game_id)

    def fold_down(self, game_id):
        game = self.games[game_id]
        if not (can_fold_down(game)):
            return self.did_not_fold(game_id)
        candidates = translate_down_fold(fold_down_candidates(game))
        game = fold_down(game)
        return self.prepare_for_next_fold(candidates, game, game_id)

    def prepare_for_next_fold(self, candidates, game, game_id):
        new_game = self.add_next_number(game_id, candidates, game)
        self.next_number[game_id] = select_number(new_game)
        self.games[game_id] = new_game
        return self.respond_to_player(game_id)

    def add_next_number(self, game_id, candidates, game):
        coordinates = select_position(candidates)
        game[coordinates[0]][coordinates[1]] = self.next_number[game_id]
        return game

    def did_not_fold(self, game_id):
        return  self.respond_to_player(game_id)

