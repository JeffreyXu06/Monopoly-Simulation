class Player:
    def __init__(self, name, start_position, starting_money=1500):
        self.name = name
        self.position = start_position
        self.money = starting_money
        self.properties = []

    def move(self, steps):
        for _ in range(steps):
            self.position = self.position.next

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

    def pay_rent(self):
        node = self.position
        if node.owner and node.owner != self:
            rent = node.rent
            self.money -= rent
            node.owner.money += rent
            print(f"{self.name} paid ${rent} rent to {node.owner.name} for landing on {node.name}.")

    def display_status(self):
        print(f"{self.name} is on {self.position.name} with ${self.money}")