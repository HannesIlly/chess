import random

import chessboard
import engine

if __name__ == '__main__':
    board = chessboard.create_starting_position()
    engine = engine.Engine(board)

    # board.print()
    # for i in range(10):
    #     moves = board.generate_moves()
    #     print(moves)
    #     board.move(moves[random.randint(0, len(moves)-1)])
    #     board.print()
    #     print('Move list:', board.moves)

    while not (board.is_checkmate() or board.is_draw()):
        board.print()
        engine.make_move(3)
        print(board.moves)
    board.print()

    """ boards for old tests:
    # stalemate
    # board = chessboard.create_from_fen('rn2k1nr/1p4pp/3p4/p1pP4/PbP2p1q/1b2pPRP/1P1NP1PQ/2B1KBNR w K - 0 1')
    # checkmate
    # board = chessboard.create_from_fen('4k1nr/1p4pp/3p4/p1pP4/PbP2p1q/1b1nrPRP/1P1NP1PQ/2B1KBNR w K - 0 1')
    """

    """ old tests:
    
    # get all possible moves (for the current player)
    moves = board.generate_moves()
    for move in moves:
        field = chessboard.translate_index_into_field(move[0])
        target = chessboard.translate_index_into_field(move[1])

        if len(move) == 3:
            print(field, '->', target, '(', move[2], ')')
        else:
            print(field, '->', target)
    print('---------------')
    
    # get all by white attacked fields
    for field_index in range(64):
        field = chessboard.translate_index_into_field(field_index)
        message = ''
        if board.is_attacked_by_white(field_index):
            message += 'is attacked by white.'
        else:
            message += 'is NOT attacked by white.'
        print(field, message)

    # get all by black attacked fields
    for field_index in range(64):
        field = chessboard.translate_index_into_field(field_index)
        message = ''
        if board.is_attacked_by_black(field_index):
            message += 'is attacked by black.'
        else:
            message += 'is NOT attacked by black.'
        print(field, message)
    """
