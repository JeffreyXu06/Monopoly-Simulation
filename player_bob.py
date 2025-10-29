from player_base import PlayerBase

class Bob(PlayerBase):
    def __init__(self, start_position):
        super().__init__(
            name="Bob",
            buy_property_rate=0.4,
            buy_house_rate=0.3,
            buy_hotel_rate=0.1
        )
        self.position = start_position