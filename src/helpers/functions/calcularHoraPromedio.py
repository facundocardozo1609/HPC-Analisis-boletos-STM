from addSecondsToTime import addSecondsToTime

def calcularHoraPromedio(json):
  for cod_parada in json:
    variantes = json[cod_parada]
    for cod_variante in variantes:
        horas = json[str(cod_parada)][str(cod_variante)]['horas']['boletos_por_hora']

        for cod_hora in horas:
            hora = json[str(cod_parada)][str(cod_variante)]['horas']['boletos_por_hora'][cod_hora]
            cantidadBoletos = hora["cantidad"]
            if (cantidadBoletos == 0):
                continue
            diferenciaTotal = hora["sumaDiferencias"]
            segundosPromedio = diferenciaTotal / cantidadBoletos
            hora["horaPromedio"] = addSecondsToTime(cod_hora, segundosPromedio)
            json[str(cod_parada)][str(cod_variante)]['horas']['boletos_por_hora'][cod_hora] = hora