import requests
import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # print(response.status_code)
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)


paramaters = {
    "lat": 30.434291353408366,
    "lng": -90.39027976656594,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=paramaters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.datetime.now()
print(time_now.hour)