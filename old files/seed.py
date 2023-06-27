from seasons import *
from item import *
from vendor import *

class DropData:
    def __init__(self, _drop:Item, _numDrops:float, _chanceOfMoreDrops:float):
        self.drop = _drop
        self.numDrops = _numDrops
        self.chanceOfMoreDrops = _chanceOfMoreDrops
    
    numDrops:float
    chanceOfMoreDrops:float
    drop:Item

class PriceData:
    def __init__(self, _vendor:Vendor, _price:float):
        self.vendor = _vendor
        self.price = _price
    
    vendor:Vendor
    price:float

class Seed:
    def __init__(self, _prices:list[PriceData], _daysToMature:float, _daysToRegrow:float, _giantCrop:bool, _seasons:list[Season], _drops:list[DropData]):
        self.daysToMature = _daysToMature
        self.daysToRegrow = _daysToRegrow

        self.giantCrop = _giantCrop

        self.seasons = _seasons

        self.drops = _drops

        self.prices = _prices
    
    cropsPerHarvest:int
    chanceOfMoreCrops:float 

    daysToMature:int
    daysToRegrow:int

    giantCrop:bool

    seasons:list[Season]

    prices:list[PriceData]

    drops:list[DropData]

    

    cost:float # Make it a list of cost data (source, cost)
    #crop type -> oil maker, preserves, keg

class Seeds:
    starfruit = Seed([PriceData(Vendors.oasis, 400)], 13, 0, False, [Season.summer], [DropData(Items.starfruit, 1, 0)])

seedsList:list = [member for member in dir(Seeds)]