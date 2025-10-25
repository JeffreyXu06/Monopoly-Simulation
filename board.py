class Node:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price
        self.rent = int(price * 0.1) if price > 0 else 0  # Simple rent rule (10% of price)
        self.owner = None
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, price=0):
        new_node = Node(name, price)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def find(self, name):
        current = self.head
        while True:
            if current.name == name:
                return current
            current = current.next
            if current == self.head:
                break
        return None


def create_monopoly_board():
    """Creates a circular Monopoly board with price and rent info."""
    board = CircularLinkedList()
    spaces = [
        ("GO", 0), ("Mediterranean Avenue", 60), ("Community Chest", 0),
        ("Baltic Avenue", 60), ("Income Tax", 0), ("Reading Railroad", 200),
        ("Oriental Avenue", 100), ("Chance", 0), ("Vermont Avenue", 100),
        ("Connecticut Avenue", 120), ("Jail / Just Visiting", 0),
        ("St. Charles Place", 140), ("Electric Company", 150),
        ("States Avenue", 140), ("Virginia Avenue", 160),
        ("Pennsylvania Railroad", 200), ("St. James Place", 180),
        ("Community Chest", 0), ("Tennessee Avenue", 180),
        ("New York Avenue", 200), ("Free Parking", 0),
        ("Kentucky Avenue", 220), ("Chance", 0), ("Indiana Avenue", 220),
        ("Illinois Avenue", 240), ("B&O Railroad", 200),
        ("Atlantic Avenue", 260), ("Ventnor Avenue", 260),
        ("Water Works", 150), ("Marvin Gardens", 280), ("Go To Jail", 0),
        ("Pacific Avenue", 300), ("North Carolina Avenue", 300),
        ("Community Chest", 0), ("Pennsylvania Avenue", 320),
        ("Short Line Railroad", 200), ("Chance", 0),
        ("Park Place", 350), ("Luxury Tax", 0), ("Boardwalk", 400)
    ]
    for name, price in spaces:
        board.append(name, price)
    return board