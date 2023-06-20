class Vendor:
    pass


class Vendors:
    jojaMart:Vendor
    oasis:Vendor
    travelingCart:Vendor


vendorsList:list = [member for member in dir(Vendors)]
