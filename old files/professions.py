class Profession:
    pass

class Professions:
    class Agriculturist(Profession):
        rate:float = 0.10 # The rate at which crop growth is sped up by
    class Tiller(Profession):
        value:float = 0.10 # The amount that crop values are increased by
    class Artisan(Profession):
        value:float = 0.40 # The amount that artisan good values are increased by