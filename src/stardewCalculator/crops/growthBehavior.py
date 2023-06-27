from stardewCalculator.time import Season
from giantCrop import GiantCrop

#toDo: include crow eating crops

# Growth behavior includes everything before harvest, including time spent as a mature crop

class GrowthBehavior:
    pass

class GrowthBehavior_Default(GrowthBehavior):
    daysToMature:float
    daysToRegrow:float

    giantCrop:GiantCrop # if left as NoneType, then crop does not grow giant crops

    seasons:list[Season]