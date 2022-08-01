from datetime import datetime
from diffBetweenTeoricAndRealTime import diffBetweenTeoricAndRealTime
from getPrevAndNextTime import getPrevAndNextTime
import sys

def distribuirBoletos(parada, json, boletosDf):
    paradaStr = "'" + parada + "'"
    boletos_de_parada = boletosDf.query("codigo_parada_origen == " + paradaStr)

    for row in boletos_de_parada.itertuples():
        cod_parada = row.codigo_parada_origen
        cod_variante = row.sevar_codigo
        fecha_evento = row.fecha_evento
        formato_date = datetime.strptime(str(fecha_evento)[:19], "%Y-%m-%dT%H:%M:%S")

        if (formato_date.weekday() > 4):
            continue

        try:
            if (not (str(cod_parada) in json) or not str(cod_variante) in json[str(cod_parada)]):
                continue

            hora_boleto = formato_date.time()  # 15:03:21
            cod_horas_variante = json[str(cod_parada)][str(cod_variante)]['horas']['clavesHora']
            prevAndNextTime = getPrevAndNextTime(cod_horas_variante, hora_boleto)
            hora_bus = prevAndNextTime[0]
            dataHora = json[str(cod_parada)][str(cod_variante)]['horas']['boletos_por_hora'][
                str(hora_bus)]
            dataHora['cantidad'] += 1
            dataHora['horasBoletos'].append(str(hora_boleto))
            dataHora['sumaDiferencias'] += diffBetweenTeoricAndRealTime(hora_bus, hora_boleto,
                                                                        prevAndNextTime[1])

        except:
            e = sys.exc_info()[0]
            print(e)
            continue
    