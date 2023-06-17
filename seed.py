from seasons import *
from item import *

class DropData:
    def __init__(self, _numDrops:float, _chanceOfMoreDrops:float, _drop:Item):
        self.numDrops = _numDrops
        self.chanceOfMoreDrops = _chanceOfMoreDrops
        self.drop = _drop
    numDrops:float
    chanceOfMoreDrops:float
    drop:Item

class Seed:
    def __init__(self, _cost:float, _daysToMature:float, _daysToRegrow:float, _giantCrop:bool, _seasons:list[Season], _drops:list[DropData]):
        self.daysToMature = _daysToMature
        self.daysToRegrow = _daysToRegrow

        self.giantCrop = _giantCrop

        self.seasons = _seasons

        self.drops = _drops

        self.cost = _cost
    
    cropsPerHarvest:int
    chanceOfMoreCrops:float 

    daysToMature:int
    daysToRegrow:int

    giantCrop:bool

    seasons:list[Season]

    drops:list[DropData]

    cost:float # Make it a list of cost data (source, cost)
    #crop type -> oil maker, preserves, keg