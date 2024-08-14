import requests
import csv
import os
from datetime import datetime

# Coordenadas Tokyo
LATITUD = 35.6895
LONGITUD = 139.6917

API_KEY = 'e9372547987c2a71f1b5d221520c0030'

# URL API
URL = f'http://api.openweathermap.org/data/2.5/weather?lat={LATITUD}&lon={LONGITUD}&appid={API_KEY}&units=metric'

# Archivo CSV 
ARCHIVO_CSV = 'clima-tokyo-hoy.csv'

def obtener_datos_climaticos():
    respuesta = requests.get(URL)
    datos = respuesta.json()
    print("Datos Añadidos correctamente")
    print(datos)
    return {
        'fecha_hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperatura': datos['main']['temp'],
        'humedad': datos['main']['humidity'],
        'presion': datos['main']['pressure'],
        'clima': datos['weather'][0]['main'],
        'estado_clima': datos['weather'][0]['description'],
        'ciudad': datos['name'],
        'pais': datos['sys']['country']
    }

def escribir_csv(datos):
    archivo_existe = os.path.isfile(ARCHIVO_CSV)
    
    with open(ARCHIVO_CSV, mode='a', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=datos.keys())
        
        if not archivo_existe:
            escritor.writeheader()
        
        escritor.writerow(datos)

def main():
    datos_climaticos = obtener_datos_climaticos()
    escribir_csv(datos_climaticos)

if __name__ == '__main__':
    main()
