import random

def take_turn(player):
    roll = random.randint(2, 12)
    print(f"\n{player.name} rolls {roll}")
    player.move(roll)
    player.display_status()

    # Handle property logic
    if player.position.price > 0:
        if player.position.owner is None:
            player.buy_property()
        elif player.position.owner != player:
            player.pay_rent()