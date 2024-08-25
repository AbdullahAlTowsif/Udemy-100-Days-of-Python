# ISS API
# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# # print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

# Sunrise Sunset API

import requests

MY_LAT = 44.061169
MY_LNG = 15.015290

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]

ss = (sunrise_time, sunset_time)
print(ss)





"""
Q: What is API?
=> An Application Programming Interface (API) is a set of commands, function,
protocols, and objects that programmers can use to create software or interact
with an external system.

HTTP Status Codes
=================
Link: https://www.webfx.com/web-development/glossary/http-status-codes/

1XX: Hold On
2XX: Here You Go
3XX: Go Away
4XX: You Screwed Up
5XX: I Screwed Up

"""

