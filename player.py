class Player:
    def __init__(self, name, start_position, starting_money=1500):
        self.name = name
        self.position = start_position
        self.money = starting_money
        self.properties = []
        self.jailed = False
        self.turns_in_jail = 0

    def move(self, steps):
        if self.jailed:
            print(f"{self.name} is in jail and cannot move this turn.")
            self.turns_in_jail += 1
            if self.turns_in_jail >= 3:
                print(f"{self.name} has served their sentence and is released from jail.")
                self.jailed = False
                self.turns_in_jail = 0
            return

        for _ in range(steps):
            if self.position.next.name == "GO":
                self.money += 200
                print(f"{self.name} passed GO and collected $200!")
            self.position = self.position.next

        if self.position.name == "Go To Jail":
            print(f"{self.name} landed on Go To Jail!")
            self.go_to_jail()

    def go_to_jail(self):
        node = self.position
        while node.name != "Jail / Just Visiting":
            node = node.next
        self.position = node
        self.jailed = True
        self.turns_in_jail = 0
        print(f"{self.name} has been sent to Jail.")

    def buy_property(self):
        node = self.position
        if node.price > 0 and node.owner is None and self.money >= node.price:
            node.owner = self
            self.money -= node.price
            self.properties.append(node)
            print(f"{self.name} bought {node.name} for ${node.price}")
        elif node.owner:
            print(f"{node.name} is already owned by {node.owner.name}.")
        else:
            print(f"{self.name} cannot buy {node.name}.")

    def owns_color_group(self, color, board):
        #Check if the player owns all properties of a given color group.
        if not color:
            return False

        current = board.head
        owned = []
        total = []
        while True:
            if current.color == color:
                total.append(current)
                if current.owner == self:
                    owned.append(current)
            current = current.next
            if current == board.head:
                break

        return len(owned) == len(total) and len(total) > 0
    def get_color_group_properties(self, color, board):
        """Return a list of all properties in a given color group."""
        props = []
        current = board.head
        while True:
            if current.color == color:
                props.append(current)
            current = current.next
            if current == board.head:
                break
        return props

    def can_build_evenly(self, property_node, board):
        """Check if adding a house keeps buildings even across the color group."""
        color = property_node.color
        group = self.get_color_group_properties(color, board)

        # Get only properties owned by this player in that color
        owned = [p for p in group if p.owner == self]
        if len(owned) != len(group):
            return False  # player doesn't own all in group (safety check)

        # Find current number of houses across the group
        house_counts = [p.houses for p in owned]

        # You can only build if no property has *more than one* less than another
        # and you’re not skipping over an uneven build
        return property_node.houses == min(house_counts)

    def buy_house(self, property_node, board):
        """Buy a house if the player owns the full set and builds evenly."""
        if property_node not in self.properties:
            print(f"{self.name} doesn't own {property_node.name}.")
            return
        if not property_node.color:
            print(f"{property_node.name} is not a property you can build on.")
            return
        if property_node.hotel:
            print(f"{property_node.name} already has a hotel.")
            return
        if property_node.houses >= 4:
            print(f"{property_node.name} already has 4 houses.")
            return

        # Check ownership of the whole set
        if not self.owns_color_group(property_node.color, board):
            print(f"{self.name} must own all {property_node.color} properties before building houses.")
            return

        # Check even-building rule
        if not self.can_build_evenly(property_node, board):
            print(f"Houses must be built evenly across all {property_node.color} properties.")
            return

        cost = property_node.house_cost
        if self.money >= cost:
            self.money -= cost
            property_node.houses += 1
            print(
                f"{self.name} built a house on {property_node.name} "
                f"(${cost}). Houses: {property_node.houses}, New rent: ${property_node.rent}"
            )
        else:
            print(f"{self.name} doesn't have enough money for a house.")

    def buy_hotel(self, property_node, board):
        """Buy a hotel only after 4 houses on all properties of the color group."""
        if property_node not in self.properties:
            print(f"{self.name} doesn't own {property_node.name}.")
            return
        if not property_node.color:
            print(f"{property_node.name} is not a property you can build on.")
            return
        if property_node.hotel:
            print(f"{property_node.name} already has a hotel.")
            return

        # Check full ownership
        if not self.owns_color_group(property_node.color, board):
            print(f"{self.name} must own all {property_node.color} properties before building a hotel.")
            return

        # Check that *all* properties have 4 houses before any hotel
        group = self.get_color_group_properties(property_node.color, board)
        for p in group:
            if p.houses < 4 or p.owner != self:
                print(f"All {property_node.color} properties must have 4 houses before building a hotel.")
                return

        cost = property_node.house_cost
        if self.money >= cost:
            self.money -= cost
            property_node.houses = 0
            property_node.hotel = True
            print(
                f"{self.name} built a hotel on {property_node.name} "
                f"(${cost}). New rent: ${property_node.rent}"
            )
        else:
            print(f"{self.name} doesn't have enough money for a hotel.")

    def pay_rent(self, board):
        node = self.position
        owner = node.owner

        if owner is None or owner == self:
            return  # No rent to pay

        # --- Base rent ---
        rent = node.rent

        # --- Scale by houses and hotel ---
        if node.hotel == 1:
            rent *= 5  # roughly Monopoly's scaling for a hotel
        elif node.houses > 0:
            rent *= (1 + node.houses)  # each house adds 100% base rent

        # --- Double rent if owner owns all properties of that color ---
        if node.color:
            # Traverse the circular linked list to collect color_group
            color_group = []
            current = board.head
            while True:
                if current.color == node.color:
                    color_group.append(current)
                current = current.next
                if current == board.head:
                    break
            
            if all(s.owner == owner for s in color_group):
                rent *= 2

        # --- Apply payment ---
        payment = min(self.money, rent)
        self.money -= payment
        owner.money += payment

        print(f"{self.name} paid ${payment} rent to {owner.name} for {node.name} (houses: {node.houses}, hotel: {node.hotel}).")

        if payment < rent:
            print(f"{self.name} couldn't afford full rent and is nearly bankrupt.")

    def display_status(self):
        status = "In Jail" if self.jailed else f"on {self.position.name}"
        print(f"{self.name} is {status} with ${self.money}")