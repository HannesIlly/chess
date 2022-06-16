import random
import unittest

import chessboard
from board_constants import *


class MyTestCase(unittest.TestCase):
    def test_starting_position_1(self):
        """
        Test all the pieces of the starting positions.
        """
        board = chessboard.create_starting_position()

        # row 1
        self.assertEqual(board.board[SQUARES['a1']], ROOK_WHITE)
        self.assertEqual(board.board[SQUARES['b1']], KNIGHT_WHITE)
        self.assertEqual(board.board[SQUARES['c1']], BISHOP_WHITE)
        self.assertEqual(board.board[SQUARES['d1']], QUEEN_WHITE)
        self.assertEqual(board.board[SQUARES['e1']], KING_WHITE)
        self.assertEqual(board.board[SQUARES['f1']], BISHOP_WHITE)
        self.assertEqual(board.board[SQUARES['g1']], KNIGHT_WHITE)
        self.assertEqual(board.board[SQUARES['h1']], ROOK_WHITE)
        # row 2
        self.assertEqual(board.board[SQUARES['a2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['b2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['c2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['d2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['e2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['f2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['g2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['h2']], PAWN_WHITE)

        # row 8
        self.assertEqual(board.board[SQUARES['a8']], ROOK_BLACK)
        self.assertEqual(board.board[SQUARES['b8']], KNIGHT_BLACK)
        self.assertEqual(board.board[SQUARES['c8']], BISHOP_BLACK)
        self.assertEqual(board.board[SQUARES['d8']], QUEEN_BLACK)
        self.assertEqual(board.board[SQUARES['e8']], KING_BLACK)
        self.assertEqual(board.board[SQUARES['f8']], BISHOP_BLACK)
        self.assertEqual(board.board[SQUARES['g8']], KNIGHT_BLACK)
        self.assertEqual(board.board[SQUARES['h8']], ROOK_BLACK)
        # row 7
        self.assertEqual(board.board[SQUARES['a7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['b7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['c7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['d7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['e7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['f7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['g7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['h7']], PAWN_BLACK)

    def test_starting_position_2(self):
        """
        Test some random empty fields of the starting position.
        """
        board = chessboard.create_starting_position()

        a = chessboard.SQUARES['h2'] + 1
        b = chessboard.SQUARES['a7'] - 1

        square_number = random.randint(a, b)
        self.assertEqual(board.board[square_number], chessboard.EMPTY)
        square_number = random.randint(a, b)
        self.assertEqual(board.board[square_number], chessboard.EMPTY)
        square_number = random.randint(a, b)
        self.assertEqual(board.board[square_number], chessboard.EMPTY)
        square_number = random.randint(a, b)
        self.assertEqual(board.board[square_number], chessboard.EMPTY)

    def test_starting_position_3(self):
        """
        Test additional information of the board in the initial state (e.g. move number, castle rights, turn).
        """
        board = chessboard.create_starting_position()

        # turn
        self.assertEqual(board.turn, 'white')
        # castle rights
        self.assertTrue(board.castle['white']['short'])
        self.assertTrue(board.castle['white']['long'])
        self.assertTrue(board.castle['black']['short'])
        self.assertTrue(board.castle['black']['long'])
        # counters
        self.assertEqual(board.move_number, 1)
        self.assertEqual(board.half_move_count_for_draw, 0)

    def test_create_from_fen_1(self):
        """
        Tests a specific position with many pieces and some additional info.
        """
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 3 24')

        # row 1
        self.assertEqual(board.board[SQUARES['a1']], ROOK_WHITE)
        self.assertEqual(board.board[SQUARES['b1']], EMPTY)
        self.assertEqual(board.board[SQUARES['c1']], EMPTY)
        self.assertEqual(board.board[SQUARES['d1']], EMPTY)
        self.assertEqual(board.board[SQUARES['e1']], KING_WHITE)
        self.assertEqual(board.board[SQUARES['f1']], EMPTY)
        self.assertEqual(board.board[SQUARES['g1']], EMPTY)
        self.assertEqual(board.board[SQUARES['h1']], ROOK_WHITE)
        # row 2
        self.assertEqual(board.board[SQUARES['a2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['b2']], EMPTY)
        self.assertEqual(board.board[SQUARES['c2']], QUEEN_WHITE)
        self.assertEqual(board.board[SQUARES['d2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['e2']], EMPTY)
        self.assertEqual(board.board[SQUARES['f2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['g2']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['h2']], EMPTY)
        # row 3
        self.assertEqual(board.board[SQUARES['a3']], EMPTY)
        self.assertEqual(board.board[SQUARES['b3']], BISHOP_WHITE)
        self.assertEqual(board.board[SQUARES['c3']], EMPTY)
        self.assertEqual(board.board[SQUARES['d3']], EMPTY)
        self.assertEqual(board.board[SQUARES['e3']], EMPTY)
        self.assertEqual(board.board[SQUARES['f3']], KNIGHT_WHITE)
        self.assertEqual(board.board[SQUARES['g3']], EMPTY)
        self.assertEqual(board.board[SQUARES['h3']], EMPTY)
        # row 4
        self.assertEqual(board.board[SQUARES['a4']], KNIGHT_BLACK)
        self.assertEqual(board.board[SQUARES['b4']], EMPTY)
        self.assertEqual(board.board[SQUARES['c4']], EMPTY)
        self.assertEqual(board.board[SQUARES['d4']], QUEEN_BLACK)
        self.assertEqual(board.board[SQUARES['e4']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['f4']], EMPTY)
        self.assertEqual(board.board[SQUARES['g4']], EMPTY)
        self.assertEqual(board.board[SQUARES['h4']], EMPTY)
        # row 5
        self.assertEqual(board.board[SQUARES['a5']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['b5']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['c5']], EMPTY)
        self.assertEqual(board.board[SQUARES['d5']], EMPTY)
        self.assertEqual(board.board[SQUARES['e5']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['f5']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['g5']], EMPTY)
        self.assertEqual(board.board[SQUARES['h5']], PAWN_WHITE)
        # row 6
        self.assertEqual(board.board[SQUARES['a6']], EMPTY)
        self.assertEqual(board.board[SQUARES['b6']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['c6']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['d6']], EMPTY)
        self.assertEqual(board.board[SQUARES['e6']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['f6']], EMPTY)
        self.assertEqual(board.board[SQUARES['g6']], KNIGHT_BLACK)
        self.assertEqual(board.board[SQUARES['h6']], EMPTY)
        # row 7
        self.assertEqual(board.board[SQUARES['a7']], EMPTY)
        self.assertEqual(board.board[SQUARES['b7']], EMPTY)
        self.assertEqual(board.board[SQUARES['c7']], BISHOP_BLACK)
        self.assertEqual(board.board[SQUARES['d7']], PAWN_BLACK)
        self.assertEqual(board.board[SQUARES['e7']], EMPTY)
        self.assertEqual(board.board[SQUARES['f7']], EMPTY)
        self.assertEqual(board.board[SQUARES['g7']], PAWN_WHITE)
        self.assertEqual(board.board[SQUARES['h7']], EMPTY)
        # row 8
        self.assertEqual(board.board[SQUARES['a8']], ROOK_BLACK)
        self.assertEqual(board.board[SQUARES['b8']], EMPTY)
        self.assertEqual(board.board[SQUARES['c8']], EMPTY)
        self.assertEqual(board.board[SQUARES['d8']], EMPTY)
        self.assertEqual(board.board[SQUARES['e8']], KING_BLACK)
        self.assertEqual(board.board[SQUARES['f8']], EMPTY)
        self.assertEqual(board.board[SQUARES['g8']], EMPTY)
        self.assertEqual(board.board[SQUARES['h8']], ROOK_BLACK)

        # turn
        self.assertEqual(board.turn, 'white')
        # castle rights
        self.assertTrue(board.castle['white']['short'])
        self.assertTrue(board.castle['white']['long'])
        self.assertTrue(board.castle['black']['short'])
        self.assertTrue(board.castle['black']['long'])
        # counters
        self.assertEqual(board.move_number, 24)
        self.assertEqual(board.half_move_count_for_draw, 3)
        # en passant
        self.assertTrue(board.en_passant)
        self.assertEqual(board.en_passant_square, SQUARES['a6'])

    def test_switch_turn(self):
        """
        Tests turn switching.
        """
        board = chessboard.create_starting_position()
        self.assertEqual(board.turn, 'white')
        board.switch_turn()
        self.assertEqual(board.turn, 'black')
        board.switch_turn()
        self.assertEqual(board.turn, 'white')

        board = chessboard.create_from_fen('rn2k1nr/1p4pp/3p4/p1pP4/PbP2p1q/1b2pPRP/1P1NP1PQ/2B1KBNR b K - 2 29')
        self.assertEqual(board.turn, 'black')
        board.switch_turn()
        self.assertEqual(board.turn, 'white')
        board.switch_turn()
        self.assertEqual(board.turn, 'black')


if __name__ == '__main__':
    unittest.main()
