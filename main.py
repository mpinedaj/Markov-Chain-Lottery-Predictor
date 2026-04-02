from src.model.matrix_generator import generar_matriz_transicion
from src.usecases.show_matrix import show_matrix
from src.usecases.probabilities import  number_n_day_probability
from src.usecases.max_number import full_number_probability
from src.ui.interface import startInterface

matrices = generar_matriz_transicion() 

ultimo_resultado = input("Ingrese el último número que cayó (3 dígitos): ")
dias_proyeccion = int(input("¿A cuántos días quiere calcular la predicción?: "))

while True:
    print("\nMENÚ DE OPCIONES:")
    print("1. Ver número más probable")
    print("2. Ver probabilidades de un número específico")
    print("3. Ver matrices de transición")
    print("4. Ver interfaz basica incompleta")
    print("5. Salir")
    
    opcion = input("\nSeleccione una opción: ")

    match opcion:
        case "1":
            # Determinar número de mayor probabilidad
            num_predicho = full_number_probability(matrices, ultimo_resultado, dias_proyeccion)
            print(f"\n>>> El número más probable es: {num_predicho}")
        
        case "2":
            # Probabilidad de un número cualquiera en n días
            num_consulta = input("Ingrese el número de 3 dígitos a consultar: ")
            print(f"\nProbabilidades para el número {num_consulta} en el día {dias_proyeccion}:")
            
            prob_conjunta = 1.0  
            
            for i in range(3):
                m_i = matrices[f"Digito_{i+1}"]
                est_actual_i = ultimo_resultado[i]
                digito_obj = num_consulta[i]
                
                p_i = number_n_day_probability(m_i, digito_obj, est_actual_i, dias_proyeccion)
                print(f" -> Digito {i+1} (Dígito {digito_obj}): {p_i:.10f}")
                
                prob_conjunta *= p_i
            
            print(f"PROBABILIDAD TOTAL DEL NÚMERO {num_consulta}: {prob_conjunta:.12f}")
        
        case "3":
            # Visualizar probabilidades de transición
            print("\nMATRICES ESTOCÁSTICAS:")
            show_matrix(matrices)

        case "4":
            startInterface()
            break  
        case "5":
            print("Saliendo del sistema...")
            break
        
        case _:
            print("Opción no válida, intente de nuevo.")