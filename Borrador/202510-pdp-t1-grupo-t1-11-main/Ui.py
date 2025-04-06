from rich.console import Console, print
from PIL import Image
from Board import Board
from Gameplay import gameplay

class Ui:
    def __init__ (self):
        self.show = Console()

    def Show_board(self, board: Board):
        #Muestra el tablero
        self.print("Hola")

    def show_winner(self, winner: str):
        #Muestra el ganador
        self.print(f"El ganador es {gameplay.winner}")