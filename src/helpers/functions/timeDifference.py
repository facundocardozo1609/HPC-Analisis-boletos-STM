from datetime import datetime


def timeDifference(time1, time2):
    # start time and end time
    start_time = datetime.strptime(time1, "%d/%m/%y %H:%M:%S")
    end_time = datetime.strptime(time2, "%d/%m/%y %H:%M:%S")

    # get difference
    delta = end_time - start_time

    return delta.total_seconds()
