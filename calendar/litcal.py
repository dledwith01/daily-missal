import requests
from parser import handle_json
from datetime import datetime, date

date = date.today()

url = "https://litcal.johnromanodorazio.com/api/dev/calendar/nation/US?year_type=CIVIL"
headers = {
  "accept": "application/json",
  "Accept-Language": "en_US"
}

response = requests.request("GET", url, headers=headers)
data = response.json()
handle_json(date, data)
