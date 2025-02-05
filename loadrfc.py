import csv
import requests

# Configurar la URL del endpoint
API_URL = "https://tu-api.com/procesar"

# Leer el archivo CSV
def leer_csv(archivo):
    registros = []
    with open(archivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:  # Asegurar que la línea tenga los 3 elementos esperados
                nombre, tipo, clave = row
                registros.append({"nombre": nombre, "tipo": tipo, "clave": clave})
    return registros

# Enviar cada registro al endpoint
def enviar_a_api(registros):
    for registro in registros:
        try:
            response = requests.post(API_URL, json=registro)
            if response.status_code == 200:
                print(f"Enviado: {registro['nombre']} - OK")
            else:
                print(f"Error enviando {registro['nombre']}: {response.status_code}")
        except requests.RequestException as e:
            print(f"Fallo en la conexión: {e}")

# Archivo CSV a procesar
archivo_csv = "datos.csv"

# Ejecutar el flujo
registros = leer_csv(archivo_csv)
enviar_a_api(registros)
