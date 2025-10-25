
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

def create_monopoly_board():
    board = LinkedList()
    spaces = [
        ("GO", 0, 0),
        ("Mediterranean Avenue", 60, 2),
        ("Community Chest", 0, 0),
        ("Baltic Avenue", 60, 4),
        ("Income Tax", 0, 0),
        ("Reading Railroad", 200, 25),
        ("Oriental Avenue", 100, 6),
        ("Chance", 0, 0),
        ("Vermont Avenue", 100, 6),
        ("Connecticut Avenue", 120, 8),
        ("Jail / Just Visiting", 0, 0),
        ("St. Charles Place", 140, 10),
        ("Electric Company", 150, 0),
        ("States Avenue", 140, 10),
        ("Virginia Avenue", 160, 12),
        ("St. James Place", 180, 14),
        ("Tennessee Avenue", 180, 14),
        ("New York Avenue", 200, 16),
        ("Free Parking", 0, 0),
        ("Kentucky Avenue", 220, 18),
        ("Indiana Avenue", 220, 18),
        ("Illinois Avenue", 240, 20),
        ("B. & O. Railroad", 200, 25),
        ("Atlantic Avenue", 260, 22),
        ("Ventnor Avenue", 260, 22),
        ("Water Works", 150, 0),
        ("Marvin Gardens", 280, 24),
        ("Go To Jail", 0, 0),
        ("Pacific Avenue", 300, 26),
        ("North Carolina Avenue", 300, 26),
        ("Pennsylvania Avenue", 320, 28),
        ("Short Line Railroad", 200, 25),
        ("Boardwalk", 400, 50)
    ]

    for name, price, rent in spaces:
        board.append(name, price, rent)

    return board