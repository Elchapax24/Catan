from Board import random_tile

class thief:
    def __init__(self):
        self.location: str = "d19"

    def randomize_location(self) -> str:
        location = random_tile()
        return location
    
    def relocate_thief(self) -> None:
        self.location = self.randomize_location()