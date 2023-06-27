import item

class Produce(item.Item):
    def __init__(self, _name: str, _baseValue: float):
        super().__init__(_name, _baseValue)
