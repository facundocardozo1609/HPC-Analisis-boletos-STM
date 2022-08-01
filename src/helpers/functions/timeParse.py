def timeParse(stringTime):
    for i in range(4):
        if len(stringTime) == 4:
            break
        stringTime = "0" + stringTime

    time = stringTime[0:2] + ":" + stringTime[2:4] + ":00"
    timeString = str(time)

    return timeString
