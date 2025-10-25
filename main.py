from board import create_monopoly_board
from player import Player
import random

board = create_monopoly_board()
players = [
    Player("Alice", board.head),
    Player("Bob", board.head)
]

for turn in range(8):
    print(f"\n--- Turn {turn + 1} ---")
    for player in players:
        roll = random.randint(2, 12)
        print(f"{player.name} rolls {roll}")
        player.move(roll)
        player.display_status()