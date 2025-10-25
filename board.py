class Node:
    def __init__(self, name, price=0, rent=0):
        self.name = name
        self.price = price
        self.base_rent = rent
        self.rent = rent
        self.owner = None
        self.houses = 0
        self.hotel = False
        self.next = None

    def update_rent(self):
        """Update rent based on number of houses/hotel."""
        if self.hotel:
            self.rent = self.base_rent * 5
        else:
            self.rent = self.base_rent * (1 + self.houses)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, price=0, rent=0):
        new_node = Node(name, price, rent)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        current = self.head
        if not current:
            return
        while True:
            owner_name = current.owner.name if current.owner else "None"
            print(
                f"{current.name} | Price: {current.price} | Rent: {current.rent} | "
                f"Houses: {current.houses} | Hotel: {current.hotel} | Owner: {owner_name}"
            )
            current = current.next
            if current == self.head:
                break