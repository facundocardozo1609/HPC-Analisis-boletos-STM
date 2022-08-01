
import os
import psutil
import datetime

my_path = os.path.abspath(os.path.dirname(__file__))

def status(parada):
    freeMemoryPercentage = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_info()[0]/2.**30 

    formato_date = datetime.datetime.strptime(str(datetime.datetime.now())[:19], "%Y-%m-%d %H:%M:%S").time()
    print(str(formato_date) + ", Paradas procesadas: " + str(parada) + ", Memoria usada: " + str(memoryUse) + "GB, Memoria libre: "+ str(freeMemoryPercentage)  + '%')
