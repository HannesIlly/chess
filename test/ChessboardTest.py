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
        self.assertEqual(ROOK_WHITE, board.board[SQUARES['a1']])
        self.assertEqual(KNIGHT_WHITE, board.board[SQUARES['b1']])
        self.assertEqual(BISHOP_WHITE, board.board[SQUARES['c1']])
        self.assertEqual(QUEEN_WHITE, board.board[SQUARES['d1']])
        self.assertEqual(KING_WHITE, board.board[SQUARES['e1']])
        self.assertEqual(BISHOP_WHITE, board.board[SQUARES['f1']])
        self.assertEqual(KNIGHT_WHITE, board.board[SQUARES['g1']])
        self.assertEqual(ROOK_WHITE, board.board[SQUARES['h1']])
        # row 2
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['a2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['b2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['c2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['d2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['e2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['f2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['g2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['h2']])

        # row 8
        self.assertEqual(ROOK_BLACK, board.board[SQUARES['a8']])
        self.assertEqual(KNIGHT_BLACK, board.board[SQUARES['b8']])
        self.assertEqual(BISHOP_BLACK, board.board[SQUARES['c8']])
        self.assertEqual(QUEEN_BLACK, board.board[SQUARES['d8']])
        self.assertEqual(KING_BLACK, board.board[SQUARES['e8']])
        self.assertEqual(BISHOP_BLACK, board.board[SQUARES['f8']])
        self.assertEqual(KNIGHT_BLACK, board.board[SQUARES['g8']])
        self.assertEqual(ROOK_BLACK, board.board[SQUARES['h8']])
        # row 7
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['a7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['b7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['c7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['d7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['e7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['f7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['g7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['h7']])

    def test_starting_position_2(self):
        """
        Test some random empty fields of the starting position.
        """
        board = chessboard.create_starting_position()

        a = chessboard.SQUARES['h2'] + 1
        b = chessboard.SQUARES['a7'] - 1

        square_number = random.randint(a, b)
        self.assertEqual(EMPTY, board.board[square_number], 'The field should not be empty in the starting position!')
        square_number = random.randint(a, b)
        self.assertEqual(EMPTY, board.board[square_number], 'The field should not be empty in the starting position!')
        square_number = random.randint(a, b)
        self.assertEqual(EMPTY, board.board[square_number], 'The field should not be empty in the starting position!')
        square_number = random.randint(a, b)
        self.assertEqual(EMPTY, board.board[square_number], 'The field should not be empty in the starting position!')

    def test_starting_position_3(self):
        """
        Test additional information of the board in the initial state (e.g. move number, castle rights, turn).
        """
        board = chessboard.create_starting_position()

        # turn
        self.assertEqual('white', board.get_turn())
        # castle rights
        self.assertTrue(board.castle['white']['short'])
        self.assertTrue(board.castle['white']['long'])
        self.assertTrue(board.castle['black']['short'])
        self.assertTrue(board.castle['black']['long'])
        # counters
        self.assertEqual(1, board.get_move_number())
        self.assertEqual(0, board.get_move_counter_for_draw())

    def test_create_from_fen_1(self):
        """
        Tests a specific position with many pieces and some additional info.
        """
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 3 24')

        # row 1
        self.assertEqual(ROOK_WHITE, board.board[SQUARES['a1']])
        self.assertEqual(EMPTY, board.board[SQUARES['b1']])
        self.assertEqual(EMPTY, board.board[SQUARES['c1']])
        self.assertEqual(EMPTY, board.board[SQUARES['d1']])
        self.assertEqual(KING_WHITE, board.board[SQUARES['e1']])
        self.assertEqual(EMPTY, board.board[SQUARES['f1']])
        self.assertEqual(EMPTY, board.board[SQUARES['g1']])
        self.assertEqual(ROOK_WHITE, board.board[SQUARES['h1']])
        # row 2
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['a2']])
        self.assertEqual(EMPTY, board.board[SQUARES['b2']])
        self.assertEqual(QUEEN_WHITE, board.board[SQUARES['c2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['d2']])
        self.assertEqual(EMPTY, board.board[SQUARES['e2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['f2']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['g2']])
        self.assertEqual(EMPTY, board.board[SQUARES['h2']])
        # row 3
        self.assertEqual(EMPTY, board.board[SQUARES['a3']])
        self.assertEqual(BISHOP_WHITE, board.board[SQUARES['b3']])
        self.assertEqual(EMPTY, board.board[SQUARES['c3']])
        self.assertEqual(EMPTY, board.board[SQUARES['d3']])
        self.assertEqual(EMPTY, board.board[SQUARES['e3']])
        self.assertEqual(KNIGHT_WHITE, board.board[SQUARES['f3']])
        self.assertEqual(EMPTY, board.board[SQUARES['g3']])
        self.assertEqual(EMPTY, board.board[SQUARES['h3']])
        # row 4
        self.assertEqual(KNIGHT_BLACK, board.board[SQUARES['a4']])
        self.assertEqual(EMPTY, board.board[SQUARES['b4']])
        self.assertEqual(EMPTY, board.board[SQUARES['c4']])
        self.assertEqual(QUEEN_BLACK, board.board[SQUARES['d4']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['e4']])
        self.assertEqual(EMPTY, board.board[SQUARES['f4']])
        self.assertEqual(EMPTY, board.board[SQUARES['g4']])
        self.assertEqual(EMPTY, board.board[SQUARES['h4']])
        # row 5
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['a5']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['b5']])
        self.assertEqual(EMPTY, board.board[SQUARES['c5']])
        self.assertEqual(EMPTY, board.board[SQUARES['d5']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['e5']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['f5']])
        self.assertEqual(EMPTY, board.board[SQUARES['g5']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['h5']])
        # row 6
        self.assertEqual(EMPTY, board.board[SQUARES['a6']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['b6']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['c6']])
        self.assertEqual(EMPTY, board.board[SQUARES['d6']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['e6']])
        self.assertEqual(EMPTY, board.board[SQUARES['f6']])
        self.assertEqual(KNIGHT_BLACK, board.board[SQUARES['g6']])
        self.assertEqual(EMPTY, board.board[SQUARES['h6']])
        # row 7
        self.assertEqual(EMPTY, board.board[SQUARES['a7']])
        self.assertEqual(EMPTY, board.board[SQUARES['b7']])
        self.assertEqual(BISHOP_BLACK, board.board[SQUARES['c7']])
        self.assertEqual(PAWN_BLACK, board.board[SQUARES['d7']])
        self.assertEqual(EMPTY, board.board[SQUARES['e7']])
        self.assertEqual(EMPTY, board.board[SQUARES['f7']])
        self.assertEqual(PAWN_WHITE, board.board[SQUARES['g7']])
        self.assertEqual(EMPTY, board.board[SQUARES['h7']])
        # row 8
        self.assertEqual(ROOK_BLACK, board.board[SQUARES['a8']])
        self.assertEqual(EMPTY, board.board[SQUARES['b8']])
        self.assertEqual(EMPTY, board.board[SQUARES['c8']])
        self.assertEqual(EMPTY, board.board[SQUARES['d8']])
        self.assertEqual(KING_BLACK, board.board[SQUARES['e8']])
        self.assertEqual(EMPTY, board.board[SQUARES['f8']])
        self.assertEqual(EMPTY, board.board[SQUARES['g8']])
        self.assertEqual(ROOK_BLACK, board.board[SQUARES['h8']])

        # turn
        self.assertEqual('white', board.get_turn())
        # castle rights
        self.assertTrue(board.castle['white']['short'])
        self.assertTrue(board.castle['white']['long'])
        self.assertTrue(board.castle['black']['short'])
        self.assertTrue(board.castle['black']['long'])
        # counters
        self.assertEqual(24, board.move_number)
        self.assertEqual(3, board.half_move_count_for_draw)
        # en passant
        self.assertTrue(board.en_passant)
        self.assertEqual(SQUARES['a6'], board.get_en_passant_square())


class MoveUndoMoveTest(unittest.TestCase):
    def test_switch_turn(self):
        """
        Tests turn switching.
        """
        board = chessboard.create_starting_position()
        self.assertEqual('white', board.get_turn())
        board.switch_turn()
        self.assertEqual('black', board.get_turn())
        board.switch_turn()
        self.assertEqual('white', board.get_turn())

        board = chessboard.create_from_fen('rn2k1nr/1p4pp/3p4/p1pP4/PbP2p1q/1b2pPRP/1P1NP1PQ/2B1KBNR b K - 2 29')
        self.assertEqual('black', board.get_turn())
        board.switch_turn()
        self.assertEqual('white', board.get_turn())
        board.switch_turn()
        self.assertEqual('black', board.get_turn())

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
        self.assertEqual(move_number, position.get_move_number(), "The move number is incorrect!")
        self.assertEqual(half_move_counter, position.get_move_counter_for_draw(), "The draw counter is incorrect!")
        self.assertEqual('white' if turn_white else 'black', position.get_turn(), "It's the wrong player's turn!")
        self.assertEqual(castle_white_short, position.castle['white']['short'], "Short castle (white) is incorrect!")
        self.assertEqual(castle_white_long, position.castle['white']['long'], "Long castle (white) is incorrect!")
        self.assertEqual(castle_black_short, position.castle['black']['short'], "Short castle (black) is incorrect!")
        self.assertEqual(castle_black_long, position.castle['black']['long'], "Long castle (black) is incorrect!")
        self.assertEqual(en_passant, position.is_en_passant_possible(), "En passant is incorrect!")
        if position.is_en_passant_possible() and en_passant:
            self.assertEqual(chessboard.translate_field_into_index(en_passant_square), position.get_en_passant_square(),
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
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(BISHOP_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 4, False)
        board.undo_last_move()
        self.assertEqual(BISHOP_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Qc3
        start_square = 'c2'
        target_square = 'c3'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(QUEEN_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 4, False)
        board.undo_last_move()
        self.assertEqual(QUEEN_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Ng5
        start_square = 'f3'
        target_square = 'g5'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KNIGHT_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 4, False)
        board.undo_last_move()
        self.assertEqual(KNIGHT_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # black to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R b KQkq - 3 24')

        # Nc5
        start_square = 'a4'
        target_square = 'c5'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KNIGHT_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 4, True)
        board.undo_last_move()
        self.assertEqual(KNIGHT_BLACK, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, False)

        # Nf4
        start_square = 'g6'
        target_square = 'f4'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KNIGHT_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 4, True)
        board.undo_last_move()
        self.assertEqual(KNIGHT_BLACK, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
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
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(PAWN_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(PAWN_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Bxa4 (irreversible, takes)
        start_square = 'b3'
        target_square = 'a4'
        move = (SQUARES[start_square], SQUARES[target_square], KNIGHT_BLACK)  # bishop takes knight
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(BISHOP_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(BISHOP_WHITE, board.get_by_name(start_square))
        self.assertEqual(KNIGHT_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Nxd4 (irreversible, takes)
        start_square = 'f3'
        target_square = 'd4'
        move = (SQUARES[start_square], SQUARES[target_square], QUEEN_BLACK)  # knight takes queen
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KNIGHT_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(KNIGHT_WHITE, board.get_by_name(start_square))
        self.assertEqual(QUEEN_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # black to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R b KQkq - 3 24')

        # Nxe5 (irreversible, takes)
        start_square = 'g6'
        target_square = 'e5'
        move = (SQUARES[start_square], SQUARES[target_square], PAWN_WHITE)  # knight takes pawn
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KNIGHT_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 0, True)
        board.undo_last_move()
        self.assertEqual(KNIGHT_BLACK, board.get_by_name(start_square))
        self.assertEqual(PAWN_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, False)

        # Bxe5 (irreversible, takes)
        start_square = 'c7'
        target_square = 'e5'
        move = (SQUARES[start_square], SQUARES[target_square], PAWN_WHITE)  # knight takes pawn
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(BISHOP_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 0, True)
        board.undo_last_move()
        self.assertEqual(BISHOP_BLACK, board.get_by_name(start_square))
        self.assertEqual(PAWN_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, False)

        # cxb5 (irreversible, takes)
        start_square = 'c6'
        target_square = 'b5'
        move = (SQUARES[start_square], SQUARES[target_square], PAWN_WHITE)  # pawn takes pawn
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(PAWN_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 0, True)
        board.undo_last_move()
        self.assertEqual(PAWN_BLACK, board.get_by_name(start_square))
        self.assertEqual(PAWN_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, False)

    def test_move_undo_3(self):
        """
        Test special moves for white.
        """
        # white to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 3 24')

        # Rc1 (castle loss long)
        start_square = 'a1'
        target_square = 'c1'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(ROOK_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 4, False, castle_white_long=False)
        board.undo_last_move()
        self.assertEqual(ROOK_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # Ke2 (castle loss all)
        start_square = 'e1'
        target_square = 'e2'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KING_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 4, False, castle_white_long=False, castle_white_short=False)
        board.undo_last_move()
        self.assertEqual(KING_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # 0-0 (castle loss all)
        start_square = 'e1'
        target_square = 'g1'
        move = (SQUARES[start_square], SQUARES[target_square], CASTLE_SHORT)
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KING_WHITE, board.get_by_name(target_square))
        self.assertEqual(ROOK_WHITE, board.get_by_name('f1'))
        self.assertEqual(EMPTY, board.get_by_name('h1'))
        self.assert_position(board, 24, 4, False, castle_white_long=False, castle_white_short=False)
        board.undo_last_move()
        self.assertEqual(KING_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assertEqual(EMPTY, board.get_by_name('f1'))
        self.assertEqual(ROOK_WHITE, board.get_by_name('h1'))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # g8Q+ (irreversible, promotion)
        start_square = 'g7'
        target_square = 'g8'
        move = (SQUARES[start_square], SQUARES[target_square], PROMOTION_QUEEN)
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(QUEEN_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(PAWN_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # gxh8N (irreversible, promotion+takes)
        start_square = 'g7'
        target_square = 'h8'
        move = (SQUARES[start_square], SQUARES[target_square], PROMOTION_KNIGHT, ROOK_BLACK)
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KNIGHT_WHITE, board.get_by_name(target_square))
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(PAWN_WHITE, board.get_by_name(start_square))
        self.assertEqual(ROOK_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

        # bxa6 e.p. (irreversible, en passant)
        start_square = 'b5'
        target_square = 'a6'
        move = (SQUARES[start_square], SQUARES[target_square], EN_PASSANT)
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(PAWN_WHITE, board.get_by_name(target_square))
        self.assertEqual(EMPTY, board.get_by_name('a5'))
        self.assert_position(board, 24, 0, False)
        board.undo_last_move()
        self.assertEqual(PAWN_WHITE, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assertEqual(PAWN_BLACK, board.get_by_name('a5'))
        self.assert_position(board, 24, 3, True, en_passant=True, en_passant_square='a6')

    def test_move_undo_4(self):
        """
        Test special moves for black.
        """
        # black to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R b KQkq - 3 24')

        # d5 (irreversible, en passant possible)
        start_square = 'd7'
        target_square = 'd5'
        move = (SQUARES[start_square], SQUARES[target_square], DOUBLE_PAWN_MOVE)
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(PAWN_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 0, True, en_passant=True, en_passant_square='d6')
        board.undo_last_move()
        self.assertEqual(PAWN_BLACK, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, False)

        # Rg8 (castle loss short)
        start_square = 'h8'
        target_square = 'g8'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(ROOK_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 4, True, castle_black_short=False)
        board.undo_last_move()
        self.assertEqual(ROOK_BLACK, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, False)

        # Kf7 (castle loss all)
        start_square = 'e8'
        target_square = 'f7'
        move = (SQUARES[start_square], SQUARES[target_square])
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KING_BLACK, board.get_by_name(target_square))
        self.assert_position(board, 25, 4, True, castle_black_short=False, castle_black_long=False)
        board.undo_last_move()
        self.assertEqual(KING_BLACK, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assert_position(board, 24, 3, False)

        # 0-0-0 (castle loss all)
        start_square = 'e8'
        target_square = 'c8'
        move = (SQUARES[start_square], SQUARES[target_square], CASTLE_LONG)
        board.move(move)
        self.assertEqual(EMPTY, board.get_by_name(start_square))
        self.assertEqual(KING_BLACK, board.get_by_name(target_square))
        self.assertEqual(EMPTY, board.get_by_name('a8'))
        self.assertEqual(ROOK_BLACK, board.get_by_name('d8'))
        self.assert_position(board, 25, 4, True, castle_black_short=False, castle_black_long=False)
        board.undo_last_move()
        self.assertEqual(KING_BLACK, board.get_by_name(start_square))
        self.assertEqual(EMPTY, board.get_by_name(target_square))
        self.assertEqual(ROOK_BLACK, board.get_by_name('a8'))
        self.assertEqual(EMPTY, board.get_by_name('d8'))
        self.assert_position(board, 24, 3, False)


class MoveGenerationTest(unittest.TestCase):
    def test_move_generation_1(self):
        possible_moves = [
            # rook a1
            (SQUARES['a1'], SQUARES['b1']),
            (SQUARES['a1'], SQUARES['c1']),
            (SQUARES['a1'], SQUARES['d1']),
            # king
            (SQUARES['e1'], SQUARES['d1']),
            (SQUARES['e1'], SQUARES['e2']),
            (SQUARES['e1'], SQUARES['f1']),
            (SQUARES['e1'], SQUARES['c1'], CASTLE_LONG),
            (SQUARES['e1'], SQUARES['g1'], CASTLE_SHORT),
            # rook h1
            (SQUARES['h1'], SQUARES['g1']),
            (SQUARES['h1'], SQUARES['f1']),
            (SQUARES['h1'], SQUARES['h2']),
            (SQUARES['h1'], SQUARES['h3']),
            (SQUARES['h1'], SQUARES['h4']),
            # knight f3
            (SQUARES['f3'], SQUARES['g1']),
            (SQUARES['f3'], SQUARES['h2']),
            (SQUARES['f3'], SQUARES['h4']),
            (SQUARES['f3'], SQUARES['g5']),
            (SQUARES['f3'], SQUARES['d4'], QUEEN_BLACK),
            # bishop b3
            (SQUARES['b3'], SQUARES['c4']),
            (SQUARES['b3'], SQUARES['d5']),
            (SQUARES['b3'], SQUARES['e6'], PAWN_BLACK),
            (SQUARES['b3'], SQUARES['a4'], KNIGHT_BLACK),
            # queen
            (SQUARES['c2'], SQUARES['b1']),
            (SQUARES['c2'], SQUARES['c1']),
            (SQUARES['c2'], SQUARES['d1']),
            (SQUARES['c2'], SQUARES['b2']),
            (SQUARES['c2'], SQUARES['c3']),
            (SQUARES['c2'], SQUARES['d3']),
            (SQUARES['c2'], SQUARES['c4']),
            (SQUARES['c2'], SQUARES['c5']),
            (SQUARES['c2'], SQUARES['c6'], PAWN_BLACK),
            # pawns
            (SQUARES['a2'], SQUARES['a3']),
            (SQUARES['b5'], SQUARES['c6'], PAWN_BLACK),
            (SQUARES['b5'], SQUARES['a6'], EN_PASSANT),
            (SQUARES['d2'], SQUARES['d3']),
            (SQUARES['e4'], SQUARES['f5'], PAWN_BLACK),
            (SQUARES['g2'], SQUARES['g3']),
            (SQUARES['g2'], SQUARES['g4'], DOUBLE_PAWN_MOVE),
            (SQUARES['g7'], SQUARES['g8'], PROMOTION_QUEEN),
            (SQUARES['g7'], SQUARES['g8'], PROMOTION_ROOK),
            (SQUARES['g7'], SQUARES['g8'], PROMOTION_KNIGHT),
            (SQUARES['g7'], SQUARES['g8'], PROMOTION_BISHOP),
            (SQUARES['g7'], SQUARES['h8'], PROMOTION_QUEEN, ROOK_BLACK),
            (SQUARES['g7'], SQUARES['h8'], PROMOTION_ROOK, ROOK_BLACK),
            (SQUARES['g7'], SQUARES['h8'], PROMOTION_KNIGHT, ROOK_BLACK),
            (SQUARES['g7'], SQUARES['h8'], PROMOTION_BISHOP, ROOK_BLACK),
            (SQUARES['h5'], SQUARES['g6'], KNIGHT_BLACK),
            (SQUARES['h5'], SQUARES['h6']),
        ]
        # white to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 3 24')
        generated_moves = board.generate_moves()

        # compare generated moves to possible moves
        self.assertEqual(len(possible_moves), len(generated_moves), 'The number of generated moves is wrong!')
        for move in generated_moves:
            self.assertTrue(move in possible_moves)

    def test_move_generation_2(self):
        possible_moves = [
            # rook a8
            (SQUARES['a8'], SQUARES['a7']),
            (SQUARES['a8'], SQUARES['a6']),
            (SQUARES['a8'], SQUARES['b8']),
            (SQUARES['a8'], SQUARES['c8']),
            (SQUARES['a8'], SQUARES['d8']),
            # king
            (SQUARES['e8'], SQUARES['d8']),
            (SQUARES['e8'], SQUARES['e7']),
            (SQUARES['e8'], SQUARES['f7']),
            (SQUARES['e8'], SQUARES['c8'], CASTLE_LONG),
            # rook h8
            (SQUARES['h8'], SQUARES['g8']),
            (SQUARES['h8'], SQUARES['f8']),
            (SQUARES['h8'], SQUARES['h7']),
            (SQUARES['h8'], SQUARES['h6']),
            (SQUARES['h8'], SQUARES['h5'], PAWN_WHITE),
            # bishop c7
            (SQUARES['c7'], SQUARES['b8']),
            (SQUARES['c7'], SQUARES['d8']),
            (SQUARES['c7'], SQUARES['d6']),
            (SQUARES['c7'], SQUARES['e5'], PAWN_WHITE),
            # knight g6
            (SQUARES['g6'], SQUARES['f8']),
            (SQUARES['g6'], SQUARES['e7']),
            (SQUARES['g6'], SQUARES['e5'], PAWN_WHITE),
            (SQUARES['g6'], SQUARES['f4']),
            (SQUARES['g6'], SQUARES['h4']),
            # knight a4
            (SQUARES['a4'], SQUARES['b2']),
            (SQUARES['a4'], SQUARES['c3']),
            (SQUARES['a4'], SQUARES['c5']),
            # queen
            (SQUARES['d4'], SQUARES['c3']),
            (SQUARES['d4'], SQUARES['b2']),
            (SQUARES['d4'], SQUARES['a1'], ROOK_WHITE),
            (SQUARES['d4'], SQUARES['d3']),
            (SQUARES['d4'], SQUARES['d2'], PAWN_WHITE),
            (SQUARES['d4'], SQUARES['e3']),
            (SQUARES['d4'], SQUARES['f2'], PAWN_WHITE),
            (SQUARES['d4'], SQUARES['e4'], PAWN_WHITE),
            (SQUARES['d4'], SQUARES['e5'], PAWN_WHITE),
            (SQUARES['d4'], SQUARES['d5']),
            (SQUARES['d4'], SQUARES['d6']),
            (SQUARES['d4'], SQUARES['c5']),
            (SQUARES['d4'], SQUARES['c4']),
            (SQUARES['d4'], SQUARES['b4']),
            # pawns
            (SQUARES['c6'], SQUARES['b5'], PAWN_WHITE),
            (SQUARES['c6'], SQUARES['c5']),
            (SQUARES['d7'], SQUARES['d5'], DOUBLE_PAWN_MOVE),
            (SQUARES['d7'], SQUARES['d6']),
            (SQUARES['f5'], SQUARES['f4']),
            (SQUARES['f5'], SQUARES['e4'], PAWN_WHITE),
        ]
        # black to move
        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R b KQkq - 3 24')
        generated_moves = board.generate_moves()

        # compare generated moves to possible moves
        self.assertEqual(len(possible_moves), len(generated_moves), 'The number of generated moves is wrong!')
        for move in generated_moves:
            self.assertTrue(move in possible_moves)

    def test_is_attacked_1(self):
        attacked = {
            'white': [False, True, True, True, True, True, True, False,
                      True, True, True, True, True, True, False, True,
                      False, True, True, True, True, True, True, True,
                      True, False, True, True, True, False, False, True,
                      False, False, True, True, True, True, True, True,
                      True, False, True, True, True, True, True, False,
                      False, False, False, False, False, False, False, False,
                      False, False, False, False, False, True, False, True],
            'black': [True, False, False, False, False, False, False, False,
                      False, True, False, True, False, True, False, False,
                      False, False, True, True, True, False, False, False,
                      True, True, True, False, True, True, True, True,
                      True, True, True, True, True, True, False, True,
                      True, True, True, True, True, False, False, True,
                      True, False, False, True, True, True, False, True,
                      False, True, True, True, True, True, True, True],
        }

        board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R b KQkq - 3 24')
        for i in range(64):
            self.assertEqual(attacked['white'][i], board.is_attacked_by_white(i),
                             'The attacked value is not correct for the square ' + str(i) + '/' +
                             chessboard.translate_index_into_field(i))
            self.assertEqual(attacked['black'][i], board.is_attacked_by_black(i),
                             'The attacked value is not correct for the square ' + str(i) + '/' +
                             chessboard.translate_index_into_field(i))

    def test_is_in_check_1(self):
        # white in check
        positions_in_check = [
            # queen
            'r1b2r2/pp3kp1/4p2p/2Q3q1/2BPp3/2P3P1/PP4P1/2KR3R w - - 8 19',  # queen (diagonal distance)
            'r1b2rk1/ppN1pNb1/3pP1p1/5p2/2q3n1/7Q/PPnB1PP1/R4K1R w - - 0 21',  # queen (diagonal, distance)
            # rook
            '6k1/p4p1p/1pB3p1/8/P4PP1/2P5/5r1K/1R6 w - - 0 27',  # rook (horizontal, small distance)
            '8/p3Rpkp/1p4p1/3B4/2P2PP1/r5K1/8/8 w - - 2 33',  # rook (horizontal, distance)
            '8/p5k1/1p3RB1/6Pp/2P2P2/6K1/8/6r1 w - - 3 40',  # rook (vertical, small distance)
            # bishop
            'r1bqk2r/pppp1ppp/5n2/1Bb1n3/4PP2/8/PPPP2PP/RNBQ1RK1 w kq - 0 6',  # bishop (distance)
            '3qnrk1/4pp1p/r5p1/3N4/3bP3/5B1P/1P4P1/1RQ2RK1 w - - 1 22',  # bishop (distance)
            '2kr3r/pp3pp1/2p3q1/8/2BnPP2/4B1Pb/PPPN2K1/R2Q1R2 w k - 0 6',  # bishop (next to)
            # knight
            '8/6b1/5k1p/2n3pP/4K1P1/5PN1/8/8 w - - 11 49',  # knight
            'r1b2rk1/ppN1pNb1/2qpP1p1/5p2/2B3n1/7Q/PPnB1PP1/R3K2R w KQ - 12 20',  # knight
            '3r2k1/pp3p1p/2p3p1/8/5BP1/2P3P1/P3nPB1/5RK1 w - - 0 22',  # knight
            # pawn
            '8/5k2/5b1p/3p2pP/4pnP1/1NN2K2/5P2/8 w - - 0 41',  # pawn
        ]
        # test the positions
        for position in positions_in_check:
            self.assertTrue(chessboard.create_from_fen(position).is_white_king_in_check())

    def test_is_in_check_2(self):
        # black in check
        positions_in_check = [
            # queen
            'r1b1k2r/pp4p1/4pq1p/7Q/3Pp3/2P3P1/PP4P1/R3KB1R b KQkq - 1 15',  # queen (diagonal distance)
            'r1b2r2/pp2k1p1/4pq1p/2Q5/3Pp3/2P3P1/PP4P1/2KR1B1R b - - 5 17',  # queen (diagonal distance)
            'Q5k1/2r1bp1p/1q4p1/1P6/8/5B1P/6P1/1R5K b - - 4 34',  # queen (horizontal distance)
            '2k3Q1/R7/8/8/1pB2P2/6K1/8/8 b - - 0 49',  # queen (horizontal distance)
            'r1b3k1/ppN1p1bQ/3pPrp1/5p2/2q5/8/PPn2PP1/R5KR b - - 1 24',  # queen (diagonal, next to)
            # rook
            '5Rk1/r1p3pp/2Rp1p2/3P4/8/p1Nn4/5PPP/6K1 b - - 0 38',  # rook (next to)
            '8/6p1/4kp1p/7P/3p1KP1/1r3P2/4R3/8 b - - 7 54',  # rook (vertical, distance)
            '8/8/1R6/7P/4K1P1/2r2P2/1k6/8 b - - 4 65',  # rook (vertical, distance)
            # bishop
            'r2qk2r/1np1bppp/p2p4/3Pn3/B5b1/2N2N2/1P3PPP/R1BQR1K1 b kq - 2 16',  # bishop (diagonal distance)
            '6k1/R4B2/8/6P1/1pr2P2/6K1/8/8 b - - 1 45',  # bishop (next to)
            # knight
            '8/4b3/4k2p/6pP/3NKnP1/5P2/8/8 b - - 2 44',  # knight
            '3R4/1bp2q1k/r5pP/np2p1N1/p3Pn2/P1P1Q2P/1P3P2/1K4R1 b - - 3 27',  # knight
            # pawn
            '8/3k2pp/2Pp1p2/1r6/6PP/8/3R1P2/6K1 b - - 0 46',  # pawn
            '8/8/1p2k3/1P1P1rp1/2P1K1R1/8/8/8 b - - 0 69',  # pawn
        ]
        # test the positions
        for position in positions_in_check:
            self.assertTrue(chessboard.create_from_fen(position).is_black_king_in_check())

    def test_is_not_in_check_1(self):
        # white not in check
        positions_not_in_check = [
            # black in check
            'r1b1k2r/pp4p1/4pq1p/7Q/3Pp3/2P3P1/PP4P1/R3KB1R b KQkq - 1 15',  # queen (diagonal distance)
            '8/6p1/4kp1p/7P/3p1KP1/1r3P2/4R3/8 b - - 7 54',  # rook (vertical, distance)
            'r2qk2r/1np1bppp/p2p4/3Pn3/B5b1/2N2N2/1P3PPP/R1BQR1K1 b kq - 2 16',  # bishop (diagonal distance)
            '8/4b3/4k2p/6pP/3NKnP1/5P2/8/8 b - - 2 44',  # knight
            '8/8/1p2k3/1P1P1rp1/2P1K1R1/8/8/8 b - - 0 69',  # pawn
            # both not in check
            '2n4r/p2k1pbp/2p1b1p1/4p1B1/4P3/N7/PP2BPPP/R5K1 w - - 3 18',
            '4R3/p4pk1/2p2r1p/2Nn3q/1P3Pb1/P3P1P1/3QP1p1/R5K1 b - - 0 30',
            '4r1k1/1p4q1/p1b3Q1/8/4p3/1P2N1P1/P5P1/4R1K1 w - - 3 36',
            'q4rk1/p1p2pp1/4p1Pp/3bP1N1/3PN3/8/3Q1PP1/4R1K1 b - - 0 27',
            'r1b1kb1r/5ppp/p1pQ2n1/4p3/4P3/5N2/PP3PPP/RNB1K2R b KQkq - 0 11',
            '3R4/5b2/5pk1/7p/2PN3K/PP1r4/8/8 b - - 4 58',
            'r1b2rk1/1pp2pq1/p2p3p/6p1/PPBbP1n1/R5NP/4RPP1/2B1Q1K1 b - - 0 19',
            'r2q1r2/1Rb1n2k/2ppbp1p/2p1p1p1/2P1P3/3PB1NP/P3RPPN/3Q2K1 b - - 6 29',
        ]

        for position in positions_not_in_check:
            self.assertFalse(chessboard.create_from_fen(position).is_white_king_in_check())

    def test_is_not_in_check_2(self):
        # black not in check
        positions_not_in_check = [
            # white in check
            'r1b2rk1/ppN1pNb1/3pP1p1/5p2/2q3n1/7Q/PPnB1PP1/R4K1R w - - 0 21',  # queen (diagonal, distance)
            '8/p5k1/1p3RB1/6Pp/2P2P2/6K1/8/6r1 w - - 3 40',  # rook (vertical, small distance)
            'r1bqk2r/pppp1ppp/5n2/1Bb1n3/4PP2/8/PPPP2PP/RNBQ1RK1 w kq - 0 6',  # bishop (distance)
            'r1b2rk1/ppN1pNb1/2qpP1p1/5p2/2B3n1/7Q/PPnB1PP1/R3K2R w KQ - 12 20',  # knight
            '8/5k2/5b1p/3p2pP/4pnP1/1NN2K2/5P2/8 w - - 0 41',  # pawn
            # both not in check
            '2n4r/p2k1pbp/2p1b1p1/4p1B1/4P3/N7/PP2BPPP/R5K1 w - - 3 18',
            '4R3/p4pk1/2p2r1p/2Nn3q/1P3Pb1/P3P1P1/3QP1p1/R5K1 b - - 0 30',
            '4r1k1/1p4q1/p1b3Q1/8/4p3/1P2N1P1/P5P1/4R1K1 w - - 3 36',
            'q4rk1/p1p2pp1/4p1Pp/3bP1N1/3PN3/8/3Q1PP1/4R1K1 b - - 0 27',
            'r1b1kb1r/5ppp/p1pQ2n1/4p3/4P3/5N2/PP3PPP/RNB1K2R b KQkq - 0 11',
            '3R4/5b2/5pk1/7p/2PN3K/PP1r4/8/8 b - - 4 58',
            'r1b2rk1/1pp2pq1/p2p3p/6p1/PPBbP1n1/R5NP/4RPP1/2B1Q1K1 b - - 0 19',
            'r2q1r2/1Rb1n2k/2ppbp1p/2p1p1p1/2P1P3/3PB1NP/P3RPPN/3Q2K1 b - - 6 29',
        ]

        for position in positions_not_in_check:
            self.assertFalse(chessboard.create_from_fen(position).is_black_king_in_check())


class CheckmateTest(unittest.TestCase):

    def test_checkmate_1(self):
        board = chessboard.create_from_fen('8/8/8/6K1/8/3Q4/8/1Rk5 b - - 48 5')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_2(self):
        board = chessboard.create_from_fen('3R2k1/b4ppp/8/8/8/8/2r1BPPP/6K1 b - - 36 6')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_3(self):
        board = chessboard.create_from_fen('r6k/3R2Qp/8/2p5/qp1n1P2/8/PPP5/1K3R2 b - - 0 28')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_4(self):
        board = chessboard.create_from_fen('2K5/p1q5/1p2n3/PP6/8/5k2/8/8 w - - 1 46')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_5(self):
        board = chessboard.create_from_fen('8/R7/8/Q2pPp2/k2P1P2/1p6/PP4P1/6K1 b - - 0 47')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_6(self):
        board = chessboard.create_from_fen('8/1p2R3/p1p1Q2p/5kpq/3P1p2/5b2/PP1B1PPP/R5K1 b - - 6 31')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_7(self):
        board = chessboard.create_from_fen('5r2/8/P5R1/2p2Nkp/2b3pN/6P1/4PP2/6K1 b - - 0 42')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_8(self):
        board = chessboard.create_from_fen('rkr5/pppNbq1p/2n5/6B1/3p4/8/PPP2PPP/R5K1 b - - 1 24')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    def test_checkmate_9(self):
        board = chessboard.create_from_fen('2r1n1r1/p3qp1k/1p2p1p1/nP1b3R/8/P2B4/1BP2PPP/3R2K1 b - - 11 25')
        self.assertTrue(board.is_checkmate())
        self.assertFalse(board.is_stalemate())

    # TODO add checkmate tests: no checkmate


if __name__ == '__main__':
    unittest.main()
