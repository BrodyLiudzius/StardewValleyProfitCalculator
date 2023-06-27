import produce

class Fruit(produce.Produce):
    def __init__(self, _name: str, _baseValue: float):
        super().__init__(_name, _baseValue)