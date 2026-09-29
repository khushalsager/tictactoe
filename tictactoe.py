#!/usr/bin/env python3
"""Unbeatable Tic-Tac-Toe: you play X, the computer plays O using minimax."""

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def winner(b):
    for a, c, d in WINS:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None


def minimax(b, is_ai):
    w = winner(b)
    if w == "O":
        return 1
    if w == "X":
        return -1
    if " " not in b:
        return 0
    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if is_ai else "X"
            scores.append(minimax(b, not is_ai))
            b[i] = " "
    return max(scores) if is_ai else min(scores)


def best_move(b):
    best, move = -2, None
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax(b, False)
            b[i] = " "
            if score > best:
                best, move = score, i
    return move


def show(b):
    print()
    for r in range(3):
        print(" " + " | ".join(b[r * 3:r * 3 + 3]))
        if r < 2:
            print("---+---+---")
    print()


def main():
    board = [" "] * 9
    print("Tic-Tac-Toe! You are X. Enter a cell number 1-9:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")
    while True:
        try:
            move = int(input("\nYour move: ")) - 1
            if move not in range(9) or board[move] != " ":
                raise ValueError
        except ValueError:
            print("Invalid move, try again.")
            continue
        board[move] = "X"
        if not winner(board) and " " in board:
            board[best_move(board)] = "O"
        show(board)
        w = winner(board)
        if w:
            print(f"{w} wins!")
            break
        if " " not in board:
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
