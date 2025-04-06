class Port:
    def __init__ (self, id: str, material: str):
        self.id: str = id
        self.material = material

    def get_id(self) -> str:
        return self.id
    
    def get_material(self) -> str:
        return self.material