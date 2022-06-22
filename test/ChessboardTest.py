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

    # TODO add more extensive tests of special moves


if __name__ == '__main__':
    unittest.main()
