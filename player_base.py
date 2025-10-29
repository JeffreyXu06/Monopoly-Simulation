import random

class PlayerBase:
    """
    Base player class that defines shared logic for all Monopoly players.
    Each player subclass (e.g., Alice, Bob) customizes buy/build probabilities.
    """
    def __init__(self, name, buy_property_rate, buy_house_rate, buy_hotel_rate):
        self.name = name
        self.money = 1500
        self.position = None  # Board node (LinkedList node)
        self.properties = []
        self.buy_property_rate = buy_property_rate
        self.buy_house_rate = buy_house_rate
        self.buy_hotel_rate = buy_hotel_rate
        self.jailed = False
        self.in_jail_turns = 0

    # ---------------- Movement ----------------
    def roll_dice(self):
        """Roll two six-sided dice."""
        return random.randint(1, 6) + random.randint(1, 6)

    def move(self):
        """Move around the board according to dice roll."""
        if self.jailed:
            self.in_jail_turns += 1
            if self.in_jail_turns >= 3:
                print(f"{self.name} has served their time and leaves jail.")
                self.jailed = False
                self.in_jail_turns = 0
            else:
                print(f"{self.name} is still in jail (Turn {self.in_jail_turns}/3).")
            return

        steps = self.roll_dice()
        for _ in range(steps):
            self.position = self.position.next

        print(f"{self.name} rolled {steps} and landed on {self.position.name}")

    # ---------------- Property Logic ----------------
    def attempt_purchase(self):
        """Attempt to buy an unowned property based on player's personality."""
        node = self.position
        if node.price > 0 and node.owner is None:
            # Calculate adjusted buy rate based on money remaining after purchase
            money_after_purchase = self.money - node.price
            adjusted_rate = self.buy_property_rate
            
            if money_after_purchase < 150:
                adjusted_rate *= 0.3  # Only 30% as likely to buy when it would leave them low on cash
            
            if random.random() < adjusted_rate and self.money >= node.price:
                node.owner = self
                self.properties.append(node)
                self.money -= node.price
                print(f"{self.name} bought {node.name} for ${node.price}")
            else:
                print(f"{self.name} decided not to buy {node.name}.")
        elif node.owner and node.owner != self:
            self.pay_rent()

    def pay_rent(self):
        """Pay rent to the owner of the current property."""
        node = self.position
        owner = node.owner
        if not owner or owner == self:
            return

        rent = node.rent
        if rent > 0:
            payment = min(self.money, rent)
            self.money -= payment
            owner.money += payment
            print(f"{self.name} paid ${payment} rent to {owner.name} for {node.name}")

    def develop_property(self):
        """Attempt to build houses or hotels on owned properties."""
        for prop in self.properties:
            if prop.price == 0 or prop.color is None:
                continue  # Skip non-buildable properties

            # Try building a house
            if not prop.hotel and prop.houses < 4:
                # Check if building would leave them with less than $150
                money_after_building = self.money - prop.house_cost
                if money_after_building < 150:
                    continue  # Skip building if it would leave them too low on cash
                
                if self.money >= prop.house_cost and random.random() < self.buy_house_rate:
                    prop.houses += 1
                    self.money -= prop.house_cost
                    print(f"{self.name} built a house on {prop.name} ({prop.houses} total).")

            # Try upgrading to a hotel
            elif prop.houses == 4 and not prop.hotel:
                # Check if upgrading would leave them with less than $150
                money_after_building = self.money - prop.house_cost
                if money_after_building < 150:
                    continue  # Skip upgrading if it would leave them too low on cash
                
                if self.money >= prop.house_cost and random.random() < self.buy_hotel_rate:
                    prop.hotel = True
                    prop.houses = 0
                    self.money -= prop.house_cost
                    print(f"{self.name} upgraded {prop.name} to a hotel!")

    # ---------------- Jail Logic ----------------
    def go_to_jail(self, jail_node):
        """Send the player to jail."""
        self.position = jail_node
        self.jailed = True
        self.in_jail_turns = 0
        print(f"{self.name} has been sent to jail!")

    # ---------------- Status Display ----------------
    def get_status(self):
        """Return or print a summary of the player's current state."""
        owned = ", ".join(p.name for p in self.properties) or "None"
        print(f"--- {self.name}'s Status ---")
        print(f"Money: ${self.money}")
        print(f"Position: {self.position.name if self.position else 'Unknown'}")
        print(f"Owned Properties: {owned}")
        print(f"Jailed: {'Yes' if self.jailed else 'No'}\n")

    def __repr__(self):
        return f"<Player {self.name}: ${self.money}, Properties={len(self.properties)}>"