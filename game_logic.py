import random

# --- Chance and Community Chest cards ---
CHANCE_CARDS = [
    ("Advance to GO", lambda p, b: setattr(p, "position", b.head)),
    ("Go to Jail", lambda p, b: p.go_to_jail(find_jail(b))),
    ("Collect $50", lambda p, b: setattr(p, "money", p.money + 50)),
    ("Pay $50 fine", lambda p, b: setattr(p, "money", max(0, p.money - 50))),
]

COMMUNITY_CHEST_CARDS = [
    ("Bank error in your favor. Collect $200", lambda p, b: setattr(p, "money", p.money + 200)),
    ("Doctor's fee. Pay $50", lambda p, b: setattr(p, "money", max(0, p.money - 50))),
    ("From sale of stock you get $45", lambda p, b: setattr(p, "money", p.money + 45)),
    ("Go to Jail", lambda p, b: p.go_to_jail(find_jail(b))),
]


def find_jail(board):
    """Find the jail node on the board."""
    current = board.head
    while True:
        if current.name == "Jail / Just Visiting":
            return current
        current = current.next
        if current == board.head:
            break
    return board.head  # Fallback


def draw_card(player, deck, deck_name, board):
    """Randomly select a card and apply its effect."""
    card_text, action = random.choice(deck)
    print(f"{player.name} drew a {deck_name} card: {card_text}")
    action(player, board)


def take_turn(player, board):
    """Handle a full player turn including movement, property actions, and card draws."""
    if player.jailed:
        print(f"{player.name} is in jail and cannot move this turn.")
        player.in_jail_turns += 1
        if player.in_jail_turns >= 3:
            player.jailed = False
            player.in_jail_turns = 0
            print(f"{player.name} has served their sentence and is released from jail.")
        return

    # Remove the separate roll - move() handles it internally
    print(f"\n🎲 {player.name}'s turn:")
    player.move()

    current = player.position

    # --- Handle card spaces ---
    if current.name == "Chance":
        draw_card(player, CHANCE_CARDS, "Chance", board)
    elif current.name == "Community Chest":
        draw_card(player, COMMUNITY_CHEST_CARDS, "Community Chest", board)
    elif current.name == "Go To Jail":
        player.go_to_jail(find_jail(board))
        return

    # --- Handle property spaces ---
    if hasattr(current, "price") and current.price > 0:
        if current.owner is None:
            player.attempt_purchase()
        elif current.owner != player:
            player.pay_rent()

    # --- Property development ---
    player.develop_property()

    if player.money <= 0:
        print(f"💀 {player.name} has gone bankrupt!")
        player.money = 0
        return
    
    # --- End of turn status ---
    print(f"End of {player.name}'s turn: ${player.money}\n")