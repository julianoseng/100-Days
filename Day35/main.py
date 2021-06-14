import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACafc5a2afd1a62f9c62e0a19e58f92f70"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 30.4388,
    "lon": -90.4415,
    "appid": api_key,
    "exclude": "currently,minutely,daily",
    "units": "standard"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for hour in data["hourly"][:12]:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today. Bring an umbrella!",
            from_="+12085988651",
            to="+19856028888"
    )

    print(message.status)