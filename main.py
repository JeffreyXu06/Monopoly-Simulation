from board import create_monopoly_board
from player_alice import Alice
from player_bob import Bob
from game_logic import take_turn

def play_game(game_number, max_turns=250, verbose=True):
    """Play a single game of Monopoly."""
    board = create_monopoly_board()
    
    players = [
        Alice(board.head),
        Bob(board.head),
    ]
    
    turn = 0
    
    while sum(p.money > 0 for p in players) > 1 and turn < max_turns:
        turn += 1

        if verbose:
            print(f"\n{'='*50}")
            print(f"=== TURN {turn} ===")
            print(f"{'='*50}\n")
            
            
        
        for player in players:



            if player.money > 0:
                take_turn(player, board)
    
    if verbose:
        print("\n🏁 Game Over! 🏁")
    
    players_sorted = sorted(players, key=lambda p: p.money, reverse=True)
    
    if verbose:
        for i, p in enumerate(players_sorted, start=1):
            status = "💀 Bankrupt" if p.money <= 0 else f"${p.money}"
            print(f"{i}. {p.name}: {status}")
    
    winner = players_sorted[0]
    if verbose:
        print(f"\n🏆 {winner.name} wins with ${winner.money} remaining!")
    
    return winner.name, winner.money, turn


def simulate_multiple_games(num_games=100, max_turns=250):
    """Simulate multiple games and track statistics."""
    print(f"🎮 Starting simulation of {num_games} games...\n")
    
    results = {
        "Alice": {"wins": 0, "total_money": 0, "bankruptcies": 0},
        "Bob": {"wins": 0, "total_money": 0, "bankruptcies": 0}
    }
    
    total_turns = 0
    
    for i in range(1, num_games + 1):
        winner_name, winner_money, turns = play_game(i, max_turns, verbose=True)
        
        results[winner_name]["wins"] += 1
        results[winner_name]["total_money"] += winner_money
        
        if winner_money <= 0:
            results[winner_name]["bankruptcies"] += 1
        
        total_turns += turns
        
        # Print progress every 10 games
        if i % 10 == 0:
            print(f"Completed {i}/{num_games} games...")
    
    # Print final statistics
    print("\n" + "="*50)
    print("📊 SIMULATION RESULTS")
    print("="*50)
    
    for player_name, stats in results.items():
        win_rate = (stats["wins"] / num_games) * 100
        avg_money = stats["total_money"] / stats["wins"] if stats["wins"] > 0 else 0
        
        print(f"\n{player_name}:")
        print(f"  Wins: {stats['wins']}/{num_games} ({win_rate:.1f}%)")
        print(f"  Average money when winning: ${avg_money:.2f}")
        print(f"  Bankruptcies: {stats['bankruptcies']}")
    
    avg_turns = total_turns / num_games
    print(f"\nAverage game length: {avg_turns:.1f} turns")
    
    # Determine and announce the overall winner
    print("\n" + "="*50)
    alice_wins = results["Alice"]["wins"]
    bob_wins = results["Bob"]["wins"]
    
    if alice_wins > bob_wins:
        print(f"🏆 OVERALL WINNER: Alice ({alice_wins} wins vs {bob_wins})")
        win_margin = alice_wins - bob_wins
        print(f"   Alice won {win_margin} more games than Bob!")
    elif bob_wins > alice_wins:
        print(f"🏆 OVERALL WINNER: Bob ({bob_wins} wins vs {alice_wins})")
        win_margin = bob_wins - alice_wins
        print(f"   Bob won {win_margin} more games than Alice!")
    else:
        print(f"🤝 IT'S A TIE! Both players won {alice_wins} games each!")
    
    print("="*50)


if __name__ == "__main__":
    # Simulate 100 games
    simulate_multiple_games(num_games=100, max_turns=250)
    
    # Optional: Play one verbose game to see details
    print("\n\n" + "="*50)