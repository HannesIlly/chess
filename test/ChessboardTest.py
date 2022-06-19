import random
import unittest

import chessboard
from chessboard import Chessboard
from board_constants import *


class CreatePositionTest(unittest.TestCase):
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


class MoveUndoMoveTest(unittest.TestCase):
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

    def assert_position(self, position: Chessboard, move_number: int, half_move_counter: int, turn_white: bool = True,
                        /, castle_white_short: bool = True, castle_white_long: bool = True,
                        castle_black_short: bool = True, castle_black_long: bool = True,
                        en_passant: bool = False, en_passant_square: str = ''):
        """
        Compares the additional position data to the given values.
        :param position: The position.
        :param move_number: The move number.
        :param half_move_counter: The counter of irreversible half moves.
        :param turn_white: If it is white's turn.
        :param castle_white_short: If white can castle short.
        :param castle_white_long: If white can castle long.
        :param castle_black_short: If black can castle short.
        :param castle_black_long: If black can castle long.
        :param en_passant: If en passant is possible.
        :param en_passant_square: The square on which en passant is possible.
        :return:
        """
        self.assertEqual(position.get_move_number(), move_number, "The move number is incorrect!")
        self.assertEqual(position.get_move_counter_for_draw(), half_move_counter, "The draw counter is incorrect!")
        self.assertEqual(position.get_turn(), 'white' if turn_white else 'black', "It's the wrong player's turn!")
        self.assertEqual(position.castle['white']['short'], castle_white_short, "Short castle (white) is incorrect!")
        self.assertEqual(position.castle['white']['long'], castle_white_long, "Long castle (white) is incorrect!")
        self.assertEqual(position.castle['black']['short'], castle_black_short, "Short castle (black) is incorrect!")
        self.assertEqual(position.castle['black']['long'], castle_black_long, "Long castle (black) is incorrect!")
        self.assertEqual(position.is_en_passant_possible(), en_passant, "En passant is incorrect!")
        if position.is_en_passant_possible() and en_passant:
            self.assertEqual(position.get_en_passant_square(), chessboard.translate_field_into_index(en_passant_square),
                             "The en passant square is incorrect!")

    def test_move_undo_1(self):
        """
        Tests basic moves (reversible, no special moves).
        """
        # white to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 3 24')

        # Bc4
        start_square = 'b3'
        target_square = 'c4'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), BISHOP_WHITE)
        self.assert_position(board, 24, 4, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), BISHOP_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Qc3
        start_square = 'c2'
        target_square = 'c3'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), QUEEN_WHITE)
        self.assert_position(board, 24, 4, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), QUEEN_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Ng5
        start_square = 'f3'
        target_square = 'g5'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KNIGHT_WHITE)
        self.assert_position(board, 24, 4, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), KNIGHT_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # black to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R b KQkq - 3 24')

        # Nc5
        start_square = 'a4'
        target_square = 'c5'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KNIGHT_BLACK)
        self.assert_position(board, 25, 4, True)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), KNIGHT_BLACK)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, False)

        # Nf4
        start_square = 'g6'
        target_square = 'f4'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KNIGHT_BLACK)
        self.assert_position(board, 25, 4, True)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), KNIGHT_BLACK)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, False)

    def test_move_undo_2(self):
        """
        Test simple irreversible moves (takes, pawn moves)
        """
        # white to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 3 24')

        # g3 (irreversible)
        start_square = 'g2'
        target_square = 'g3'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), PAWN_WHITE)
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), PAWN_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Bxa4 (irreversible, takes)
        start_square = 'b3'
        target_square = 'a4'
        move = (SQUARES[start_square], SQUARES[target_square], KNIGHT_BLACK)  # bishop takes knight
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), BISHOP_WHITE)
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), BISHOP_WHITE)
        self.assertEqual(board.get_by_name(target_square), KNIGHT_BLACK)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Nxd4 (irreversible, takes)
        start_square = 'f3'
        target_square = 'd4'
        move = (SQUARES[start_square], SQUARES[target_square], QUEEN_BLACK)  # knight takes queen
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KNIGHT_WHITE)
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), KNIGHT_WHITE)
        self.assertEqual(board.get_by_name(target_square), QUEEN_BLACK)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # black to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R b KQkq - 3 24')

        # Nxe5 (irreversible, takes)
        start_square = 'g6'
        target_square = 'e5'
        move = (SQUARES[start_square], SQUARES[target_square], PAWN_WHITE)  # knight takes pawn
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KNIGHT_BLACK)
        self.assert_position(board, 25, 0, True)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), KNIGHT_BLACK)
        self.assertEqual(board.get_by_name(target_square), PAWN_WHITE)
        self.assert_position(board, 24, 3, False)

        # Bxe5 (irreversible, takes)
        start_square = 'c7'
        target_square = 'e5'
        move = (SQUARES[start_square], SQUARES[target_square], PAWN_WHITE)  # knight takes pawn
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), BISHOP_BLACK)
        self.assert_position(board, 25, 0, True)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), BISHOP_BLACK)
        self.assertEqual(board.get_by_name(target_square), PAWN_WHITE)
        self.assert_position(board, 24, 3, False)

        # cxb5 (irreversible, takes)
        start_square = 'c6'
        target_square = 'b5'
        move = (SQUARES[start_square], SQUARES[target_square], PAWN_WHITE)  # pawn takes pawn
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), PAWN_BLACK)
        self.assert_position(board, 25, 0, True)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), PAWN_BLACK)
        self.assertEqual(board.get_by_name(target_square), PAWN_WHITE)
        self.assert_position(board, 24, 3, False)

    def test_move_undo_3(self):
        """
        Test special moves for white.
        """
        # white to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 3 24')

        # Rc1 (irreversible (because of castle loss), castle loss long)
        start_square = 'a1'
        target_square = 'c1'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), ROOK_WHITE)
        self.assert_position(board, 24, 0, False, castle_white_long=False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), ROOK_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Ke2 (irreversible (because of castle loss), castle loss all)
        start_square = 'e1'
        target_square = 'e2'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KING_WHITE)
        self.assert_position(board, 24, 0, False, castle_white_long=False, castle_white_short=False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), KING_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # 0-0 (irreversible (because of castle loss), castle loss all)
        start_square = 'e1'
        target_square = 'g1'
        move = (SQUARES[start_square], SQUARES[target_square], CASTLE_SHORT)
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KING_WHITE)
        self.assertEqual(board.get_by_name('f1'), ROOK_WHITE)
        self.assertEqual(board.get_by_name('h1'), EMPTY)
        self.assert_position(board, 24, 0, False, castle_white_long=False, castle_white_short=False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), KING_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assertEqual(board.get_by_name('f1'), EMPTY)
        self.assertEqual(board.get_by_name('h1'), ROOK_WHITE)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # g8Q+ (irreversible, promotion)
        start_square = 'g7'
        target_square = 'g8'
        move = (SQUARES[start_square], SQUARES[target_square], QUEEN_WHITE)
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), QUEEN_WHITE)
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), PAWN_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # gxh8N (irreversible, promotion+takes)
        start_square = 'g7'
        target_square = 'h8'
        move = (SQUARES[start_square], SQUARES[target_square], KNIGHT_WHITE, ROOK_BLACK)
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), KNIGHT_WHITE)
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), PAWN_WHITE)
        self.assertEqual(board.get_by_name(target_square), ROOK_BLACK)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # bxa6 e.p. (irreversible, en passant)
        start_square = 'b5'
        target_square = 'a6'
        move = (SQUARES[start_square], SQUARES[target_square], EN_PASSANT)
        board.move(move)
        self.assertEqual(board.get_by_name(start_square), EMPTY)
        self.assertEqual(board.get_by_name(target_square), PAWN_WHITE)
        self.assertEqual(board.get_by_name('a5'), EMPTY)
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(board.get_by_name(start_square), PAWN_WHITE)
        self.assertEqual(board.get_by_name(target_square), EMPTY)
        self.assertEqual(board.get_by_name('a5'), PAWN_BLACK)
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

    def test_move_undo_4(self):
        """
        Test special moves for black.
        TODO complete tests
        TODO fix test fails
        """
        # d5 (irreversible, en passant possible)
        # Rg8 (irreversible (because of castle loss), castle loss short)
        # Kf7 (irreversible (because of castle loss), castle loss all)
        # 0-0-0 (irreversible (because of castle loss), castle loss all)


if __name__ == '__main__':
    unittest.main()
