EMPTY = 0
KING_WHITE = 1
QUEEN_WHITE = 2
BISHOP_WHITE = 3
KNIGHT_WHITE = 4
ROOK_WHITE = 5
PAWN_WHITE = 6
KING_BLACK = 7
QUEEN_BLACK = 8
BISHOP_BLACK = 9
KNIGHT_BLACK = 10
ROOK_BLACK = 11
PAWN_BLACK = 12
translation_from_fen = {
    'K': KING_WHITE,
    'Q': QUEEN_WHITE,
    'B': BISHOP_WHITE,
    'N': KNIGHT_WHITE,
    'R': ROOK_WHITE,
    'P': PAWN_WHITE,
    'k': KING_BLACK,
    'q': QUEEN_BLACK,
    'b': BISHOP_BLACK,
    'n': KNIGHT_BLACK,
    'r': ROOK_BLACK,
    'p': PAWN_BLACK,
}
translation_to_fen = {
    KING_WHITE: 'K',
    QUEEN_WHITE: 'Q',
    BISHOP_WHITE: 'B',
    KNIGHT_WHITE: 'N',
    ROOK_WHITE: 'R',
    PAWN_WHITE: 'P',
    KING_BLACK: 'k',
    QUEEN_BLACK: 'q',
    BISHOP_BLACK: 'b',
    KNIGHT_BLACK: 'n',
    ROOK_BLACK: 'r',
    PAWN_BLACK: 'p',
}
SQUARES = {
    'a1': 0,
    'b1': 1,
    'c1': 2,
    'd1': 3,
    'e1': 4,
    'f1': 5,
    'g1': 6,
    'h1': 7,
    'a2': 8,
    'b2': 9,
    'c2': 10,
    'd2': 11,
    'e2': 12,
    'f2': 13,
    'g2': 14,
    'h2': 15,
    'a7': 48,
    'b7': 49,
    'c7': 50,
    'd7': 51,
    'e7': 52,
    'f7': 53,
    'g7': 54,
    'h7': 55,
    'a8': 56,
    'b8': 57,
    'c8': 58,
    'd8': 59,
    'e8': 60,
    'f8': 61,
    'g8': 62,
    'h8': 63
}
# special moves
CASTLE_SHORT = -1
CASTLE_LONG = -2
PROMOTION_QUEEN = -9
PROMOTION_ROOK = -5
PROMOTION_BISHOP = -4
PROMOTION_KNIGHT = -3
DOUBLE_PAWN_MOVE = -10
EN_PASSANT = -11


