import chess
from movegen import *
from evaluate import *

depth = 3

def depth_cal(is_end_game: bool, board: chess.Board) -> int:
    is_end_game = check_end_game(board)
    if is_end_game:
        return 3
    return 2


def print_board(board: chess.Board) -> str:
    # inspired by sunfish
    # https://github.com/thomasahle/sunfish/blob/master/fancy.py
    board_string = list(str(board))
    chess_piece = {
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "P": "♙",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "p": "♟",
        ".": "·",
    }
    for i, char in enumerate(board_string):
        if char in chess_piece:
            board_string[i] = chess_piece[char]
    rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []
    for rank in "".join(board_string).split("\n"):
        display.append(f"{rows.pop()} {rank}")
    if board.turn == chess.BLACK:
        display.reverse()
    display.append("  a b c d e f g h")
    return "\n" + "\n".join(display)

def get_move(board: chess.Board):
    '''ordered_move = get_ordered_moves(board)
    best_cur_move = ordered_move[0]'''
    move = input(f"\nEnter your move (Suggestion: {list(board.legal_moves)[0]}:\n")
    for legal_move in move:
        if move == str(legal_move):
            return legal_move
    return get_move(board) 
    

def start():
    board = chess.Board()
    moves = get_ordered_moves(board)
    user_side = (
        chess.WHITE if input("Start as [w]hite or [b]lack: ") == "w" else chess.BLACK
    )

    if user_side == chess.WHITE:
        print(print_board(board))
        board.push(get_move(board))
        #board.push(next_move(depth, board))
        #board.push(next_move(depth_cal(check_end_game(board), board), board))

    while not board.is_game_over():
        board.push(next_move(depth, board))
        #board.push(next_move_stupid(depth, board))
        print(print_board(board))
        board.push(get_move(board))
        #board.push(next_move(depth, board))
        #board.push(next_move(depth_cal(check_end_game(board), board), board))

    print(f"\nResult: [w]{board.result()}[b]")

if __name__ == "__main__":
        start()
