from openweather import *
from datetime import datetime
import kintone, time
# import explorerhat as hat

weatherApiKey = ""
sdomain = ""
appId = ""
token = ""
zipCode = ""
countryCode = ""

def turnOnPump(duration):
    print("!")
#     hat.output.one.on()
#     hat.output.two.on()
#     time.sleep(duration)
#     hat.output.one.off()
#     hat.output.two.off()
    
def getWeekDay(currentDt):
    daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return daysOfWeek[currentDt.weekday()]
    
while True:
    try:
        weatherData = getZipWeather(zipCode, countryCode, "imperial", weatherApiKey)
        sunsetDt = getSunsetToday(weatherData)
        sunsetHr = sunsetDt.hour
        sunsetMin = sunsetDt.minute

        currentDt = datetime.now()
        currentHr = currentDt.hour
        currentMin = currentDt.minute
        currentWkDay = getWeekDay(currentDt)
 
        record = kintone.getRecord(subDomain=sdomain,
                                   apiToken=token,
                                   appId=appId,
                                   recordId="1")
        onNow = record["onNow"]["value"]
        weeklySchedule = record["weeklySchedule"]["value"]
        onSchedule = record["onSchedule"]["value"]
        scheduledTime = record["scheduledTime"]["value"]
        duration = int(record["duration"]["value"])
        
        if onNow == "Yes":
            turnOnPump(duration)
        elif currentWkDay in weeklySchedule:
            if "Sunset time" in onSchedule:
                if (currentHr == sunsetHr and
                    currentMin == sunsetMin):
                    turnOnPump(duration)        
            if "Another time" in onSchedule:
                schedTime = scheduledTime.split(":")
                schedHr = schedTime[0]
                schedMin = schedTime[1]
                if currentHr == schedHr and currentMin == schedMin:
                    turnOnPump(duration)
        time.sleep(60)
    except KeyboardInterrupt:
        break
