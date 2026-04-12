import requests
import pandas as pd
from datetime import datetime, date
import os
import json
import sys

path = "../data/data.csv"
url = "https://data.ny.gov/resource/n4w8-wxte.json"

#Obtener la ultima fecha del CSV
def obtener_ultima_fecha_csv():
    
    if not os.path.exists(path):
        return None
    
    try:
        df = pd.read_csv(path, header=None, names=['fecha', 'midday'])
        if len(df) == 0:
            return None
        
        df['fecha_dt'] = pd.to_datetime(df['fecha'], format='%m/%d/%Y')
        ultima_fecha = df['fecha_dt'].max()
        print(f"Ultima fecha en el CSV:{ultima_fecha}")
        return ultima_fecha

    except Exception as e:
        print(f"Error al leer fecha del CSV: {e}")
        return None

#Descargar los números de la lotería de "https://data.ny.gov/w/n4w8-wxte/caer-yrtv?cur=y8pA_2CK7FK" 
def descargar_datos_ny():
    params = {
        "$limit": 10000,
        "$order": "draw_date DESC"
    }
    
    fecha_desde = obtener_ultima_fecha_csv()
    hoy = date.today()
    hoy = hoy.strftime('%m/%d/%Y')
    
    if str(fecha_desde) == hoy:
        print("Datos al día")
        return None
    
    if fecha_desde:
        print("Ultima fecha existente")
        fecha_formateada = fecha_desde.strftime('%Y-%m-%d')
        params["$where"] = f"draw_date >= '{fecha_formateada}'"
        print(f"Filtrando datos desde: {fecha_desde.strftime('%m/%d/%Y')}")
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        print(f"{len(data)} registros descargados con exito")
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar datos: {e}")
        sys.exit(1)

#Formatea los datos antes de generar permanencia en data/data.csv
def procesar_datos():
    
    data = descargar_datos_ny()
    
    if not data:
        return None
    
    registros = []
    
    for item in data:
        draw_date = item.get('draw_date', '')
        midday = item.get('midday_daily', '')
            
        if draw_date and midday:
            fecha = datetime.strptime(draw_date[:10], '%Y-%m-%d')
            fecha_formateada = fecha.strftime('%m/%d/%Y')
                
            registros.append({
                'fecha': fecha_formateada,
                'midday': midday
            })
        
    df = pd.DataFrame(registros)
    
    df['fecha_sort'] = pd.to_datetime(df['fecha'], format='%m/%d/%Y')
    df.sort_values('fecha_sort', ascending=False)
    df = df.drop('fecha_sort', axis=1)
    
    print("Datos formateados")
    return df

#Actualizar el archivo
def actualizar_csv():
    print("Actualizando archivo CSV...")
    
    df = procesar_datos()
    
    if os.path.exists(path):
        df_existente = pd.read_csv(path, header=None, names=['fecha', 'midday'])
        print(f"Cantidad de registros existentes: {len(df_existente)}")
        
        df_combinado = pd.concat([df_existente, df], ignore_index=True)
        df_combinado = df_combinado.drop_duplicates(subset='fecha', keep='last')
        
        df_combinado['fecha_sort'] = pd.to_datetime(df_combinado['fecha'], format='%m/%d/%Y')
        df_combinado = df_combinado.sort_values('fecha_sort', ascending=False)
        df_combinado = df_combinado.drop('fecha_sort', axis=1)

    else:
        df_combinado = df
        
    df_combinado.to_csv(path, index=False, header=False)
    print("Archivo actualizado correctamente")
    
    print("\nÚltimos 5 registros:")
    print(df_combinado.head().to_string(index=False, header=False))
        
def main():
    actualizar_csv()

if __name__ == "__main__":
    main()
