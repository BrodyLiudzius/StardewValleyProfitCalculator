import growthBehavior, harvestBehavior
import stardewCalculator.items.seed as sc

# the crop class represents an actual crop that is planted in the ground and growing

class Crop:
    seed:sc.Seed
    growthBehavior:growthBehavior.GrowthBehavior
    harvestBehavior:harvestBehavior.HarvestBehavior

class Crop_Default(Crop):
    growthBehavior:growthBehavior.GrowthBehavior_Default
    harvestBehavior:harvestBehavior.HarvestBehavior_Default

class Crop_Regrowth(Crop):
    growthBehavior:growthBehavior.GrowthBehavior_Regrowth
    harvestBehavior:harvestBehavior.HarvestBehavior_Regrowth

class Crop_GiantCrop(Crop):
    pass