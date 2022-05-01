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


class Chessboard:
    """
    This class represents a chessboard with its position and some additional data like castle rights.
    """

    def __init__(self, board: list, turn: str, castle: dict, en_passant: bool, en_passant_field: int, move_number: int,
                 draw_counter: int) -> None:
        # initialize board
        self.evaluation = None
        self.board = board
        self.turn = turn
        self.castle = castle
        self.en_passant = en_passant
        self.en_passant_field = en_passant_field
        self.half_move_count_for_draw = draw_counter
        self.move_number = move_number
        # list of next board states
        self.next_states = []

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

    def move_piece(self, start: int, end: int) -> bool:
        """
        Moves a piece to an empty field. Does NOT check for illegal moves (e.g. move direction, checks, pins)
        :param start: The starting field.
        :param end: The destination field.
        :return: If the piece could be moved.
        """
        # check for special cases
        if self.is_empty(start):
            return False
        if not self.is_empty(end):
            return False

        # move the piece
        self.board[end] = self.board[start]
        self.board[start] = EMPTY
        return True

    def remove_piece(self, field: int) -> bool:
        """
        Removes a piece from the board.
        :param field: The field that is cleared.
        :return: If a piece was removed.
        """
        if self.is_empty(field):
            return False

        self.board[field] = EMPTY
        return True

    def has_evaluation(self) -> bool:
        return self.evaluation is not None

    def set_evaluation(self, evaluation: float) -> None:
        self.evaluation = evaluation

    def get_evaluation(self) -> float:
        return self.evaluation

    def generate_moves(self):
        moves = []  # list of tuples with from-square and to-square.
        for field in range(64):
            if self.is_empty(field):
                continue
            if self.turn == 'white' and self.is_white_piece(field):
                if self.has_piece(field, KING_WHITE):
                    moves.extend(self.get_king_moves(field))
                elif self.has_piece(field, QUEEN_WHITE):
                    moves.extend(self.get_queen_moves(field))
                elif self.has_piece(field, ROOK_WHITE):
                    moves.extend(self.get_rook_moves(field))
                elif self.has_piece(field, BISHOP_WHITE):
                    moves.extend(self.get_bishop_moves(field))
                elif self.has_piece(field, KNIGHT_WHITE):
                    moves.extend(self.get_knight_moves(field))
                else:
                    pass  # TODO pawn
            elif self.turn == 'black' and self.is_black_piece(field):
                pass  # TODO continue here with black moves

    def get_directional_moves(self, field: int, direction_x: int, direction_y: int, distance: int = 7) -> list:
        is_white_piece = self.is_white_piece(field)
        moves = []  # list of tuples with from-square and to-square.

        for i in range(1, distance + 1):
            target_field = field + i * direction_x + 8 * i * direction_y
            # check if the target field is still on the board
            if not is_field(target_field):
                return moves
            # check if the target field has not crossed the left/right border
            if direction_x < 0 and target_field % 8 > field % 8:
                return moves
            if direction_x > 0 and target_field % 8 < field % 8:
                return moves
            # check if a piece was reached. (capture or same colour)
            if not self.is_empty(target_field):
                if not self.is_same_colour(field, target_field):
                    move = (field, target_field)
                    moves.append(move)
                return moves

            move = (field, target_field)
            moves.append(move)
        return moves

    def get_diagonal_moves(self, field, distance=7):
        moves = []
        moves.extend(self.get_directional_moves(field, -1, -1, distance))
        moves.extend(self.get_directional_moves(field, -1, 1, distance))
        moves.extend(self.get_directional_moves(field, 1, -1, distance))
        moves.extend(self.get_directional_moves(field, 1, 1, distance))
        return moves

    def get_straight_moves(self, field, distance=7):
        moves = []
        moves.extend(self.get_directional_moves(field, 0, -1, distance))
        moves.extend(self.get_directional_moves(field, 0, 1, distance))
        moves.extend(self.get_directional_moves(field, -1, 0, distance))
        moves.extend(self.get_directional_moves(field, 1, 0, distance))
        return moves

    def get_king_moves(self, field):
        moves = []
        moves.extend(self.get_diagonal_moves(field, 1))
        moves.extend(self.get_straight_moves(field, 1))
        # check castle
        if self.is_white_piece(field):
            if field == translate_field_into_index('e1'):
                if self.castle['white']['short']:
                    pass  # TODO check castle
                if self.castle['white']['long']:
                    pass  # TODO check castle
        elif self.is_black_piece(field):
            if field == translate_field_into_index('e8'):
                if self.castle['black']['short']:
                    pass  # TODO check castle
                if self.castle['black']['long']:
                    pass  # TODO check castle
        return moves

    def get_queen_moves(self, field):
        moves = []
        moves.extend(self.get_diagonal_moves(field))
        moves.extend(self.get_straight_moves(field))
        return moves

    def get_rook_moves(self, field):
        return self.get_straight_moves(field)

    def get_bishop_moves(self, field):
        return self.get_diagonal_moves(field)

    def get_knight_moves(self, field):
        moves = []
        moves.extend(self.get_directional_moves(field, -2, -1, 1))
        moves.extend(self.get_directional_moves(field, -2, 1, 1))
        moves.extend(self.get_directional_moves(field, -1, 2, 1))
        moves.extend(self.get_directional_moves(field, -1, -2, 1))
        moves.extend(self.get_directional_moves(field, 1, -2, 1))
        moves.extend(self.get_directional_moves(field, 1, 2, 1))
        moves.extend(self.get_directional_moves(field, 2, -1, 1))
        moves.extend(self.get_directional_moves(field, 2, 1, 1))
        return moves

    def get_pawn_moves(self):
        pass  # TODO normal, long, en passant, promotion
        # TODO maybe split into white/black

    def has_piece(self, field: int, piece: int):
        if 0 <= field <= 63:
            if self.board[field] == piece:
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
            row += translate_index_into_field(self.en_passant_field)
        else:
            row += '-'
        print(row)


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