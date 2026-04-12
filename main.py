from src.ui.interface import startInterface
from utils.update_data import actualizar_csv
import pandas as pd

def obtener_ultimo_resultado():
    df = pd.read_csv('data/data.csv', names=['fecha', 'midday'])
    ultimo_resultado = df['midday'].iloc[0]
    return str(ultimo_resultado)

if __name__ == "__main__":
    actualizar_csv()
    startInterface(obtener_ultimo_resultado())
    print("Programa finalizado")