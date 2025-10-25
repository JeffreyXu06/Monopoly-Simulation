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

    def buy_house(self, property_node):
        """Buy a house if you own the property and haven’t reached 4 yet."""
        if property_node not in self.properties:
            print(f"{self.name} doesn't own {property_node.name}.")
            return
        if property_node.hotel:
            print(f"{property_node.name} already has a hotel.")
            return
        if property_node.houses >= 4:
            print(f"{property_node.name} already has 4 houses.")
            return
        house_cost = 50
        if self.money >= house_cost:
            self.money -= house_cost
            property_node.houses += 1
            property_node.update_rent()
            print(f"{self.name} built a house on {property_node.name}. Houses: {property_node.houses}")
        else:
            print(f"{self.name} doesn't have enough money to buy a house.")

    def buy_hotel(self, property_node):
        """Buy a hotel if property has 4 houses."""
        if property_node not in self.properties:
            print(f"{self.name} doesn't own {property_node.name}.")
            return
        if property_node.hotel:
            print(f"{property_node.name} already has a hotel.")
            return
        if property_node.houses < 4:
            print(f"{property_node.name} needs 4 houses before a hotel can be built.")
            return
        hotel_cost = 100
        if self.money >= hotel_cost:
            self.money -= hotel_cost
            property_node.houses = 0
            property_node.hotel = True
            property_node.update_rent()
            print(f"{self.name} built a hotel on {property_node.name}!")
        else:
            print(f"{self.name} doesn't have enough money for a hotel.")

    def pay_rent(self):
        node = self.position
        if node.owner and node.owner != self:
            rent = node.rent
            self.money -= rent
            node.owner.money += rent
            print(f"{self.name} paid ${rent} rent to {node.owner.name} for {node.name}.")

    def display_status(self):
        status = "In Jail" if self.jailed else f"on {self.position.name}"
        print(f"{self.name} is {status} with ${self.money}")