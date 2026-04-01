import numpy as np
import pandas as pd
from datetime import datetime, timedelta

fecha_inicio = datetime(2011, 1, 1)
total_dias = (15 * 365) + 4
registros = []

for i in range(total_dias):
    fecha_actual = fecha_inicio + timedelta(days=i)
    
    d1 = np.random.randint(0, 10)
    d2 = np.random.randint(0, 10)
    d3 = np.random.randint(0, 10)
    numero = f"{d1}{d2}{d3}"
    
    registros.append([fecha_actual.strftime('%Y/%m/%d'), numero])


df = pd.DataFrame(registros, columns=["Fecha", "Numero"])
df.to_csv("./data/data.csv", index=False, header=False)

#NO EJECUTAR