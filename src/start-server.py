# start-server.py

from litcal import fetch_calendar_today
from datetime import date

def main():
    date_today = date.today()
    fetch_calendar_today(date_today)


main()
