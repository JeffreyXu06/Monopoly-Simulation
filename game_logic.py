import random

CHANCE_CARDS = [
    ("Advance to GO", lambda p: p.move(40)),
    ("Go to Jail", lambda p: p.go_to_jail()),
    ("Collect $50", lambda p: setattr(p, "money", p.money + 50)),
    ("Pay $50 fine", lambda p: setattr(p, "money", p.money - 50)),
]

COMMUNITY_CHEST_CARDS = [
    ("Bank error in your favor. Collect $200", lambda p: setattr(p, "money", p.money + 200)),
    ("Doctor's fee. Pay $50", lambda p: setattr(p, "money", p.money - 50)),
    ("From sale of stock you get $45", lambda p: setattr(p, "money", p.money + 45)),
    ("Go to Jail", lambda p: p.go_to_jail()),
]

def draw_card(player, deck, deck_name):
    card_text, action = random.choice(deck)
    print(f"{player.name} drew a {deck_name} card: {card_text}")
    action(player)

def take_turn(player):
    if player.jailed:
        print(f"{player.name} is in jail and cannot move this turn.")
        player.turns_in_jail += 1
        if player.turns_in_jail >= 3:
            player.jailed = False
            player.turns_in_jail = 0
            print(f"{player.name} has served their sentence and is released from jail.")
        return

    roll = random.randint(2, 12)
    print(f"\n{player.name} rolls {roll}")
    player.move(roll)
    player.display_status()

    current = player.position
    if current.name == "Chance":
        draw_card(player, CHANCE_CARDS, "Chance")
    elif current.name == "Community Chest":
        draw_card(player, COMMUNITY_CHEST_CARDS, "Community Chest")

    if current.price > 0:
        if current.owner is None:
            player.buy_property()
        elif current.owner != player:
            player.pay_rent()

    # Optional: Try upgrading owned properties
    for prop in player.properties:
        if random.random() < 0.3:  # 30% chance to upgrade
            if prop.houses < 4 and not prop.hotel:
                player.buy_house(prop)
            elif prop.houses == 4 and not prop.hotel:
                player.buy_hotel(prop)