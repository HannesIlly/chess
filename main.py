import chessboard

if __name__ == '__main__':
    # random relatively full position with many different moves.
    board = chessboard.create_from_fen('r3k2r/2bp2P1/1pp1p1n1/pP2Pp1P/n2qP3/1B3N2/P1QP1PP1/R3K2R w KQkq a6 0 24')
    board.print()

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
