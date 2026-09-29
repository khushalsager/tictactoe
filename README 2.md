# ❌⭕ Tic-Tac-Toe with Minimax AI

A terminal Tic-Tac-Toe game in Python where the computer plays **perfectly** using the minimax algorithm. The best you can do is draw!

## Requirements
- Python 3.8+ (no external packages)

## Run
```bash
python tictactoe.py
```

## How to play
You are `X`. Enter a number from 1–9 to place your mark:
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## How it works
The AI explores every possible future game state recursively (`minimax`), scoring a win as +1, a loss as -1, and a draw as 0, then picks the move with the best guaranteed outcome. Tic-Tac-Toe is small enough that no pruning is needed.

## Ideas for extension
- Add alpha-beta pruning
- Let the player choose X or O / who moves first
- Add a GUI with Tkinter

## License
MIT
