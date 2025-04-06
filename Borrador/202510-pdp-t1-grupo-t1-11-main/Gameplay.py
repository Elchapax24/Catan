class gameplay:
    def __init__(self, player):
        self.player = player
        self.winner = None

    def start_game(self):
        print("Game started!")
        self.game_state = "running"

    

    def end_game(self):
        self.game_state = "game_over"
        print("Game over!")