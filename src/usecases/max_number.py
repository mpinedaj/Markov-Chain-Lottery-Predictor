import numpy as np
from src.model.matrix_generator import matrix_generator_n_day


def max_probability_n_day_number(matriz, estado, dias):
    vn = matrix_generator_n_day(matriz, estado, dias)
    max_p_number = np.argmax(vn)
    return max_p_number

def full_number_probability(matrices, ultimo_resultado, dias):
    numero = ""
    
    for i in range(3):
        m = matrices[f"Digito_{i+1}"]
        est = ultimo_resultado[i]
        indice = max_probability_n_day_number(m, est, dias)
        numero += str(indice)
        
    return numero