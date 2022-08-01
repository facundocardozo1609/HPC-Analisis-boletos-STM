
import os
import datetime

my_path = os.path.abspath(os.path.dirname(__file__))

def log(error, pid):
    formato_date = datetime.datetime.strptime(str(datetime.datetime.now())[:19], "%Y-%m-%d %H:%M:%S").time()

    with open('log_' + str(pid) + '.txt', 'a') as outfile:
        outfile.write(str(formato_date) + " " + str(error) + '\n')
        outfile.close()
