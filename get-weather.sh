#!/bin/bash

#Define el path al entorno virtual si es necesario
#source /home/josefu/TokyoWeatherReport/env/bin/activate
source /home/josefu/miniforge3/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate iccd332
#Define el path al script de Python
SCRIPT_PATH="/home/josefu/TokyoWeatherReport/main.py"

#Ejecuta el script de Python
python3 "$SCRIPT_PATH"

# si no funciona <chmod +x nombre_del_archivo.sh> para dar permisos de ejecucion