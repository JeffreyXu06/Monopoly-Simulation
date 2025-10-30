I don't know how to write a README, so I will just put down whats important. 

Main.py line 6
def play_game(game_number, max_turns=250, verbose=True):
                                ^ max number of turns per game

Main.py line 115
simulate_multiple_games(num_games=100, max_turns=250)
                          ^ determine how many games are going to be simulated.

If you want to make your own player just add a player file, with the same attributes, you can change them to see what the optimal strategy is. 
This program simulates two monopoly players with different personalities playing at random. 
