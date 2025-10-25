class Node:
    def __init__(self, name, price=0, rent_values=None, color=None, house_cost=0):
        self.name = name
        self.price = price
        self.color = color
        self.house_cost = house_cost
        self.rent_values = rent_values or [0, 0, 0, 0, 0, 0]
        self.houses = 0
        self.hotel = False
        self.owner = None
        self.next = None

    @property
    def rent(self):
        if self.hotel:
            return self.rent_values[5]
        return self.rent_values[self.houses]

    def __repr__(self):
        return (
            f"{self.name} | {self.color or 'N/A'} | Price: {self.price} | "
            f"Rent: {self.rent} | Houses: {self.houses} | Hotel: {self.hotel} | "
            f"Owner: {self.owner.name if self.owner else 'None'}"
        )


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, price=0, rent_values=None, color=None, house_cost=0):
        new_node = Node(name, price, rent_values, color, house_cost)
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
            print(current)
            current = current.next
            if current == self.head:
                break


def create_monopoly_board():
    board = LinkedList()

    # Color-based building costs
    COST = {
        "Brown": 50,
        "Light Blue": 50,
        "Pink": 100,
        "Orange": 100,
        "Red": 150,
        "Yellow": 150,
        "Green": 200,
        "Dark Blue": 200,
    }

    spaces = [
        ("GO", 0, [0, 0, 0, 0, 0, 0], None),
        ("Mediterranean Avenue", 60, [2, 10, 30, 90, 160, 250], "Brown"),
        ("Community Chest", 0, [0, 0, 0, 0, 0, 0], None),
        ("Baltic Avenue", 60, [4, 20, 60, 180, 320, 450], "Brown"),
        ("Income Tax", 0, [0, 0, 0, 0, 0, 0], None),
        ("Reading Railroad", 200, [25, 50, 100, 200, 200, 200], None),
        ("Oriental Avenue", 100, [6, 30, 90, 270, 400, 550], "Light Blue"),
        ("Chance", 0, [0, 0, 0, 0, 0, 0], None),
        ("Vermont Avenue", 100, [6, 30, 90, 270, 400, 550], "Light Blue"),
        ("Connecticut Avenue", 120, [8, 40, 100, 300, 450, 600], "Light Blue"),
        ("Jail / Just Visiting", 0, [0, 0, 0, 0, 0, 0], None),
        ("St. Charles Place", 140, [10, 50, 150, 450, 625, 750], "Pink"),
        ("Electric Company", 150, [0, 0, 0, 0, 0, 0], None),
        ("States Avenue", 140, [10, 50, 150, 450, 625, 750], "Pink"),
        ("Virginia Avenue", 160, [12, 60, 180, 500, 700, 900], "Pink"),
        ("St. James Place", 180, [14, 70, 200, 550, 750, 950], "Orange"),
        ("Tennessee Avenue", 180, [14, 70, 200, 550, 750, 950], "Orange"),
        ("New York Avenue", 200, [16, 80, 220, 600, 800, 1000], "Orange"),
        ("Free Parking", 0, [0, 0, 0, 0, 0, 0], None),
        ("Kentucky Avenue", 220, [18, 90, 250, 700, 875, 1050], "Red"),
        ("Indiana Avenue", 220, [18, 90, 250, 700, 875, 1050], "Red"),
        ("Illinois Avenue", 240, [20, 100, 300, 750, 925, 1100], "Red"),
        ("B. & O. Railroad", 200, [25, 50, 100, 200, 200, 200], None),
        ("Atlantic Avenue", 260, [22, 110, 330, 800, 975, 1150], "Yellow"),
        ("Ventnor Avenue", 260, [22, 110, 330, 800, 975, 1150], "Yellow"),
        ("Water Works", 150, [0, 0, 0, 0, 0, 0], None),
        ("Marvin Gardens", 280, [24, 120, 360, 850, 1025, 1200], "Yellow"),
        ("Go To Jail", 0, [0, 0, 0, 0, 0, 0], None),
        ("Pacific Avenue", 300, [26, 130, 390, 900, 1100, 1275], "Green"),
        ("North Carolina Avenue", 300, [26, 130, 390, 900, 1100, 1275], "Green"),
        ("Pennsylvania Avenue", 320, [28, 150, 450, 1000, 1200, 1400], "Green"),
        ("Short Line Railroad", 200, [25, 50, 100, 200, 200, 200], None),
        ("Park Place", 350, [35, 175, 500, 1100, 1300, 1500], "Dark Blue"),
        ("Boardwalk", 400, [50, 200, 600, 1400, 1700, 2000], "Dark Blue"),
    ]

    for name, price, rents, color in spaces:
        board.append(name, price, rents, color, COST.get(color, 0))

    return board