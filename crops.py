from seasons import *

class CropQuality:
    regular:float   = 1.0
    silver:float    = 1.25
    gold:float      = 1.5
    iridium:float  = 2

class Crop:
    def __init__(self, baseValue, seedCost, cropsPerHarvest, chanceOfMoreCrops, daysToMature, regrowth, daysToRegrow):
        self.baseValue = baseValue
        self.seedCost = seedCost
        self.cropsPerHarvest  = cropsPerHarvest
        self.chanceOfMoreCrops = chanceOfMoreCrops
        self.daysToMature = daysToMature
        self.regrowth = regrowth
        self.daysToRegrow = daysToRegrow

    baseValue:float
    seedCost:float
    cropsPerHarvest:int
    chanceOfMoreCrops:float 

    daysToMature:int

    regrowth:bool
    daysToRegrow:int

    giantCrop: bool

    seasons:list[Season]

    isSeed:bool # determines whether tiller applies (i.e. coffee)
    #crop type -> oil maker, preserves, keg


# Crop definitions
class Crops:
    Pumpkin = Crop(320, 100, 1, 0, 13, False, 0)
    SweetGemBerry = Crop(3000, 1000, 1, 0, 24, False, 0) # does not get the tiller profession boost
    StarFruit = Crop(750, 400, 1, 0, 13, False, 0)