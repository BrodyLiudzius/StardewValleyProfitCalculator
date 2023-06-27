class Fertilizer:
    class none:
        level:float = 0
        price:float = 0
    class basic:
        level:float = 1
        price:float = 100
    class quality:
        level:float = 2
        price:float = 150
    class deluxe:
        level:float = 3
        price:float = 0 # unable to calculate price

class RetainingSoil:
    class none:
        price:float = 0
    class basic:
        price:float = 100
    class quality:
        price:float = 150
    class deluxe:
        price:float = 0 # unable to calculate price

class SpeedGro:
    class none:
        rate:float = 0
        price:float = 0
    class basic:
        rate:float = 0.10
        price:float = 100
    class deluxe:
        rate:float = 0.25
        price:float = 150
    class hyper:
        rate:float = 0.33
        price:float = 0 # unable to calculate price