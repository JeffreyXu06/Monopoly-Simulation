from board import create_monopoly_board
from player_alice import Alice
from player_bob import Bob
from game_logic import take_turn

board = create_monopoly_board()

players = [
    Alice(board.head),
    Bob(board.head),
]

turn = 0
MAX_TURNS = 250

while sum(p.money > 0 for p in players) > 1 and turn < MAX_TURNS:
    turn += 1
    print(f"\n=== Turn {turn} ===")
    for player in players:
        if player.money > 0:
            take_turn(player, board)

print("\n Game Over On Turn " + str(turn))
players_sorted = sorted(players, key=lambda p: p.money, reverse=True)
for i, p in enumerate(players_sorted, start=1):
    status = "💀 Bankrupt" if p.money <= 0 else f"${p.money}"
    print(f"{i}. {p.name}: {status}")

winner = players_sorted[0]
print(f"\n🏆 {winner.name} wins with ${winner.money} remaining!")