import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "60fa7768bcf910b4d109bf9ac6a122ee"

weather_params = {
    "lat": 22.356852,
    "lon": 91.783180,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["weather"]:
    condition_code = hour_data["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")
else:
    print("Don't need")