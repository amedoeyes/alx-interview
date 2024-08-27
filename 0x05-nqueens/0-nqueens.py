#!/usr/bin/python3

"""N-Queens"""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)


if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)


if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)


n = int(sys.argv[1])


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        same_row_or_diagonal = board[i] == row or board[i] == row - col + i
        same_anti_diagonal = board[i] == row + col - i
        if same_row_or_diagonal or same_anti_diagonal:
            return False
    return True


def solve(board, col):
    """Use backtracking to find all solutions"""
    if col == n:
        print([[i, board[i]] for i in range(n)])
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve(board, col + 1)
            board


board = [0 for i in range(n)]
solve(board, 0)
