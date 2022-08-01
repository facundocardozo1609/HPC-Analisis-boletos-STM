from datetime import datetime, timedelta


def addSecondsToTime(time, secondsToAdd):
    SPACE = " "
    HOY = datetime.now()
    HOY_STRING = HOY.strftime("%d/%m/%y")

    date = datetime.strptime(HOY_STRING + SPACE + str(time), "%d/%m/%y %H:%M:%S")
    date = date + timedelta(seconds=secondsToAdd)
    dateStr = str(date)

    return dateStr[11 : len(str(dateStr))]
