# main.py
from board import create_monopoly_board
from player import Player
from game_logic import take_turn

# Create board and players
board = create_monopoly_board()
player1 = Player("Alice", board.head)
player2 = Player("Bob", board.head)

players = [player1, player2]

# Simulate 5 turns
for turn in range(5):
    print(f"\n=== Turn {turn + 1} ===")
    for player in players:
        take_turn(player)