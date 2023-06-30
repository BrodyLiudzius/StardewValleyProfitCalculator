import item
import stardewCalculator.vendors.priceData as sc

class Seed(item.Item):
    def __init__(self, _name: str, _baseValue: float):
        super().__init__(_name, _baseValue)
    
    cropsPerHarvest:int
    chanceOfMoreCrops:float
    
    prices:list[sc.PriceData]