This project is a fully object-oriented simulation of the Monopoly board game written in Python.
It models the complete gameplay loop including property ownership, rent calculation, player strategies, and rule enforcement.
The goal is to enable experimentation with different player behaviors and statistical analysis of gameplay outcomes.

board.py	              Defines the Monopoly board layout, property data, and color groups.
player_base.py	        Base class defining common player behavior and shared attributes.
alice.py, bob.py	      Example subclasses implementing custom player strategies.
game_logic.py	          Coordinates a full game simulation; handles turns, dice rolls, and rules.
main.py                 Sets up the game to start

To run a single simulation with default players: python game.py

To modify player strategies or simulation parameters:
  1.  Edit game.py to change the player list (e.g., players = [Alice(), Bob()])
  2.  Adjust constants such as NUM_GAMES, STARTING_CASH, or logging level.


To add something a new player:
1.  Create a new file in the project root (e.g., charlie.py).
Subclass from PlayerBase:

#from player_base import PlayerBase
#class Alice(PlayerBase):
    #def __init__(self, start_position):


Register your player in game.py:

from charlie import Charlie
players = [Alice(), Bob(), Charlie()]

To edit board configuration, modify the data in board.py.
To implement new mechanics (like auctions or taxes), extend Game._handle_tile() or relevant helper methods.
