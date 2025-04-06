import random
from Board import Board
from PIL import Image, ImageDraw

def titulo_imagen(material):
    try:
        return Image.open(f"images/{material}.png")
    except FileNotFoundError:
        return Image.new("RGB", (100, 100), color="gray")
def generar_tablero(board):
    # Crear una imagen en blanco
    board_image = Image.new("RGB", (800, 800), color="white")
    draw = ImageDraw.Draw(board_image)
    
    for tile in board.tiles:
        tile_image = titulo_imagen(tile.material)
        # Aquí se debe calcular la posición de cada tile basado en su ID o alguna otra lógica.
        # Por simplicidad, vamos a posicionarlos aleatoriamente.
        x, y = random.randint(0, 700), random.randint(0, 700)
        board_image.paste(tile_image, (x, y))
    
    # Dibujar los ports
    for port in board.ports:
        port_image = titulo_imagen(port.material)
        # Aquí se debe calcular la posición de cada port basado en su ID o alguna otra lógica.
        # Por simplicidad, vamos a posicionarlos aleatoriamente.
        x, y = random.randint(0, 700), random.randint(0, 700)
        board_image.paste(port_image, (x, y))
    
    return board_image

board = Board()
board.load("board_config.json")

board_image = generar_tablero(board)
board_image.show()
