import pandas as pd
import numpy as np
from scipy.stats import chisquare
from statsmodels.tsa.stattools import acf 

def validation(path):
    df = pd.read_csv(path, header=None, names=["Fecha", "Numero"])
    v = df['Numero'].astype(int).values
    n = len(v)

    # 2. Chi-Cuadrado (Uniformidad)
    f, _ = np.histogram(v, bins=10, range=(0, 1000))
    _, p_chi = chisquare(f)

    # 3. Test de Poker (Estructura)
    pk = [len(set(f"{int(x):03}")) for x in v]
    cnt = [pk.count(3), pk.count(2), pk.count(1)]
    _, p_pok = chisquare(cnt, f_exp=[n*0.72, n*0.27, n*0.01])

    # 4. Autocorrelación (Independencia) - (+-0.027)
    res_acf = acf(v, nlags=30, fft=False)

    print(f"P-valor Chi: {p_chi:.4f} (Ideal > 0.05)")
    print(f"P-valor Poker: {p_pok:.4f} (Ideal > 0.05)")
    print(f"Autocorrelación: {res_acf[1:].round(3)}") 


if __name__ == "__main__":
    archivo = './data/data.csv'
    validation(archivo)