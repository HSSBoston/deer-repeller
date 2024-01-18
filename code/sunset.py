from openweather import *
from datetime import datetime

weatherApiKey = "" 

weatherData = getUsWeather("Bedford", "MA", "imperial", weatherApiKey)
sunsetDt = getSunsetToday(weatherData)
sunsetHr = sunsetDt.hour
sunsetMin = sunsetDt.minute

currentDt = datetime.now()
currentHr = currentDt.hour
currentMin = currentDt.minute
 
print(sunsetHr, sunsetMin)
print(currentHr, currentMin)
