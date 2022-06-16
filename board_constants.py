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
    'a3': 16,
    'b3': 17,
    'c3': 18,
    'd3': 19,
    'e3': 20,
    'f3': 21,
    'g3': 22,
    'h3': 23,
    'a4': 24,
    'b4': 25,
    'c4': 26,
    'd4': 27,
    'e4': 28,
    'f4': 29,
    'g4': 30,
    'h4': 31,
    'a5': 32,
    'b5': 33,
    'c5': 34,
    'd5': 35,
    'e5': 36,
    'f5': 37,
    'g5': 38,
    'h5': 39,
    'a6': 40,
    'b6': 41,
    'c6': 42,
    'd6': 43,
    'e6': 44,
    'f6': 45,
    'g6': 46,
    'h6': 47,
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