class Chessboard:
    """
    This class represents a chessboard with its position and some additional data like castle rights.
    It can make, undo and generate all legal moves.
    """

    def __init__(self, board: list, turn: str, castle: dict, en_passant: bool, en_passant_field: int, move_number: int,
                 draw_counter: int) -> None:
        """
        Creates a new chessboard with all basic data.
        :param board: The list of squares.
        :param turn: Which player has to make a move next.
        :param castle: The castle rights of both players.
        :param en_passant: If there is an en passant in the position.
        :param en_passant_field: The field of the en passant.
        :param move_number: The current move number.
        :param draw_counter: The counter of moves for the 50 move rule.
        """
        # initialize board
        self.board = board
        self.turn = turn
        self.castle = castle
        self.move_number_castle_loss_short_white = 0
        self.move_number_castle_loss_long_white = 0
        self.move_number_castle_loss_short_black = 0
        self.move_number_castle_loss_long_black = 0
        self.en_passant = en_passant
        self.en_passant_square = en_passant_field
        self.half_move_count_for_draw = draw_counter
        self.move_number = move_number
        self.moves = []  # the list of moves that were made
        # this list needs to keep track of all previous half move counters for undoing moves
        self.half_move_counters = []

    def is_empty(self, field: int) -> bool:
        """
        Checks if a field is empty.
        :param field: The field.
        :return: If the field is empty.
        """
        return self.board[field] == EMPTY

    def is_white_piece(self, field: int) -> bool:
        """
        Checks if a white piece is on the specified field.
        :param field: The field.
        :return: If a white piece is on the field.
        """
        return 0 < self.board[field] <= 6

    def is_black_piece(self, field: int) -> bool:
        """
        Checks if a black piece is on the specified field.
        :param field: The field.
        :return: If a black piece is on the field.
        """
        return 6 < self.board[field] <= 12

    def is_same_colour(self, field1: int, field2: int):
        """
        Checks if both fields have a piece of the same colour.
        :param field1: The index of the first field.
        :param field2: The index of the second field.
        :return: If both fields have pieces of the same colour. If one field is empty False is returned.
        """
        if self.is_white_piece(field1) and self.is_white_piece(field2):
            return True
        if self.is_black_piece(field1) and self.is_black_piece(field2):
            return True
        return False

    def move(self, move: tuple):
        """
        Moves a piece according to the specified move.
        :param move: The tuple describing the move.
        """
        if len(move) < 2:
            return

        start_square = move[0]
        target_square = move[1]

        if self.is_empty(start_square):
            return
        if self.is_white_piece(start_square) and self.turn == 'black':
            return
        if self.is_black_piece(start_square) and self.turn == 'white':
            return

        # execute move
        self.board[target_square] = self.board[start_square]
        self.board[start_square] = EMPTY
        # set en passant as not possible
        self.en_passant = False
        # if it was a special move, additional steps must be taken (promotion, en passant, castle)
        if len(move) > 3:  # castle, en passant, takes, promotion and takes+promotion
            # reset draw counter (all special irreversible moves)
            self.half_move_counters.append(self.half_move_count_for_draw)
            self.half_move_count_for_draw = 0

            additional_move_info = move[2]
            if additional_move_info == EN_PASSANT:
                # remove en passant pawn
                if self.turn == 'white':
                    self.board[target_square - 8] = EMPTY
                else:
                    self.board[target_square + 8] = EMPTY
            elif additional_move_info == DOUBLE_PAWN_MOVE:
                # set en passant square
                self.en_passant = True
                self.en_passant_square = int((start_square + target_square) / 2)
            elif additional_move_info == CASTLE_SHORT:
                # move the rook
                if self.turn == 'white':
                    self.board[SQUARES['h1']] = EMPTY
                    self.board[SQUARES['f1']] = ROOK_WHITE
                else:
                    self.board[SQUARES['h8']] = EMPTY
                    self.board[SQUARES['f8']] = ROOK_WHITE
            elif additional_move_info == CASTLE_LONG:
                # move the rook
                if self.turn == 'white':
                    self.board[SQUARES['a1']] = EMPTY
                    self.board[SQUARES['d1']] = ROOK_WHITE
                else:
                    self.board[SQUARES['a8']] = EMPTY
                    self.board[SQUARES['d8']] = ROOK_WHITE
            elif additional_move_info == PROMOTION_QUEEN or additional_move_info == PROMOTION_ROOK or \
                    additional_move_info == PROMOTION_KNIGHT or additional_move_info == PROMOTION_BISHOP:
                # promote the pawn
                self.promote(target_square, additional_move_info)
        else:
            # pawn moves
            if self.board[target_square] == PAWN_WHITE or self.board[target_square] == PAWN_BLACK:
                # reset draw counter
                self.half_move_counters.append(self.half_move_count_for_draw)
                self.half_move_count_for_draw = 0
            # all other moves
            else:
                self.half_move_count_for_draw += 1
        # update castle rights
        if self.board[target_square] == KING_WHITE or self.board[target_square] == KING_BLACK:
            if self.castle[self.turn]['short']:
                self.castle[self.turn]['short'] = False  # remove castle right
                if self.turn == 'white':
                    self.move_number_castle_loss_short_white = self.move_number
                else:
                    self.move_number_castle_loss_short_black = self.move_number
            if self.castle[self.turn]['long']:
                self.castle[self.turn]['long'] = False  # remove castle right
                if self.turn == 'white':
                    self.move_number_castle_loss_long_white = self.move_number
                else:
                    self.move_number_castle_loss_long_black = self.move_number
        if self.board[target_square] == ROOK_WHITE or self.board[target_square] == ROOK_BLACK:
            if self.castle[self.turn]['short']:
                if self.turn == 'white' and start_square == SQUARES['h1']:
                    self.castle[self.turn]['short'] = False  # remove castle right
                    self.move_number_castle_loss_short_white = self.move_number
                elif self.turn == 'black' and start_square == SQUARES['h8']:
                    self.castle[self.turn]['short'] = False  # remove castle right
                    self.move_number_castle_loss_short_black = self.move_number
            if self.castle[self.turn]['long']:
                if self.turn == 'white' and start_square == SQUARES['a1']:
                    self.castle[self.turn]['long'] = False  # remove castle right
                    self.move_number_castle_loss_long_white = self.move_number
                elif self.turn == 'black' and start_square == SQUARES['a8']:
                    self.castle[self.turn]['long'] = False  # remove castle right
                    self.move_number_castle_loss_long_black = self.move_number

        # add the move to the list of executed moves
        self.moves.append(move)
        # increase move counter
        if self.turn == 'black':
            move += 1
        # switch turn
        self.switch_turn()

    def undo_last_move(self):
        """
        Reverses the last move that has been made.
        """
        # get and remove the last move from the list
        move = self.moves.pop()
        # decrease move counter
        if self.turn == 'white':
            move -= 1
        # decrease half move counter for draw (50 move rule)
        if self.half_move_count_for_draw > 0:
            self.half_move_count_for_draw -= 1
        else:
            # if it is at 0, the last one is loaded
            self.half_move_count_for_draw = self.half_move_counters.pop()
        # switch turn
        self.switch_turn()
        # update castle rights
        if self.turn == 'white':
            if self.move_number < self.move_number_castle_loss_short_white:
                self.move_number_castle_loss_short_white = 0
                self.castle[self.turn] = True
            if self.move_number < self.move_number_castle_loss_long_white:
                self.move_number_castle_loss_long_white = 0
                self.castle[self.turn] = True
        if self.turn == 'black':
            if self.move_number < self.move_number_castle_loss_short_black:
                self.move_number_castle_loss_short_black = 0
                self.castle[self.turn] = True
            if self.move_number < self.move_number_castle_loss_long_black:
                self.move_number_castle_loss_long_black = 0
                self.castle[self.turn] = True

        if len(move) < 2:
            return
        start_square = move[0]
        target_square = move[1]

        if self.is_empty(target_square):
            return
        if self.is_white_piece(target_square) and self.turn == 'black':
            return
        if self.is_black_piece(target_square) and self.turn == 'white':
            return

        # undo the move
        self.board[start_square] = self.board[target_square]
        self.board[target_square] = EMPTY
        # if it was a special move, additional steps must be taken (promotion, en passant, castle)
        if len(move) == 3:  # castle, en passant, takes, promotion and takes+promotion
            additional_move_info = move[2]
            if additional_move_info == DOUBLE_PAWN_MOVE:
                pass  # do nothing, is excluded for capture check at the end
            elif additional_move_info == EN_PASSANT:
                # restore en passant pawn
                if self.turn == 'white':
                    self.board[target_square - 8] = PAWN_BLACK
                else:
                    self.board[target_square + 8] = PAWN_WHITE
            elif additional_move_info == CASTLE_SHORT:
                # undo the rook move
                if self.turn == 'white':
                    self.board[SQUARES['h1']] = ROOK_WHITE
                    self.board[SQUARES['f1']] = EMPTY
                else:
                    self.board[SQUARES['h8']] = ROOK_BLACK
                    self.board[SQUARES['f8']] = EMPTY
            elif additional_move_info == CASTLE_LONG:
                # undo the rook move
                if self.turn == 'white':
                    self.board[SQUARES['a1']] = ROOK_WHITE
                    self.board[SQUARES['d1']] = EMPTY
                else:
                    self.board[SQUARES['a8']] = ROOK_BLACK
                    self.board[SQUARES['d8']] = EMPTY
            elif additional_move_info == PROMOTION_QUEEN or additional_move_info == PROMOTION_ROOK or \
                    additional_move_info == PROMOTION_KNIGHT or additional_move_info == PROMOTION_BISHOP:
                # undo promotion
                if self.turn == 'white':
                    self.board[start_square] = PAWN_WHITE
                else:
                    self.board[start_square] = PAWN_BLACK
            else:  # takes
                # undo takes
                self.board[target_square] = additional_move_info
        elif len(move) == 4:  # takes+promotion
            # undo promotion
            if self.turn == 'white':
                self.board[start_square] = PAWN_WHITE
            else:
                self.board[start_square] = PAWN_BLACK
            # undo takes
            self.board[target_square] = move[3]

        if len(self.moves) > 0:
            # if the last move was a double pawn move, set en passant
            previous_move = self.moves[-1]
            if len(previous_move) == 3 and previous_move[2] == DOUBLE_PAWN_MOVE:
                self.en_passant = True
                self.en_passant_square = int((previous_move[0] + previous_move[1]) / 2)

    def promote(self, target_square: int, piece: int):
        """
        Promotes a pawn on the target square to the specified piece.
        If the square is not on the back rank or has no pawn, nothing happens.
        :param target_square: The square of the promotion.
        :param piece: The promotion constant that specifies the piece.
        """
        if self.turn == 'white':
            if target_square < SQUARES['a8'] or not self.has_piece(target_square, PAWN_WHITE):
                return

            if piece == PROMOTION_QUEEN:
                self.board[target_square] = QUEEN_WHITE
            elif piece == PROMOTION_KNIGHT:
                self.board[target_square] = KNIGHT_WHITE
            elif piece == PROMOTION_ROOK:
                self.board[target_square] = ROOK_WHITE
            elif piece == PROMOTION_BISHOP:
                self.board[target_square] = BISHOP_WHITE
        else:
            if target_square > SQUARES['h1'] or not self.has_piece(target_square, PAWN_BLACK):
                return

            if piece == PROMOTION_QUEEN:
                self.board[target_square] = QUEEN_BLACK
            elif piece == PROMOTION_KNIGHT:
                self.board[target_square] = KNIGHT_BLACK
            elif piece == PROMOTION_ROOK:
                self.board[target_square] = ROOK_BLACK
            elif piece == PROMOTION_BISHOP:
                self.board[target_square] = BISHOP_BLACK

    def generate_moves(self) -> list:
        """
        Generates a list of all legal moves in this position.
        The moves are stored as tuples in the following form:
            - Basic moves: (start_square, target_square)
        More complex moves have additional data:
            - Takes: (start_square, target_square, taken_piece)
            - Promotion: (start_square, target_square, promoted_piece)
            - Takes+Promotion: (start_square, target_square, promoted_piece, taken_piece)
            - Castle: (start_square_of_king, target_square_of_king, castle_indicator)
            - Double pawn move: (start_square, target_square, double_move_indicator)
            - En passant: (start_square, target_square, en_passant_indicator)
        :return: The list of legal moves.
        """
        moves = []  # list of tuples with from-square and to-square. Special moves have the move type in third place.

        for square in range(64):
            if self.is_empty(square):
                continue
            if self.turn == 'white' and self.is_white_piece(square):
                if self.has_piece(square, KING_WHITE):
                    moves.extend(self.get_king_moves(square))
                elif self.has_piece(square, QUEEN_WHITE):
                    moves.extend(self.get_queen_moves(square))
                elif self.has_piece(square, ROOK_WHITE):
                    moves.extend(self.get_rook_moves(square))
                elif self.has_piece(square, BISHOP_WHITE):
                    moves.extend(self.get_bishop_moves(square))
                elif self.has_piece(square, KNIGHT_WHITE):
                    moves.extend(self.get_knight_moves(square))
                else:
                    moves.extend(self.get_pawn_moves(square))
            elif self.turn == 'black' and self.is_black_piece(square):
                if self.has_piece(square, KING_BLACK):
                    moves.extend(self.get_king_moves(square))
                elif self.has_piece(square, QUEEN_BLACK):
                    moves.extend(self.get_queen_moves(square))
                elif self.has_piece(square, ROOK_BLACK):
                    moves.extend(self.get_rook_moves(square))
                elif self.has_piece(square, BISHOP_BLACK):
                    moves.extend(self.get_bishop_moves(square))
                elif self.has_piece(square, KNIGHT_BLACK):
                    moves.extend(self.get_knight_moves(square))
                else:
                    moves.extend(self.get_pawn_moves(square))

        # exclude moves where the king would be in check (or moved through check)
        legal_moves = []
        for move in moves:
            self.move(move)
            # check for legality
            # since a move was made it is the other player's turn
            if self.turn == 'black' and self.is_white_king_in_check():
                self.undo_last_move()
                continue
            elif self.turn == 'white' and self.is_black_king_in_check():
                self.undo_last_move()
                continue
            else:
                legal_moves.append(move)
                self.undo_last_move()
        return legal_moves

    def is_white_king_in_check(self) -> bool:
        """
        Checks if the white king is attacked.
        :return: If the white king is in check.
        """
        # search for king
        for square in range(64):
            if self.has_piece(square, KING_WHITE):
                # check if king is attacked
                return self.is_attacked_by_black(square)

    def is_black_king_in_check(self) -> bool:
        """
        Checks if the black king is attacked.
        :return: If the black king is in check.
        """
        # search for king
        for square in range(64):
            if self.has_piece(square, KING_BLACK):
                # check if king is attacked
                return self.is_attacked_by_white(square)

    def get_directional_moves(self, start_square: int, direction_x: int, direction_y: int, distance: int = 7) -> list:
        """
        Returns a list of moves that are in the specified direction vector.
        The moves are either basic moves or taking moves. The distance is the maximum number of times
        the direction vector can be added. If an enemy piece is reached, the taking move will be included. If a piece
        with the same colour is reached, the search for moves is stopped.
        :param start_square: The square from which the moves will be generated.
        :param direction_x: The x part of the direction vector.
        :param direction_y: The y part of the direction vector.
        :param distance: The maximum distance.
        :return: The list of moves.
        """
        is_white_piece = self.is_white_piece(start_square)
        moves = []  # list of tuples with from-square and to-square (and possibly taken piece).

        for i in range(1, distance + 1):
            target_square = start_square + i * direction_x + 8 * i * direction_y
            # check if the target field is still on the board
            if not is_field(target_square):
                return moves
            # check if the target field has not crossed the left/right border
            if direction_x < 0 and target_square % 8 > start_square % 8:
                return moves
            if direction_x > 0 and target_square % 8 < start_square % 8:
                return moves
            # check if a piece was reached. (capture or same colour)
            if not self.is_empty(target_square):
                if not self.is_same_colour(start_square, target_square):
                    # takes move
                    move = (start_square, target_square, self.board[target_square])
                    moves.append(move)
                # a piece was reached: stop searching
                return moves

            move = (start_square, target_square)
            moves.append(move)
        return moves

    def is_attacked_by_white(self, square: int) -> bool:
        """
        Checks if the specified square is attacked by white.
        :param square: The square that is checked.
        :return: If the square is attacked by white.
        """
        directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        knight_directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        # check all directions
        for x, y in directions:
            for distance in range(1, 8):
                target_square = square + distance * x + 8 * distance * y
                # check if the target square is still on the board or a black piece blocks a potential attack
                if not is_field(target_square) or self.is_black_piece(target_square):
                    break
                # check if the target square has crossed the left/right border
                if x < 0 and target_square % 8 > square % 8:
                    break
                if x > 0 and target_square % 8 < square % 8:
                    break

                # check if a piece was reached and the piece can take on the origin square
                # if not, the piece blocks other pieces from attacking (-> exit the distance loop)
                if self.has_piece(target_square, KING_WHITE):
                    if distance == 1:
                        return True
                    else:
                        break
                elif self.has_piece(target_square, QUEEN_WHITE):
                    return True
                elif self.has_piece(target_square, ROOK_WHITE):
                    if (x + y) % 2 == 1:  # only straight moves
                        return True
                    else:
                        break
                elif self.has_piece(target_square, BISHOP_WHITE):
                    if (x + y) % 2 == 0:  # only diagonal moves
                        return True
                    else:
                        break
                elif self.has_piece(target_square, PAWN_WHITE):
                    if distance == 1 and x != 0 and y == -1:  # viewpoint of the attacked field
                        return True
                    else:
                        break

        # check knight positions
        for x, y in knight_directions:
            target_square = square + x + 8 * y
            # check if the target field is still on the board
            if not is_field(target_square):
                continue
            # check if the target field has crossed the left/right border
            if x < 0 and target_square % 8 > square % 8:
                continue
            if x > 0 and target_square % 8 < square % 8:
                continue

            # check if a white knight was reached
            if self.has_piece(target_square, KNIGHT_WHITE):
                return True

        return False

    def is_attacked_by_black(self, square: int) -> bool:
        """
        Checks if the specified square is attacked by white.
        :param square: The square that is checked.
        :return: If the square is attacked by white.
        """
        directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        knight_directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        # check all directions
        for x, y in directions:
            for distance in range(1, 8):
                target_square = square + distance * x + 8 * distance * y
                # check if the target field is still on the board or a white piece blocks a potential attack
                if not is_field(target_square) or self.is_white_piece(target_square):
                    break
                # check if the target field has crossed the left/right border
                if x < 0 and target_square % 8 > square % 8:
                    break
                if x > 0 and target_square % 8 < square % 8:
                    break

                # check if a piece was reached and the piece can take on the origin square
                # if not, the piece blocks other pieces from attacking (-> exit the distance loop)
                if self.has_piece(target_square, KING_BLACK):
                    if distance == 1:
                        return True
                    else:
                        break
                elif self.has_piece(target_square, QUEEN_BLACK):
                    return True
                elif self.has_piece(target_square, ROOK_BLACK):
                    if (x + y) % 2 == 1:  # only straight moves
                        return True
                    else:
                        break
                elif self.has_piece(target_square, BISHOP_BLACK):
                    if (x + y) % 2 == 0:  # only diagonal moves
                        return True
                    else:
                        break
                elif self.has_piece(target_square, PAWN_BLACK):
                    if distance == 1 and x != 0 and y == 1:  # viewpoint of the attacked square
                        return True
                    else:
                        break

        # check knight positions
        for x, y in knight_directions:
            target_square = square + x + 8 * y
            # check if the target square is still on the board
            if not is_field(target_square):
                continue
            # check if the target square has crossed the left/right border
            if x < 0 and target_square % 8 > square % 8:
                continue
            if x > 0 and target_square % 8 < square % 8:
                continue

            # check if a black knight was reached
            if self.has_piece(target_square, KNIGHT_BLACK):
                return True

        return False

    def is_checkmate(self):
        if self.turn == 'white':
            for square in self.board:
                if self.has_piece(square, KING_WHITE):
                    if not self.is_attacked_by_black(square):
                        return False
                    else:
                        if len(self.generate_moves()) == 0:
                            return True
                        else:
                            return False
        else:
            for square in self.board:
                if self.has_piece(square, KING_BLACK):
                    if not self.is_attacked_by_white(square):
                        return False
                    else:
                        if len(self.generate_moves()) == 0:
                            return True
                        else:
                            return False

    def is_stalemate(self):
        if self.turn == 'white':
            for square in self.board:
                if self.has_piece(square, KING_WHITE):
                    if self.is_attacked_by_black(square):
                        return False
                    else:
                        if len(self.generate_moves()) == 0:
                            return True
                        else:
                            return False
        else:
            for square in self.board:
                if self.has_piece(square, KING_BLACK):
                    if self.is_attacked_by_white(square):
                        return False
                    else:
                        if len(self.generate_moves()) == 0:
                            return True
                        else:
                            return False
        return False

    def is_draw_move_count(self):
        return self.half_move_count_for_draw >= 100

    def is_draw_repetition(self):
        return False

    def is_draw(self):
        return self.is_draw_repetition() or self.is_stalemate() or self.is_draw_move_count()

    def get_diagonal_moves(self, field: int, distance: int = 7) -> list:
        moves = []
        moves.extend(self.get_directional_moves(field, -1, -1, distance))
        moves.extend(self.get_directional_moves(field, -1, 1, distance))
        moves.extend(self.get_directional_moves(field, 1, -1, distance))
        moves.extend(self.get_directional_moves(field, 1, 1, distance))
        return moves

    def get_straight_moves(self, field: int, distance: int = 7) -> list:
        moves = []
        moves.extend(self.get_directional_moves(field, 0, -1, distance))
        moves.extend(self.get_directional_moves(field, 0, 1, distance))
        moves.extend(self.get_directional_moves(field, -1, 0, distance))
        moves.extend(self.get_directional_moves(field, 1, 0, distance))
        return moves

    def get_king_moves(self, square: int) -> list:
        moves = []
        moves.extend(self.get_diagonal_moves(square, 1))
        moves.extend(self.get_straight_moves(square, 1))
        # check castle
        if self.has_piece(square, KING_WHITE) and square == SQUARES['e1']:
            if self.castle['white']['short'] and self.is_empty(SQUARES['f1']) and self.is_empty(SQUARES['g1']):
                moves.append((square, SQUARES['g1'], CASTLE_SHORT))
            if self.castle['white']['long'] and self.is_empty(SQUARES['b1']) and self.is_empty(SQUARES['c1']) \
                    and self.is_empty(SQUARES['d1']):
                moves.append((square, SQUARES['c1'], CASTLE_LONG))
        elif self.has_piece(square, KING_BLACK) and square == SQUARES['e8']:
            if self.castle['black']['short'] and self.is_empty(SQUARES['f8']) and self.is_empty(SQUARES['g8']):
                moves.append((square, SQUARES['g8'], CASTLE_SHORT))
            if self.castle['black']['long'] and self.is_empty(SQUARES['b8']) and self.is_empty(SQUARES['c8']) \
                    and self.is_empty(SQUARES['d8']):
                moves.append((square, SQUARES['c8'], CASTLE_LONG))
        return moves

    def get_queen_moves(self, square: int) -> list:
        moves = []
        moves.extend(self.get_diagonal_moves(square))
        moves.extend(self.get_straight_moves(square))
        return moves

    def get_rook_moves(self, square: int) -> list:
        return self.get_straight_moves(square)

    def get_bishop_moves(self, square: int) -> list:
        return self.get_diagonal_moves(square)

    def get_knight_moves(self, square: int) -> list:
        moves = []
        moves.extend(self.get_directional_moves(square, -2, -1, 1))
        moves.extend(self.get_directional_moves(square, -2, 1, 1))
        moves.extend(self.get_directional_moves(square, -1, 2, 1))
        moves.extend(self.get_directional_moves(square, -1, -2, 1))
        moves.extend(self.get_directional_moves(square, 1, -2, 1))
        moves.extend(self.get_directional_moves(square, 1, 2, 1))
        moves.extend(self.get_directional_moves(square, 2, -1, 1))
        moves.extend(self.get_directional_moves(square, 2, 1, 1))
        return moves

    def get_white_pawn_moves(self, square: int) -> list:
        if not self.has_piece(square, PAWN_WHITE):
            return []

        moves = []

        # forward
        if self.is_empty(square + 8):
            # promotion
            if square + 8 >= 8 * 7:
                moves.append((square, square + 8, PROMOTION_QUEEN))
                moves.append((square, square + 8, PROMOTION_ROOK))
                moves.append((square, square + 8, PROMOTION_BISHOP))
                moves.append((square, square + 8, PROMOTION_KNIGHT))
            else:
                moves.append((square, square + 8))
            # two squares forward
            if square < 16 and self.is_empty(square + 16):
                moves.append((square, square + 16, DOUBLE_PAWN_MOVE))
        # takes
        if self.is_black_piece(square + 7) and (square + 7) % 8 < square % 8:
            # promotion
            if square + 7 >= 8 * 7:
                moves.append((square, square + 7, PROMOTION_QUEEN, self.board[square + 7]))
                moves.append((square, square + 7, PROMOTION_ROOK, self.board[square + 7]))
                moves.append((square, square + 7, PROMOTION_BISHOP, self.board[square + 7]))
                moves.append((square, square + 7, PROMOTION_KNIGHT, self.board[square + 7]))
            else:
                moves.append((square, square + 7, self.board[square + 7]))
        if self.is_black_piece(square + 9) and (square + 9) % 8 > square % 8:
            # promotion
            if square + 9 >= 8 * 7:
                moves.append((square, square + 9, PROMOTION_QUEEN, self.board[square + 9]))
                moves.append((square, square + 9, PROMOTION_ROOK, self.board[square + 9]))
                moves.append((square, square + 9, PROMOTION_BISHOP, self.board[square + 9]))
                moves.append((square, square + 9, PROMOTION_KNIGHT, self.board[square + 9]))
            else:
                moves.append((square, square + 9, self.board[square + 9]))
        # en passant
        if self.en_passant:
            if self.en_passant_square == square + 7 and self.en_passant_square % 8 < square % 8:
                moves.append((square, self.en_passant_square, EN_PASSANT))
            elif self.en_passant_square == square + 9 and self.en_passant_square % 8 > square % 8:
                moves.append((square, self.en_passant_square, EN_PASSANT))
        return moves

    def get_black_pawn_moves(self, square: int) -> list:
        if not self.has_piece(square, PAWN_BLACK):
            return []

        moves = []

        # forward
        if self.is_empty(square - 8):
            # promotion
            if square - 8 < 8:
                moves.append((square, square - 8, PROMOTION_QUEEN))
                moves.append((square, square - 8, PROMOTION_ROOK))
                moves.append((square, square - 8, PROMOTION_BISHOP))
                moves.append((square, square - 8, PROMOTION_KNIGHT))
            else:
                moves.append((square, square - 8))
            # two squares forward
            if square >= 8 * 6 and self.is_empty(square - 16):
                moves.append((square, square - 16, DOUBLE_PAWN_MOVE))
        # takes
        if self.is_white_piece(square - 7) and (square - 7) % 8 > square % 8:
            # promotion
            if square - 7 < 8:
                moves.append((square, square - 7, PROMOTION_QUEEN, self.board[square - 7]))
                moves.append((square, square - 7, PROMOTION_ROOK, self.board[square - 7]))
                moves.append((square, square - 7, PROMOTION_BISHOP, self.board[square - 7]))
                moves.append((square, square - 7, PROMOTION_KNIGHT, self.board[square - 7]))
            else:
                moves.append((square, square - 7, self.board[square - 7]))
        if self.is_white_piece(square - 9) and (square - 9) % 8 < square % 8:
            # promotion
            if square - 9 >= 8 * 7:
                moves.append((square, square - 9, PROMOTION_QUEEN, self.board[square - 9]))
                moves.append((square, square - 9, PROMOTION_ROOK, self.board[square - 9]))
                moves.append((square, square - 9, PROMOTION_BISHOP, self.board[square - 9]))
                moves.append((square, square - 9, PROMOTION_KNIGHT, self.board[square - 9]))
            else:
                moves.append((square, square - 9, self.board[square - 9]))
        # en passant
        if self.en_passant:
            if self.en_passant_square == square - 7 and self.en_passant_square % 8 > square % 8:
                moves.append((square, self.en_passant_square, EN_PASSANT))
            elif self.en_passant_square == square - 9 and self.en_passant_square % 8 < square % 8:
                moves.append((square, self.en_passant_square, EN_PASSANT))
        return moves

    def get_pawn_moves(self, square: int) -> list:
        moves = []
        moves.extend(self.get_white_pawn_moves(square))
        moves.extend(self.get_black_pawn_moves(square))
        return moves

    def has_piece(self, square: int, piece: int):
        if 0 <= square <= 63:
            if self.board[square] == piece:
                return True
        return False

    def print(self) -> None:
        """
        Prints the board in a readable way.
        """
        # print the board
        print('+-----------------+')
        for y in range(7, -1, -1):
            row = '| '
            for x in range(8):
                if self.board[8 * y + x] == EMPTY:
                    row += ' '
                else:
                    row += translation_to_fen[self.board[8 * y + x]]
                row += ' '
            row += '|'
            print(row)
        print('+-----------------+')

        # print castle rights
        row = 'Castle: '
        for player in ('white', 'black'):
            row += player + ' '
            if self.castle[player]['short']:
                if self.castle[player]['long']:
                    row += 'both'
                else:
                    row += 'kingside'
            else:
                if self.castle[player]['long']:
                    row += 'queenside'
                else:
                    row += 'none'
            if player == 'white':
                row += ', '
        print(row)

        # print move number/moves for draw rule/en passant
        row = 'Move: ' + str(self.move_number) + ' ' + self.turn
        row += ', draw rule: ' + str(self.half_move_count_for_draw)
        row += ', en passant: '
        if self.en_passant:
            row += translate_index_into_field(self.en_passant_square)
        else:
            row += '-'
        print(row)

        # print checkmate/stalemate
        if self.is_checkmate():
            if self.turn == 'white':
                winner = 'Black'
            else:
                winner = 'White'
            print('CHECKMATE!', winner, 'won the game!')
        elif self.is_draw():
            print('Draw!')

    def switch_turn(self):
        """
        Switches the player that can make a move.
        """
        # switch turn
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'


