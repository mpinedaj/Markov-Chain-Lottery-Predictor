import numpy as np
from src.model.matrix_generator import matrix_generator_n_day

def number_n_day_probability(matriz, number, estado, dias):
    vn = matrix_generator_n_day(matriz, estado, dias)
    return vn[int(number)]  
