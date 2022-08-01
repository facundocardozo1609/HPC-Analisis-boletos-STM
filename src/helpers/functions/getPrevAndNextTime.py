from datetime import datetime, timedelta
from timeDifference import timeDifference

SPACE = " "
HOY = datetime.now()
AYER = HOY - timedelta(days=1)
HOY_STRING = HOY.strftime("%d/%m/%y")
AYER_STRING = AYER.strftime("%d/%m/%y")

def getPrevAndNextTime(arrayTime, time):
    nextTime = ""
    prevTime = ""
    fechaBoleto = ""
    existeHoraMayor = False

    for i in range(len(arrayTime) - 1):
        if (
            timeDifference(
                HOY_STRING + SPACE + str(arrayTime[i]), HOY_STRING + SPACE + str(time)
            )
            < 0
        ):
            nextTime = HOY_STRING + SPACE + arrayTime[i]
            nextTimeDay = HOY_STRING
            if i == 0:
                fechaBoleto = HOY_STRING
                prevTime = AYER_STRING + SPACE + arrayTime[len(arrayTime) - 1]
                prevTimeDay = AYER_STRING
                existeHoraMayor = True

            else:
                fechaBoleto = HOY_STRING
                prevTime = HOY_STRING + SPACE + arrayTime[i - 1]
                prevTimeDay = HOY_STRING
                existeHoraMayor = True
            break

    if existeHoraMayor == False:
        fechaBoleto = AYER_STRING
        prevTime = AYER_STRING + SPACE + arrayTime[len(arrayTime) - 1]
        prevTimeDay = AYER_STRING
        nextTime = HOY_STRING + SPACE + arrayTime[0]
        nextTimeDay = HOY_STRING

    diferencia = timeDifference(prevTime, nextTime)

    if timeDifference(prevTime, fechaBoleto + SPACE + str(time)) <= diferencia * 0.8:
        horaAsignada = prevTime
        mismoDia = fechaBoleto == prevTimeDay
    else:
        horaAsignada = nextTime
        mismoDia = fechaBoleto == nextTimeDay

    return [horaAsignada[9 : len(horaAsignada)], mismoDia]
