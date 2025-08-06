# calendar.py

import sys
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
    ordinary = baptism + timedelta(days = 1)
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
    if date >= compute_advent(year - 1) and date < compute_christmas(year - 1):
        return "Advent"
    elif date >= compute_christmas(year - 1) and date <= compute_baptism(year):
        return "Christmas"
    elif date >= compute_ordinary(year) and date < compute_ash_wednesday(year):
        return "Ordinary Time"
    elif date >= compute_ash_wednesday(year) and date < compute_holy_thursday(year):
        return "Lent"
    elif date >= compute_holy_thursday(year) and date < compute_easter(year):
        return "Triduum"
    elif date >= compute_easter(year) and date <= compute_pentecost(year):
        return "Easter"
    elif date > compute_pentecost(year) and date < compute_advent(year):
        return "Ordinary Time"
    else:
        return "unknown season"

# Compute the Sunday cycle (A/B/C)
def compute_sunday_cycle(date):
    year = compute_liturgical_year(date)
    if (year % 3 == 1):
        return "A"
    elif (year % 3 == 2):
        return "B"
    elif (year % 3 == 0):
        return "C"
    else:
        return "unknown sunday cycle"

# Compute the weekday cycle (I/II)
def compute_weekday_cycle(date):
    year = date.year
    if (year % 2 == 1):
        return "I"
    elif (year % 2 == 0):
        return "II"
    else:
        return "unknown weekday cycle"

# Prints a helpful message
def print_help():
    print("this daily-missal-server.\nYou are probably looking for daily-missal-client, but")
    print("that's ok. example use: daily-missal-server 01-06-2025")

# Main
date = date.today()
print(date)
print(compute_liturgical_season(date))
if date.weekday() == 6:
    print(compute_sunday_cycle(date))
else:
    print(compute_weekday_cycle(date))

