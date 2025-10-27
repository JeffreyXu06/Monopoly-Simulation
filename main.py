# main.py
from board import create_monopoly_board
from player import Player
from game_logic import take_turn

# Create board and players
board = create_monopoly_board()
player1 = Player("Alice", board.head)
player2 = Player("Bob", board.head)
player3 = Player("Cynthia", board.head)
player4 = Player("D4vd", board.head)

players = [player1, player2, player3, player4]
# players = [player1, player2]
# # Simulate 5 turns
# for turn in range(5):
#     print(f"\n=== Turn {turn + 1} ===")
#     for player in players:
#         take_turn(player, board)


# Simulate till one runs out of money
turn = 0
while player1.money > 0 and player2.money > 0 and turn < 250:
    turn += 1
    print(f"\n=== Turn {turn} ===")
    for player in players:
        take_turn(player, board)

print("\n Game Over! ")
print(f"Total Turns Played: {turn}\n")

# Sort players by remaining money (descending)
players_sorted = sorted(players, key=lambda p: p.money, reverse=True)

# Print final scoreboard
print("=== Final Scoreboard ===")
for i, p in enumerate(players_sorted, start=1):
    status = "Bankrupt" if p.money <= 0 else f"${p.money}"
    print(f"{i}. {p.name}: {status}")

# Determine winner(s)
alive_players = [p for p in players if p.money > 0]
if len(alive_players) == 1:
    print(f"\n{alive_players[0].name} wins with ${alive_players[0].money} remaining!")
elif len(alive_players) > 1:
    print(f"\nNo clear winner after {turn} turns.")
    print(f"Top player: {players_sorted[0].name} (${players_sorted[0].money})")
else:
    print("\nAll players went bankrupt! No winners this time.")