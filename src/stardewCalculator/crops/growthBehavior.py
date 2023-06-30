from stardewCalculator.time import Season

#toDo: include crow eating crops

# Growth behavior includes everything before harvest, including time spent as a mature crop

class GrowthBehavior:
    seasons:list[Season]
    daysToMature:float
    
    def Evaluate():
        pass #toDo

class GrowthBehavior_Default(GrowthBehavior):
    def Evaluate():
        pass #toDo

class GrowthBehavior_Regrowth(GrowthBehavior):
    daysToRegrow:float

    def Evaluate():
        pass #toDo

