from datetime import datetime, timedelta
from timeDifference import timeDifference

def diffBetweenTeoricAndRealTime(horaBus, horaBoleto, mismoDia):
    SPACE = " "
    HOY = datetime.now()
    AYER = HOY - timedelta(days=1)
    HOY_STRING = HOY.strftime("%d/%m/%y")
    AYER_STRING = AYER.strftime("%d/%m/%y")

    fechaBoleto = HOY_STRING + SPACE + str(horaBoleto)

    if mismoDia:
            fechaBoleto = HOY_STRING + SPACE + str(horaBoleto)
            fechaBus = HOY_STRING + SPACE + str(horaBus)
    else:
        if timeDifference(HOY_STRING + SPACE + str(horaBus), HOY_STRING + SPACE + str(horaBoleto)) < 0:
            fechaBoleto = HOY_STRING + SPACE + str(horaBoleto)
            fechaBus = AYER_STRING + SPACE + str(horaBus)
        else:
            fechaBoleto = AYER_STRING + SPACE + str(horaBoleto)
            fechaBus = HOY_STRING + SPACE + str(horaBus)

    return timeDifference(fechaBus, fechaBoleto)
