import vendor

class PriceData:
    def __init__(self, _vendor:vendor.Vendor, _price:float, _availableAfter:float = 0):
        self.vendor = _vendor
        self.price = _price
        self.availableAfter = _availableAfter
    
    vendor:vendor.Vendor
    price:float
    availableAfter:float # Some crops are only available after year 1