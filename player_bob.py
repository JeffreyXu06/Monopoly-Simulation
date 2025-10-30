from player_base import PlayerBase

class Bob(PlayerBase):
    def __init__(self, start_position):
        super().__init__(
            name="Bob",
            buy_property_rate=0.7,
            buy_house_rate=0.3,
            buy_hotel_rate=0.1,
            min_cash_reserve=450  # Bob is more aggressive
        )
        self.position = start_position