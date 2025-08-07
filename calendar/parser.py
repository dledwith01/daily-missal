import json
import pprint
from datetime import datetime
import time
import calendar
import shutil

RESET_COLOR = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
BOLD = "\033[1m"

WIDTH = shutil.get_terminal_size().columns

def handle_json(date, data):
    unix_time = calendar.timegm(date.timetuple())
    date = datetime.utcfromtimestamp(unix_time)
    long_date = date.strftime("%A, %B, %d, %Y")
    events = data.get("litcal", [])

    today_events = [
        event for event in events
        if event.get("date") == unix_time
    ]

    if not today_events:
        print("No Events Found")
    else:
        for event in today_events:
            name = event.get("name")
            color_array = event.get("color")
            color = color_array[0]
            liturgical_year = event.get("liturgical_year")
            liturgical_season = event.get("liturgical_season")
            isVigil = event.get("is_vigil_mass", False)
            title_out = str(BOLD + long_date + " - " + name + " - " + liturgical_season)
            print(title_out.ljust(WIDTH))
            print(RESET_COLOR + "Readings: \n\n\n")
