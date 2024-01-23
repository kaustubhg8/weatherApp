import requests
import json
import os
city = input("Enter name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=90fb0f6a01c34ff1bcd154036242201&q={city}"

weather = requests.get(url)
# print(weather.text)
# print(type(weather.text))
wdisct = json.loads(weather.text)
# print(type(wdisct))
# print(wdisct["current"]["temp_c"])
command = f'wsay "the temperature in the {city} is {wdisct["current"]["temp_c"]} degree celsius"'
os.system(command)