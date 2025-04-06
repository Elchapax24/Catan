class Player:
    def __init__(self, name: str):
        self.name: str = name

    def input_name(self) -> None:
        name = input("Enter player name: ")
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def print_player_name(self):
        print(f"Player name: {self.name}")