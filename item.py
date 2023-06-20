class Item:
    def __init__(self, _name:str, _baseValue:float):
        self.name = _name
        self.baseValue = _baseValue
    name:str
    baseValue:float


class Produce(Item):
    pass

class Fruit(Item):
    pass

class Vegetable(Item):
    pass


class Items:
    starfruit = Item("starfruit", 750)


itemList:list = [member for member in dir(Items)]