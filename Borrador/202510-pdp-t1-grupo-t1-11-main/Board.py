import json
import random
import math
from Tile import Tile
from Port import Port
from PIL import Image, ImageDraw

def random_tile() -> str:
    letters = ["c", "l", "b", "l", "m"]
    numbers = [f"{number:02}" for number in range(1, 20)]
    letter = random.choice(letters)
    location = random.choice(numbers)
    return letter + location

class Board:
    def __init__(self) -> None:
        self.tiles: list[Tile] = []
        self.ports: list[Port] = []

    def load(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for t in data["tiles"]:
                self.tiles.append(Tile(t["id"], t["material"], t["edges"]))
            for p in data["ports"]:
                self.ports.append(Port(p["id"], p["material"]))
    
    def random_map(self):
        self.tiles.append(Tile(id="d19", material="desierto", edges={"top": random_tile, "top-right": random_tile(), "right": random_tile(), "bottom_right": random_tile(), "bottom": random_tile(), "bottom_left": random_tile(), "left": random_tile(), "top_left": random_tile()}))
        # implementar el checkeo de tiles colindantes
        pass

    def validate_map(self):
        if (
            self.tiles.append(Tile(id="d19", material="desierto"))
            and 
            len(self.tiles) == 19
        ):
            pass
        # validar mapa aleatorio e importado
        pass

    def draw_board(self, output_path: str) -> None:
        board_image = Image.new("RGB", (1000, 1000), color="white")
        draw = ImageDraw.Draw(board_image)
        
        hex_size = 60  # Tamaño del hexágono
        hex_height = math.sqrt(3) * hex_size
        hex_width = 2 * hex_size
        center_x, center_y = board_image.size[0] // 2, board_image.size[1] // 2
        
        def hex_corner(center, size, i):
            angle_deg = 60 * i + 30
            angle_rad = math.pi / 180 * angle_deg
            return center[0] + size * math.cos(angle_rad), center[1] + size * math.sin(angle_rad)

        def draw_hexagon(center, size, color):
            corners = [hex_corner(center, size, i) for i in range(6)]
            draw.polygon(corners, outline="black", fill=color)
        
        materials_colors = {
            "desierto": "khaki",
            "madera": "green",
            "ladrillo": "red",
            "oveja": "white",
            "trigo": "yellow",
            "piedra": "gray"
        }

        hex_centers = []
        for row in range(-2, 3):
            for col in range(-2, 3):
                if abs(row + col) <= 2:
                    x = center_x + col * hex_width * 3/4
                    y = center_y + row * hex_height / 2
                    hex_centers.append((x, y))

        for tile, center in zip(self.tiles, hex_centers):
            color = materials_colors.get(tile.material, "gray")
            draw_hexagon(center, hex_size, color)
        
        board_image.save(output_path)
