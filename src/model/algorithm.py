import numpy as np
import pandas as pd

def generar_matriz_transicion(path):
    df = pd.read_csv(path, header=None, names=["Fecha", "Numero"], dtype={'Numero': str})
    numeros = df['Numero'].values
    
    matrices = {}
    
    for i in range(3):
        estados = [int(num[i]) for num in numeros]
        
        # Crear frecuencias de cada posicion de la matriz
        frecuencias = np.zeros((10, 10))
        for t in range(len(estados) - 1):
            frecuencias[estados[t]][estados[t+1]] += 1
        
        # Se saca la probabilidad en cada punto
        suma = frecuencias.sum(axis=1, keepdims=True)
        p = np.divide(frecuencias, suma, out=np.zeros_like(frecuencias), where=suma!=0)
        matrices[f"Posicion_{i+1}"] = p
    
    return matrices

if __name__ == "__main__":
    path = "./data/data.csv" 
    resultado_matrices = generar_matriz_transicion(path)
        
    for nombre, matriz in resultado_matrices.items():
        print(f"{nombre}:")
        print(pd.DataFrame(matriz)) 
        print("\n")
            