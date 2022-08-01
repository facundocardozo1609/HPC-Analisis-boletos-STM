
import bisect
from timeParse import timeParse

def buildJson(parada, json, horariosParadasDf):
  paradaDf = horariosParadasDf.query("cod_ubic_parada == '" + parada + "'")
  list_cod_variante = paradaDf['cod_variante'].unique()
  json[str(parada)] = {}
  for cod_variante in list_cod_variante:
      varianteDf = paradaDf.query("cod_variante == '" + str(cod_variante) + "'")
      list_cod_hora = varianteDf['hora'].unique()
      json[str(parada)][str(cod_variante)] = {}
      json[str(parada)][str(cod_variante)]['horas'] = {'clavesNum': [], 'clavesHora': [],
                                                              'boletos_por_hora': {}}
      for code_hora in list_cod_hora:
          claveNum = json[str(parada)][str(cod_variante)]['horas']['clavesNum']
          code_hora = int(code_hora)

          bisect.insort(claveNum, code_hora)
          json[str(parada)][str(cod_variante)]['horas']['clavesNum'] = claveNum
          indiceHora = json[str(parada)][str(cod_variante)]['horas']['clavesNum'].index(code_hora)
          json[str(parada)][str(cod_variante)]['horas']['clavesHora'].insert(indiceHora, timeParse(str(code_hora)))
          json[str(parada)][str(cod_variante)]['horas']['boletos_por_hora'][timeParse(str(code_hora))] = {'cantidad': 0, 'horaPromedio': "", 'sumaDiferencias': 0,'horasBoletos': []}