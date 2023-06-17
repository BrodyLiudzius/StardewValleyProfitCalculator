#toDo: rename this file to something that includes Time

class Season:
    spring:int = 0
    summer:int = 1
    fall:int   = 2
    winter:int = 3

    days:float = 28

class Time:
    hoursPerDay:float = 20 # 6am to 2am
    minutesPerHour:float = 60
    daysPerSeason:float = 28
    seasonsPerYear:float = 4

    # All time is in units of days since that is most relevant to crops
    minute:float = 1/hoursPerDay/minutesPerHour
    hour:float = 1/hoursPerDay
    day:float = 1
    season:float = daysPerSeason
    year:float = seasonsPerYear
    
