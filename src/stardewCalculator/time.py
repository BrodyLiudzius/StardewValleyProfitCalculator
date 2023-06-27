# All time is in units of days since days are most relevant to crops

class Season:
    seasonList:list
    def __init__(self, _duration:float, _name:str):
        self.duration = _duration
        Season.seasonList.append(self)
    name:str
    duration:float


spring:Season = Season(28, "Spring")
summer:Season = Season(28, "Summer")
fall:Season   = Season(28, "Fall")
winter:Season = Season(28, "Winter")


__HOURS_PER_DAY:float = 20 # 6am to 2am
__MINUTES_PER_HOUR:float = 60


minute:float = 1/__HOURS_PER_DAY/__MINUTES_PER_HOUR
hour:float = 1/__HOURS_PER_DAY
day:float = 1
year:float = sum([season.duration for season in Season.seasonList])
