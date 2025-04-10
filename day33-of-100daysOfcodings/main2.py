import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL= "abcd@gmail.com"
MY_PASSWORD = "123456"

MY_LAT = 22.572645
MY_LNG = 88.363892

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    #Your position is within -5 or +5 degrees of the iss position
    print(MY_LNG - 5)
    print(longitude)
    print(latitude)
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True

def is_night():
    parmeters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params= parmeters)
    response.raise_for_status()
    data = response.json()
    sunrises = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunsets = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunsets or time_now <= sunrises:
        return True

if is_iss_overhead() and is_night():
    print("Look Up: The ISS is above you in the sky.")
else:
    print("Not yet")

"""        
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("Look Up: The ISS is above you in the sky.")
        
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg="Subject: Look UP \n\nThe ISS is above you in the sky."
        )
"""













"""

sunrise_all_time = sunrise.split('T')
sunrise_time = sunrise_all_time[1]
sunrise_split_hour_min_sec = sunrise_time.split(':')
sunrise_h = sunrise_split_hour_min_sec[0]
sunrise_m = sunrise_split_hour_min_sec[1]


# or this way

my_sunrise_time = sunrise.split("T")[1].split(":").split("+")

print(my_sunrise_time)




"""




