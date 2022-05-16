import math
import random
import time

import chessboard
from chessboard import Chessboard


class Engine:

    def __init__(self, initial_position: Chessboard):
        self.position = initial_position

    def make_move(self, depth: int):
        """
        Calculates the best move and executes it.
        :param depth: The depth of the search tree.
        """
        start_time = time.time()

        # avoid bad depths
        if depth < 0:
            depth = 3
        if depth > 10:
            depth = 10

        # calculate move
        move, evaluation = self.search(depth)
        # print move, eval and needed time
        duration = time.time() - start_time
        print('Computer moves: ', move, ', eval =', evaluation, ', duration = ', duration)  # TODO remove print?

        # make move
        self.position.move(move)

    def search(self, depth: int) -> tuple:
        if self.position.turn == 'white':
            return self.max(depth)
        else:
            return self.min(depth)

    def max(self, depth: int) -> tuple:
        if depth == 0:
            return (), self.evaluate()

        moves = self.position.generate_moves()
        if len(moves) == 0:
            return (), self.evaluate()

        best_evaluation = -math.inf
        best_move = moves[0]
        for move in moves:
            self.position.move(move)
            current_evaluation = self.min(depth - 1)[1]
            if current_evaluation == best_evaluation:
                # random choice between moves (50/50)
                if bool(random.getrandbits(1)):
                    best_evaluation = current_evaluation
                    best_move = move
            elif current_evaluation > best_evaluation:
                best_evaluation = current_evaluation
                best_move = move
            self.position.undo_last_move()
        return best_move, best_evaluation

    def min(self, depth: int) -> tuple:
        if depth == 0:
            return (), self.evaluate()

        moves = self.position.generate_moves()
        if len(moves) == 0:
            return (), self.evaluate()

        best_evaluation = math.inf
        best_move = moves[0]
        for move in moves:
            self.position.move(move)
            current_evaluation = self.max(depth - 1)[1]
            if current_evaluation == best_evaluation:
                # random choice between moves (50/50)
                if bool(random.getrandbits(1)):
                    best_evaluation = current_evaluation
                    best_move = move
            elif current_evaluation < best_evaluation:
                best_evaluation = current_evaluation
                best_move = move
            self.position.undo_last_move()
        return best_move, best_evaluation

    def evaluate(self):
        return evaluate(self.position)


def evaluate(position: Chessboard) -> int:
    # check for win and draw
    if position.is_checkmate():
        if position.turn == 'white':
            return -100
        else:
            return 100
    elif position.is_draw():
        return 0

    evaluation = 0
    # count pieces
    for field in range(64):
        if not position.is_empty(field):
            if position.has_piece(field, chessboard.KING_WHITE):
                pass
            elif position.has_piece(field, chessboard.QUEEN_WHITE):
                evaluation += 9
            elif position.has_piece(field, chessboard.ROOK_WHITE):
                evaluation += 5
            elif position.has_piece(field, chessboard.BISHOP_WHITE):
                evaluation += 3
            elif position.has_piece(field, chessboard.KNIGHT_WHITE):
                evaluation += 3
            elif position.has_piece(field, chessboard.PAWN_WHITE):
                evaluation += 1
            elif position.has_piece(field, chessboard.KING_BLACK):
                pass
            elif position.has_piece(field, chessboard.QUEEN_BLACK):
                evaluation -= 9
            elif position.has_piece(field, chessboard.ROOK_BLACK):
                evaluation -= 5
            elif position.has_piece(field, chessboard.BISHOP_BLACK):
                evaluation -= 3
            elif position.has_piece(field, chessboard.KNIGHT_BLACK):
                evaluation -= 3
            elif position.has_piece(field, chessboard.PAWN_BLACK):
                evaluation -= 1

    return evaluation
