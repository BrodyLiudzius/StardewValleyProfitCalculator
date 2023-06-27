class CropQuality:
    regular:float   = 1.0
    silver:float    = 1.25
    gold:float      = 1.5
    iridium:float   = 2

class GiantCrop:
    minDrops:float = 15
    maxDrops:float = 21
    quality = CropQuality.regular
    dailyChance:float = 0.01