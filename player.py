# player.py

class Player:
    def __init__(self, name, start_position, starting_money=1500):
        self.name = name
        self.position = start_position
        self.money = starting_money
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0

    def move(self, steps):
        """Move the player unless they are in jail."""
        if self.in_jail:
            self.jail_turns += 1
            print(f"{self.name} is in Jail (Turn {self.jail_turns}/3).")
            # Release automatically after 3 turns
            if self.jail_turns >= 3:
                self.release_from_jail()
            else:
                return

        # Move forward normally
        for _ in range(steps):
            self.position = self.position.next
        print(f"{self.name} lands on {self.position.name}")
        self.handle_landing()

    def handle_landing(self):
        """What happens when landing on a space."""
        space = self.position
        if space.name == "Go To Jail":
            self.send_to_jail()
            return

        if self.in_jail:
            return

        # Pay rent if owned by another player
        if space.owner and space.owner != self:
            self.pay_rent(space)
        # Buy if it's unowned and has a price
        elif space.price > 0 and space.owner is None:
            self.buy_property()
        else:
            print(f"{self.name} does nothing on {space.name}.")

    def send_to_jail(self):
        """Send the player to Jail."""
        print(f"{self.name} is sent directly to Jail!")
        # Move until reaching the Jail space
        while self.position.name != "Jail / Just Visiting":
            self.position = self.position.next
        self.in_jail = True
        self.jail_turns = 0

    def release_from_jail(self):
        """Release the player after serving jail turns."""
        self.in_jail = False
        self.jail_turns = 0
        print(f"{self.name} is released from Jail!")

    def buy_property(self):
        space = self.position
        if self.money >= space.price:
            space.owner = self
            self.money -= space.price
            self.properties.append(space)
            print(f"{self.name} buys {space.name} for ${space.price}.")
        else:
            print(f"{self.name} cannot afford {space.name} (${space.price}).")

    def pay_rent(self, space):
        rent = space.rent
        owner = space.owner
        if self.money < rent:
            print(f"{self.name} cannot afford rent (${rent}) to {owner.name}!")
            self.money = 0
        else:
            self.money -= rent
            owner.money += rent
            print(f"{self.name} pays ${rent} rent to {owner.name} for {space.name}.")

    def display_status(self):
        status = f"{self.name}: ${self.money} | Current: {self.position.name}"
        if self.in_jail:
            status += " (In Jail)"
        print(status)
        if self.properties:
            print("  Owns:", ", ".join([p.name for p in self.properties]))