## Estructura del proyecto

- `/src/helpers` - contiene todas las funciones auxiliares que se utilizan en el proyecto 
- `/src/resources` - se guardan todos los archivos procesados que generea el proyecto

## Setup

1. Instalar python2.7

2. Instalar todas las dependencias utilizadas en el proyecto

3. Descargar el archivo `uptu_pasada_variante.csv` de el siguiente enlace:  http://www.montevideo.gub.uy/sites/default/files/datos/uptu_pasada_variante.zip

4. Descargar el archivo `viajes_stm_042022.csv` de el siguiente enlace: https://imnube.montevideo.gub.uy/share/s/THiuXt2vRsCLypFeNaMoIg

## Ejecucion en cluster.uy

Ejecutar el archivo main.py con el siguiente comando `python2.7 main.py CANTIDAD_PROCESOS NOMBRE_USUARIO`
- `CANTIDAD_PROCESOS` es un parámetro que indica la cantidad de proceso a utilizar para procesar la información
- `NOMBRE_USUARIO` es el usuario con el que se ingresa al cluster.uy. 

`Nota:` Se utiliza el espacio temporal alta velocidad como se indica en Consejos y buenas prácticas de uso

### Obtener N paradas con menor diferencia de tiempo teórico y práctico

Ejecutar el archivo buscarDemoraMaximaMinima.py con el siguiente comando `python2.7 buscarDemoraMaximaMinima.py CANTIDAD_PARADAS`
- `CANTIDAD_PARADAS` es un parámetro que indica las N a mostrar

`Nota:` Para ejectura `buscarDemoraMaximaMinima.py` previamente debe ejecutar `main.py`. Además debe renombrar el archivo `resultados_PID.json` a `resultados.json` que se crea en la carpeta `resources`. 

- `PID` es el identificador del proceso master que ejecutó `main.py`