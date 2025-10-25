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

#players = [player1, player2, player3, player4]
players = [player1, player2]
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

if player1.money > 0 and player2.money <= 0:
    winner = player1  
    loser = player2 if winner == player1 else player1
    print(f"\n🏁 Game over! {winner.name} wins with ${winner.money} remaining.")
    print(f"{loser.name} went bankrupt at turn {turn}.")
elif player1.money <= 0 and player2.money > 0:
    winner = player1  
    loser = player2 if winner == player1 else player1
    print(f"\n🏁 Game over! {winner.name} wins with ${winner.money} remaining.")
    print(f"{loser.name} went bankrupt at turn {turn}.")
elif player1.money > 0 and player2.money > 0:
    if player1.money == player2.money:
         print(f"\n🏁 Game over! It's a tie with ${player1.money} remaining.")
    else:

        winner = player1 if player1.money > player2.money else player2
        loser = player1 if player1.money < player2.money else player2
        print(f"\n🏁 Game over! {winner.name} wins with ${winner.money} remaining.")
        print(f"{loser.name} had less money on turn {turn} with ${loser.money} remaining.")