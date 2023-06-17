from seasons import * 

class Equipment:
    class SeedMaker:
        time:float = 20 * Time.minute

        probabilityOfProducing:float = 0.9751
        averageSeedsProduced:float = 2
        # For clarity's sake, the calculation is written out rather than just having a constant
        percentHarvestRequired:float = 1/(probabilityOfProducing*averageSeedsProduced)

    class PreservesBarrel:
        pass
    
    class Keg:
        pass
    
    class Cask:
        pass
    
    class OilMaker:
        pass