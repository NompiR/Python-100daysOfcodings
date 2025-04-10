import requests

parameters = {
    "lat": 34.792973,#12.971599, 51.507351
    "lon": 69.233315,#77.594566, -0.127758
    "appid": "757beb52a0ec7c9a554c2b6d6a08637e",
    "cnt": 4,
}

response_data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response_data.raise_for_status()
data = response_data.json()

will_rain = False
for hourly_data in data["list"]:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")

"""list_zero_weather = data['list'][0]['weather']

if list_zero_weather[0]['id'] < 700:
    print("Bring an Umbrella")"""
#print(data)
