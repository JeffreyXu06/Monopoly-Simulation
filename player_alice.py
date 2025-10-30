from player_base import PlayerBase

class Alice(PlayerBase):
    def __init__(self, start_position):
        super().__init__(
            name="Alice",
            buy_property_rate=0.5,
            buy_house_rate=0.2,
            buy_hotel_rate=0.05,
            min_cash_reserve=650  # Alice is cautious
        )
        self.position = start_position