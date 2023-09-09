from openweather import *
from datetime import datetime

weatherApiKey = "1e8916214f329eb63fe4956810360e09" 

weatherData = getUsWeather("Bedford", "MA", "imperial", weatherApiKey)
sunsetDt = getSunsetToday(weatherData)
sunsetHr = sunsetDt.hour
sunsetMin = sunsetDt.minute

currentDt = datetime.now()
currentHr = currentDt.hour
currentMin = currentDt.minute
 
print(sunsetHr, sunsetMin)
print(currentHr, currentMin)
