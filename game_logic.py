import random

# --- Chance and Community Chest cards ---
CHANCE_CARDS = [
    ("Advance to GO", lambda p, b: p.move(40)),  # Loops around board
    ("Go to Jail", lambda p, b: p.go_to_jail()),
    ("Collect $50", lambda p, b: setattr(p, "money", p.money + 50)),
    ("Pay $50 fine", lambda p, b: setattr(p, "money", p.money - 50)),
]

COMMUNITY_CHEST_CARDS = [
    ("Bank error in your favor. Collect $200", lambda p, b: setattr(p, "money", p.money + 200)),
    ("Doctor's fee. Pay $50", lambda p, b: setattr(p, "money", p.money - 50)),
    ("From sale of stock you get $45", lambda p, b: setattr(p, "money", p.money + 45)),
    ("Go to Jail", lambda p, b: p.go_to_jail()),
]


def draw_card(player, deck, deck_name, board):
    """Randomly select a card and apply its effect."""
    card_text, action = random.choice(deck)
    print(f"{player.name} drew a {deck_name} card: {card_text}")
    action(player, board)


def take_turn(player, board):
    """Handle a full player turn including movement, property actions, and card draws."""
    if player.jailed:
        print(f"{player.name} is in jail and cannot move this turn.")
        player.turns_in_jail += 1
        if player.turns_in_jail >= 3:
            player.jailed = False
            player.turns_in_jail = 0
            print(f"{player.name} has served their sentence and is released from jail.")
        return

    roll = random.randint(2, 12)
    print(f"\n🎲 {player.name} rolls {roll}")
    player.move(roll)
    player.display_status()

    current = player.position

    # --- Handle card spaces ---
    if current.name == "Chance":
        draw_card(player, CHANCE_CARDS, "Chance", board)
    elif current.name == "Community Chest":
        draw_card(player, COMMUNITY_CHEST_CARDS, "Community Chest", board)
    elif current.name == "Go To Jail":
        player.go_to_jail()
        return

    # --- Handle property spaces ---
    if current.price > 0:
        if current.owner is None:
            decision = random.choice(["buy", "skip"])  # could later be user input
            if decision == "buy" and player.money >= current.price:
                player.buy_property()
            else:
                print(f"{player.name} decided not to buy {current.name}.")
        elif current.owner != player:
            player.pay_rent(board)

    # --- Optional: Simulate random house/hotel purchases if the player can afford it ---
    if current.owner == player and current.color:
        # Randomly decide to build (for testing AI behavior)

        if random.random() < 1:
            player.buy_house(current, board)
        elif random.random() < 0.5:
            player.buy_hotel(current, board)

    # --- End of turn status ---
    print(f"End of {player.name}'s turn: ${player.money}\n")