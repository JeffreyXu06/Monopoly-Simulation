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
                self.money += 200  # Passing GO
                print(f"{self.name} passed GO and collected $200!")
            self.position = self.position.next

        if self.position.name == "Go To Jail":
            print(f"{self.name} landed on Go To Jail!")
            self.go_to_jail()

    def go_to_jail(self):
        # Find Jail space and move player there
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