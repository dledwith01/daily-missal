# event.py

class Event:
    def __init__(self, name, date, liturgical_season, color):
        self.name = name
        self.date = date
        self.liturgical_season = liturgical_season
        self.color = color

    def __str__(self):
        return f"{self.date}{self.name}{self.liturgical_season}"
