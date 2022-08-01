import sys
import os

sys.path.insert(0,'./')
from buildJson import buildJson
from calcularHoraPromedio import calcularHoraPromedio
from distribuirBoletos import distribuirBoletos
from log import log

def procesarParada(cola_resultados, cod_paradas_disponibles, horarios_paradas_df, boletos_df, pid):
    dataAsJson = {}
    contador = 0
    while True:
        try:
            parada = cod_paradas_disponibles.get_nowait()
            buildJson(parada=parada, json=dataAsJson, horariosParadasDf=horarios_paradas_df)
            distribuirBoletos(parada=parada, boletosDf=boletos_df, json=dataAsJson)
            calcularHoraPromedio(json=dataAsJson)
            cola_resultados.put_nowait(dataAsJson)
            contador += 1
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log(str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + "Al procesar parada: " + str(contador), pid)
            break