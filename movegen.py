from typing import Dict, List, Any
import chess
from evaluate import *

def get_ordered_moves(board: chess.Board):
    end_game = check_end_game(board)

    def ordering(move):
        return move_value(board, move, end_game)

    in_order = sorted(
        board.legal_moves, key=ordering, reverse=(board.turn == chess.WHITE)
    )
    return list(in_order)

'''
Minimax algorithm:
https://www.youtube.com/watch?v=CAEI_J50B18&t=1174s&ab_channel=%C4%90%E1%BB%97Ph%C3%BAcH%E1%BA%A3o
https://en.wikipedia.org/wiki/Minimax

Pseudocode from wiki: 

function  minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := -inf
        for each child of node do
            value := max(value, minimax(child, depth - 1, FALSE))
        return value
    else (* minimizing player *)
        value := inf
        for each child of node do
            value := min(value, minimax(child, depth - 1, TRUE))
        return value
'''

def minimax_ab(depth: int, board: chess.Board, alpha:float, beta:float, maxPlayer: bool):
    if board.is_game_over(): 
        return 0
    if board.is_checkmate():
        return -100000000000 if maxPlayer else 100000000000

    if depth == 0:
            return evaluate_board(board)
    if maxPlayer:
        best_move = -float("inf")
        moves = get_ordered_moves(board)
        for move in moves:
            board.push(move)
            best_move = max(best_move, minimax_ab(depth-1, board, alpha, beta, not maxPlayer))
            board.pop()
            alpha = max(alpha, best_move)
            #if alpha >= beta: return best_move
            if best_move >= beta: break
        return best_move
    else:
        best_move = float("inf")
        moves = get_ordered_moves(board)
        for move in moves:
            board.push(move)
            best_move = min(best_move, minimax_ab(depth-1, board, alpha, beta, maxPlayer))
            board.pop()
            beta = min(beta, best_move)
            #if alpha >= beta: return best_move
            if best_move <= alpha: break
        return best_move




def minimax_root(depth: int, board: chess.Board):
    max = board.turn == chess.WHITE
    if max: 
        best_move = -float("inf")
    else: 
        best_move = float("inf")


    moves = get_ordered_moves(board)
    best_move_minimax = moves[0]

    for move in moves:
        board.push(move)
        if board.can_claim_draw(): value = 0
        else: value = minimax_ab(depth-1, board, -float("inf"), float("inf"), not max)
        board.pop()
        if max and value >= best_move:
            best_move = value
            best_move_minimax = move
        elif not max and value <= best_move:
            best_move = value
            best_move_minimax = move
    
    return best_move_minimax


def next_move(depth: int, board:chess.Board):
    return minimax_root(depth, board)

def next_move_stupid(depth: int, board: chess.Board):
    return minimax_root(depth-1, board)



        