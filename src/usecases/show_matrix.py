import pandas as pd

def show_matrix(matriz_transicion):

    for nombre, matriz in matriz_transicion.items():
        print(f"{nombre}:")
        print(pd.DataFrame(matriz)) 
        print("\n")