def is_field(index: int) -> bool:
    return 0 <= index <= 63


def create_from_fen(fen: str) -> Chessboard:
    """
    Creates a new chessboard out of the FEN notation of a position.
    :param fen: The position in FEN-Format. If fen is empty, an empty board is returned.
    :return: The Chessboard corresponding to the FEN.
    """
    # initialize variables
    board = []
    castle = {
        'white': {
            'short': False,
            'long': False,
        },
        'black': {
            'short': False,
            'long': False,
        }
    }
    en_passant = False
    en_passant_field = 0

    # check special cases
    if len(fen) == 0:
        # empty board
        turn = 'white'
        move_number = 1
        half_move_count_for_draw = 0
        for i in range(64):
            board.append(EMPTY)
        return Chessboard(board, turn, castle, en_passant, en_passant_field, move_number, half_move_count_for_draw)

    # parse FEN data
    position_data = fen.split(' ')
    position = position_data[0].split('/')

    # load additional data
    if position_data[1] == 'w':
        turn = 'white'
    else:
        turn = 'black'
    if 'K' in position_data[2]:
        castle['white']['short'] = True
    if 'Q' in position_data[2]:
        castle['white']['long'] = True
    if 'k' in position_data[2]:
        castle['black']['short'] = True
    if 'q' in position_data[2]:
        castle['black']['long'] = True
    if position_data[3] != '-':
        en_passant = True
        en_passant_field = translate_field_into_index(position_data[3])
    move_number = int(position_data[5])
    half_move_count_for_draw = int(position_data[4])

    # load position
    for y in range(8):
        for field in position[7 - y]:
            if field.isnumeric() and 1 <= int(field) <= 8:
                for i in range(int(field)):
                    board.append(EMPTY)
            else:
                board.append(translation_from_fen[field])
    return Chessboard(board, turn, castle, en_passant, en_passant_field, move_number, half_move_count_for_draw)


def create_starting_position() -> Chessboard:
    """
    Creates a chessboard with the starting position.
    :return: A new chessboard with the starting position.
    """
    # starting position of a chess game
    starting_position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    return create_from_fen(starting_position)


def translate_field_into_index(field: str) -> int:
    """
    Translates a field identifier in text form (e.g. c5) into an index.
    :param field: The field.
    :return: The field index.
    """
    field_x = ord(field[0]) - 97
    field_y = int(field[1]) - 1
    return field_x + 8 * field_y


def translate_index_into_field(index: int) -> str:
    """
    Translates an index into a field identifier in text form (e.g. c5).
    :param: The field index.
    :return field: The field.
    """
    return chr(index % 8 + 97) + str((index // 8) + 1)
