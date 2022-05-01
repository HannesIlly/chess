import chessboard

if __name__ == '__main__':
    board = chessboard.create_from_fen('1k5r/p7/1pn5/5B2/1pP1K3/8/3B4/8 b - c3 5 34')
    board.print()
