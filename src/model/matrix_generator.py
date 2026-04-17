import numpy as np
import pandas as pd

def generar_matriz_transicion():
    path = "./data/data.csv"

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
        matrices[f"Digito_{i+1}"] = p
    
    return matrices

def matrix_generator_n_day(matriz_transicion, estado, dias):
    v = np.zeros(10)
    v[int(estado)] = 1

    pi_t = matriz_transicion.T
    
    for _ in range(dias):
        v = np.dot(pi_t, v)
    return v
            
