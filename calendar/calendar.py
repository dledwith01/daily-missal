# calendar.py

from datetime import datetime, timedelta, date

# Meeus/Jones/Butcher algorithm for computing the date for Easter Sunday for a given year
def compute_easter(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = ((19 * a) + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + (2 * e) + (2 * i) - h - k) % 7
    m = (a + (11 * h) + (22 * l)) // 451
    n = (h + l - (7 * m) + 114) // 31
    o = ((h + l - (7 * m) + 114) % 31) + 1
    month = n
    day = o
    easter_sunday = datetime(year, month, day).date()
    return easter_sunday

# Ash Wednesday is 46 days before Easter Sunday
def compute_ash_wednesday(year):
    easter = compute_easter(year)
    ash_wednesday = easter - timedelta(days = 46)
    return ash_wednesday

# Holy Thursday is 3 days before Easter Sunday
def compute_holy_thursday(year):
    easter = compute_easter(year)
    holy_thursday = easter - timedelta(days = 3)
    return holy_thursday

# Pentecost is 49 days after Easter Sunday
def compute_pentecost(year):
    easter = compute_easter(year)
    pentecost = easter + timedelta(days = 49)
    return pentecost

# Christmas
def compute_christmas(year):
    christmas = datetime(year, 12, 25).date()
    return christmas

# Advent begins 4 Sundays before Christmas
def compute_advent(year):
    christmas = compute_christmas(year)
    advent = christmas
    sundays = 0
    while sundays < 4:
        advent -= timedelta(days = 1)
        if advent.weekday() == 6:
            sundays += 1
    return advent

# Epiphany
def compute_epiphany(year):
    epiphany = datetime(year, 1, 6).date()
    return epiphany

# Baptism of the Lord is the Sunday on or after Epiphany
def compute_baptism(year):
    epiphany = compute_epiphany(year)
    baptism = epiphany
    while baptism.weekday() != 6:
        baptism += timedelta(days = 1)
    return baptism

# Ordinary time begins the day after the Baptism of the Lord
def compute_ordinary(year):
    baptism = compute_baptism(year)
    ordinary = baptism + timedelta(days=1)
    return ordinary

# Compute the liturgical year for a given date
def compute_liturgical_year(date):
    advent = compute_advent(date.year)
    if date >= advent:
        return date.year + 1
    else:
        return date.year

# Compute the liturgical season for a given date
def compute_liturgical_season(date):
    year = compute_liturgical_year(date)
    last_year = year - 1
    last_advent = compute_advent(last_year)
    advent = compute_advent(year)
    last_christmas = compute_christmas(last_year)
    christmas = compute_christmas(year)
    baptism = compute_baptism(year)
    ordinary = compute_ordinary(year)
    ash_wednesday = compute_ash_wednesday(year)
    holy_thursday = compute_holy_thursday(year)
    easter = compute_easter(year)
    pentecost = compute_pentecost(year)
    if date >= last_advent and date < last_christmas:
        return "Advent"
    elif date >= last_christmas and date <= baptism:
        return "Christmas"
    elif date >= ordinary and date < ash_wednesday:
        return "Ordinary Time I"
    elif date >= ash_wednesday and date < holy_thursday:
        return "Lent"
    elif date >= holy_thursday and date < easter:
        return "Triduum"
    elif date >= easter and date <= pentecost:
        return "Easter"
    elif date > pentecost and date < advent:
        return "Ordinary Time II"
    else:
        return "Unknown"
    
date = datetime(2025, 1, 1).date()
while date.year < 2026:
    print(date, compute_liturgical_season(date))
    date += timedelta(days=1)

