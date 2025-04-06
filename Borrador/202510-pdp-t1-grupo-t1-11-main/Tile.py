class Tile:
    def __init__(self, id: str, material: str, edges: dict):
        self.id: str = id
        self.material: str = material
        self.edges: dict[str: str] = edges  

    def get_id(self) -> str:
        return self.id
    def get_material(self) -> str:
        return self.material
    def get_edges(self) -> dict:
        return self.edges