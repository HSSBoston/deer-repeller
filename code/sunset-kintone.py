from openweather import *
from datetime import datetime
import time, explorerhat as hat

weatherApiKey = "" 
sdomain = "jxsboston"
appId = "22"
token = ""

def turnOnPump():
    hat.output.one.on()
    time.sleep(10)
    hat.output.one.off()

while True:
    try:
        weatherData = getUsWeather("Bedford", "MA", "imperial", weatherApiKey)
        sunsetDt = getSunsetToday(weatherData)
        sunsetHr = sunsetDt.hour
        sunsetMin = sunsetDt.minute

        currentDt = datetime.now()
        currentHr = currentDt.hour
        currentMin = currentDt.minute
         
        print(sunsetHr, sunsetMin)
        print(currentHr, currentMin)

        record = kintone.getRecord(subDomain=sdomain,
                                   apiToken=token,
                                   appId=appId,
                                   recordId="1")
        onNow = record["on_now"]["value"]
        schedule = record["schedule"]["value"]
        scheduledTime = record["scheduledTime"]["value"]
        time = record["time"]["value"]
        
        if onNow == "Yes":
            turnOnPump()
        
        if scheduledTime == "Sunset time":
            if currentHr == sunsetHr and currentMin == sunsetMin:
                turnOnPump()
        
        if scheduledTime == "Another time":
            turnOnPump()

        time.sleep(60)

    except: KeyboardInterrupt:
        
