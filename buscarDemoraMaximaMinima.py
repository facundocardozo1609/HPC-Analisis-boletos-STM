import bisect
import os
import json
import sys

class ClaseParada:
    def __init__(self):
        self.parada = 0
        self.variante = 0
        self.horaTeorica = ""
        self.horaPromedio = ""

CANTIDAD_PARADAS = int(sys.argv[1])

def buscarDemoraMaximaMinima(cantidad_paradas):
    my_path = os.path.abspath(os.path.dirname(__file__))
    result_path = my_path + "/src/resources/resultado.json"
    with open(result_path, "r") as outfile:
        resultado = json.load(outfile)

    diferenciaPositivas = []
    paradasInfoPositvas = []
    diferenciaNegativas = []
    paradasInfoNegativas = []
            
    for parada in resultado:
        for variante in resultado[parada]:
            for horarioTeorico in resultado[parada][variante]["horas"]["boletos_por_hora"]:
                horario = resultado[parada][variante]["horas"]["boletos_por_hora"][horarioTeorico]
                if horario["cantidad"] > 10:
                    sumaDiferenciasPromedio = horario["sumaDiferencias"]/horario["cantidad"]
                    
                    p = ClaseParada()
                    p.parada = parada
                    p.variante = variante
                    p.horaTeorica = horarioTeorico
                    p.horaPromedio = horario["horaPromedio"]
                                        
                    if sumaDiferenciasPromedio >= 0: 
                        index = bisect.bisect(diferenciaPositivas, sumaDiferenciasPromedio)
                        diferenciaPositivas.insert(index, sumaDiferenciasPromedio)
                        paradasInfoPositvas.insert(index, p)
                        continue
                    elif sumaDiferenciasPromedio < 0:
                        index = bisect.bisect(diferenciaNegativas, sumaDiferenciasPromedio)
                        diferenciaNegativas.insert(index, sumaDiferenciasPromedio)
                        paradasInfoNegativas.insert(index, p)
                        continue

    with open(my_path + '/src/resources/top_' + str(CANTIDAD_PARADAS) + '_diferencia_tiempo_paradas.txt', 'a') as outfile:
        for i in paradasInfoPositvas[:CANTIDAD_PARADAS]:
            outfile.write("Teorico " + i.horaTeorica + " - Practico " + i.horaPromedio + " - Parada: " + str(i.parada) + " - Variante " + str(i.variante) + '\n')
        outfile.write('\n\n')
        for i in paradasInfoNegativas[-CANTIDAD_PARADAS:]:
            outfile.write("Teorico " + i.horaTeorica + " - Practico " + i.horaPromedio + " - Parada: " + str(i.parada) + " - Variante " + str(i.variante) + '\n') 
        outfile.close() 

buscarDemoraMaximaMinima(CANTIDAD_PARADAS)


