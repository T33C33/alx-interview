#!/usr/bin/python3
import sys


def print_usage_and_exit(message):
    print(message)
    sys.exit(1)


# Validate input
if len(sys.argv) != 2:
    print_usage_and_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except ValueError:
    print_usage_and_exit("N must be a number")

if N < 4:
    print_usage_and_exit("N must be at least 4")


# Backtracking function
def solve_nqueens(N):
    solutions = []
    board = [-1] * N  # -1 indicates no queen is placed in that row

    def is_safe(row, col):
        # Check if the queen can be placed at (row, col)
        for i in range(row):
            # Check if there's a conflict with previous rows
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def place_queens(row):
        # Place queens row by row
        if row == N:
            # If all queens are placed, add solution
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                place_queens(row + 1)
                board[row] = -1  # Backtrack

    place_queens(0)
    return solutions


# Find and print all solutions
solutions = solve_nqueens(N)
for solution in solutions:
    print(solution)
