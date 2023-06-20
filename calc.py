import math

from seed import *
from crops import *
from equipment import *
from fertilizer import *
from professions import *


"""

Questions to answer:
- What crop is the most profitable under _any_ circumstances? What are those circumstances?
- What crop is the most valuable within any given season?
- What crop is the most valuable in any given season when you consider inter-season growth?
- When is it more profitable to use a seed maker to get your seeds?
- When is it more profitable to use the seedmaker to turn the crop into seeds and sell them?
- When is fertilizer profitable?
- When is speed-gro profitable?
- What is the most profitable series of crops to plant at the beginning of the game?


#toDo:
- Account for how fertilizer on multi-yield crops with regrowth only affects the first crop of the harvest 
- consider hyper speed gro/deluxe fertilizer prices
- prices considering if the player crafted speed gro/fertilizer/retaining soil
- post processing
- speedGro added after planting
- calculate regroth or growth cycles given seasons and dates
- giant crops

"""



# INPUTS
useSeedMaker:bool = False

numberOfCrops:float = 1
crop:Seed = Seeds.starfruit
growthCycles:float = 1

farmingLevel:float  = 0
professions:list[Profession] = [Professions.Agriculturist]

fertilizer = Fertilizer.none
speedGro = SpeedGro.none
retainingSoil = RetainingSoil.none




# Crop values are based on quality; 1.25, 1.5, 2.0 rounded down to nearest integer number of gold
# As such, the actual value might be closer to 1.24 or 1.48 depending on the crop
# The adjusted values are calculated below
iridiumValue:float = math.floor(crop.baseValue * CropQuality.iridium) / crop.baseValue
goldValue:float = math.floor(crop.baseValue * CropQuality.gold) / crop.baseValue
silverValue:float = math.floor(crop.baseValue * CropQuality.silver) / crop.baseValue
regularValue:float = math.floor(crop.baseValue * CropQuality.regular) /crop.baseValue

gamma = 0.2/10 * farmingLevel + 0.2 * fertilizer.level * (farmingLevel + 2) + 0.01
percentIridum:float = 0 if fertilizer.level < Fertilizer.deluxe.level else gamma / 2
percentGold:float = (1-percentIridum) * gamma
percentSilver:float = (1-percentIridum-percentGold) * min(2*gamma, 0.75)
percentRegular:float = 0 if fertilizer.level >= Fertilizer.deluxe.level else (1-percentIridum-percentGold-percentSilver)

values = [regularValue, silverValue, goldValue, iridiumValue]
percentages = [percentRegular, percentSilver, percentGold, percentIridum]

# if a seed maker is used, then some of the crops generated must be fed back into the seed maker
# starting with the regular quality crops, then silver, gold, iridium until enough for a replant have
# been used up
if useSeedMaker: #toDo: account for not needing to replant
    seedCropNeeded:float = Equipment.SeedMaker.percentHarvestRequired
    for i, p in enumerate(percentages):
        if p >= seedCropNeeded:
            percentages[i] = p - seedCropNeeded
            break
        else:
            seedCropNeeded -= p
            percentages[i] = 0

# The game generates a random number. If the probability to generate more crops is met,
# then another crop is generated and a new probability is checked to see if more extra
# crops are produced. The number of crops generated is calculated using expectation of
# a geometric random variable
extraYield = 0 if crop.chanceOfMoreCrops == 0 else crop.chanceOfMoreCrops / (1 - crop.chanceOfMoreCrops)

revenue:float = crop.cropsPerHarvest * sum(percentages[i]*values[i] for i in range(len(percentages))) # Calculate the base value of a single harvest in units of the crop's base value
revenue += extraYield*values[0] # All extra yields produced by a single crop are of regular quality
revenue *= numberOfCrops*growthCycles*crop.baseValue # multiply by the base value, growthCycles, and number of crops to get the actual value
revenue *= 1 + (Professions.Tiller.value if Professions.Tiller in professions else 0) # Increase by 10% if the tiller profession is taken

#toDo: post processing

soilCost:float = retainingSoil.price + fertilizer.price + speedGro.price
capital:float = soilCost + (0 if useSeedMaker else crop.seedCost*(1 if crop.daysToRegrow > 0 else growthCycles))

maturationTime:float = math.floor(crop.daysToMature * (1 - speedGro.rate - (Professions.Agriculturist.rate if Professions.Agriculturist in professions else 0)))
regrowthTime:float = crop.daysToRegrow * (growthCycles-1)
totalTime:float = maturationTime + regrowthTime if crop.daysToRegrow > 0 else maturationTime*growthCycles

profit:float = revenue - capital
profitPerDay:float = profit/totalTime

print(profit)
print(profitPerDay)