from Board import Board
class Game:
    def __init__(self, players: list):
        self.players = players
        self.turn = 0
        self.board = Board()

    def get_players(self):
        return self.players
        
    def get_turn(self):
        return self.turn
        

