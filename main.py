#!/usr/bin/python
# -*- coding: utf8 -*-
import multiprocessing as mp
import pandas as pd
import os.path
import json
import sys
import gc
import os

sys.path.insert(0,'./src/helpers/functions')
from procesarParada import procesarParada
from processResults import processResults

from status import status
from log import log

CANT_PROCESOS = int(sys.argv[1])
NOMBRE_USUARIO = sys.argv[2]
CANT_PARADAS = 200
PID = os.getpid()

log("Cargando datos en el sistema...",PID)
my_path = os.path.abspath(os.path.dirname(__file__))

horarios_path = os.path.join(my_path, "src/resources/uptu_pasada_variante.csv")

boletos_path = os.path.join(my_path, "src/resources/viajes_stm_042022.csv")

log("Cargando horarios",PID)

horarios_paradas_df = pd.read_csv(horarios_path,
                            names=["tipo_dia", "cod_variante", "frecuencia", "cod_ubic_parada", "ordinal", "hora",
                                    "dia_anterior"],
                            usecols=["tipo_dia", "cod_variante", "cod_ubic_parada", "hora"],
                            dtype={'tipo_dia': 'str', 'cod_variante': 'str',  'cod_ubic_parada': 'str', "hora": 'str'},
                            sep=";",
                            header=None
                            )

log("Cargando boletos",PID)

boletos_df = pd.read_csv(boletos_path,
                        names=["id_viaje", "con_tarjeta", "fecha_evento", "tipo_viaje", "descripcion_tipo_viaje",
                                "grupo_usuario", "descripcion_grupo_usuario",
                                "grupo_usuario_especifico", "descripcion_grupo_usuario_espe", "ordinal_de_tramo",
                                "cantidad_pasajeros", "codigo_parada_origen",
                                "cod_empresa", "descrip_empresa", "linea_codigo", "dsc_linea", "sevar_codigo"],
                        usecols=["fecha_evento", "sevar_codigo", "codigo_parada_origen"],
                        dtype={'fecha_evento': 'str', 'sevar_codigo': 'str', 'codigo_parada_origen': 'str'},
                        sep=",",
                        header=None
                        )

horarios_paradas_df = horarios_paradas_df.query("tipo_dia == '1'")
cods_ubic_parada = horarios_paradas_df['cod_ubic_parada'].unique()
log("Datos Cargados! \n",PID)

quedanParadas = len(cods_ubic_parada) > 0
paradaInicio = 0
paradaFin = CANT_PARADAS

log("Inicia procesado de boletos ...",PID)
while quedanParadas:
    try:
        paradasParaProcesar = cods_ubic_parada[paradaInicio:paradaFin]
        cod_paradas_disponibles = mp.Manager().Queue()
        cola_resultados = mp.Manager().Queue()
        salteados = mp.Manager().Queue()

        for cod_ubic_para in paradasParaProcesar:
            cod_paradas_disponibles.put(cod_ubic_para)

        #Se asigna cada boleto al horario correspondiente
        log("Procesando boletos ...",PID)
        procesos = []
        for i in range(CANT_PROCESOS):
            procesos.append(
                mp.Process(target=procesarParada, args=(cola_resultados, cod_paradas_disponibles, horarios_paradas_df, boletos_df, PID)))
            procesos[i].start()

        for p in procesos:
            p.join()
        log("Boletos listos!",PID)

        #Se guarda la información de la parada con los boletos asignados
        log("Gurdando resultado...",PID)
        result = {}
        contador = 0
        while True:
            try:
                datosParada = cola_resultados.get_nowait()
                result.update(datosParada)
                contador += 1
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                log(str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + "Intentando obtener parada " + str(contador), PID)
                break


        json_object = json.dumps(result)
        
        path = "/scratch/" + str(NOMBRE_USUARIO) + "/" + str(paradaInicio) + "_" + str(PID) + ".json"
        with open(path, "w") as outfile:
            outfile.write(json_object)
            outfile.close()
        log("Resultado listos! \n",PID)

        paradaInicio = paradaFin
        paradaFin += CANT_PARADAS
        
        status(paradaInicio)

        if(paradaInicio >= len(cods_ubic_parada)):
            quedanParadas = False
            
        #Se libera memoria
        del cola_resultados
        del result
        del json_object
        gc.collect()
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        log(str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno), PID)
    

del boletos_df
del horarios_paradas_df
gc.collect()

processResults(NOMBRE_USUARIO, PID)
