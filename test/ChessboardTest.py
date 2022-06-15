import random
import unittest

import chessboard


class MyTestCase(unittest.TestCase):
    def test_starting_position_1(self):
        """
        Test all the pieces of the starting positions.
        """
        board = chessboard.create_starting_position()

        # row 1
        self.assertEqual(board.board[chessboard.SQUARES['a1']], chessboard.ROOK_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['b1']], chessboard.KNIGHT_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['c1']], chessboard.BISHOP_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['d1']], chessboard.QUEEN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['e1']], chessboard.KING_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['f1']], chessboard.BISHOP_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['g1']], chessboard.KNIGHT_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['h1']], chessboard.ROOK_WHITE)
        # row 2
        self.assertEqual(board.board[chessboard.SQUARES['a2']], chessboard.PAWN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['b2']], chessboard.PAWN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['c2']], chessboard.PAWN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['d2']], chessboard.PAWN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['e2']], chessboard.PAWN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['f2']], chessboard.PAWN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['g2']], chessboard.PAWN_WHITE)
        self.assertEqual(board.board[chessboard.SQUARES['h2']], chessboard.PAWN_WHITE)

        # row 8
        self.assertEqual(board.board[chessboard.SQUARES['a8']], chessboard.ROOK_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['b8']], chessboard.KNIGHT_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['c8']], chessboard.BISHOP_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['d8']], chessboard.QUEEN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['e8']], chessboard.KING_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['f8']], chessboard.BISHOP_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['g8']], chessboard.KNIGHT_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['h8']], chessboard.ROOK_BLACK)
        # row 7
        self.assertEqual(board.board[chessboard.SQUARES['a7']], chessboard.PAWN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['b7']], chessboard.PAWN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['c7']], chessboard.PAWN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['d7']], chessboard.PAWN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['e7']], chessboard.PAWN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['f7']], chessboard.PAWN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['g7']], chessboard.PAWN_BLACK)
        self.assertEqual(board.board[chessboard.SQUARES['h7']], chessboard.PAWN_BLACK)

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

if __name__ == '__main__':
    unittest.main()
