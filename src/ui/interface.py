import tkinter as tk
from tkinter import simpledialog
import pandas as pd
from src.model.matrix_generator import generar_matriz_transicion
from src.usecases.max_number import full_number_probability
from src.usecases.probabilities import number_n_day_probability

list_enumeracion = ["Primer Dígito", "Segundo Dígito", "Tercer Dígito"]

#Esta función se ejecuta al iniciar la interfaz, tal y como sigue la lógica el main
#Genera la matriz de transición y pide los datos que solicita el main, pero de una forma más práctica
def initValues():
    matrices = generar_matriz_transicion()
    ultimo_resultado = simpledialog.askstring("Ultimo resultado de la lotería", "Ingrese el último número de la lotería (3 dígitos): ")
    dias_proyeccion = simpledialog.askinteger("Días de proyección", "¿A cuántos días quiere calcular la predicción?: ")
    return matrices, ultimo_resultado, dias_proyeccion

def startInterface():
    #Arrancamos el programa solicitando los valores pertinentes
    matrixs, last_result, projection_days = initValues()

    root = tk.Tk()
    root.title("Markov Chain Lottery Predictor")
    root.resizable(True, True)

    titulo = tk.Label(root, text="Análisis de la lotería - Markov", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)
    
    #Contenedor principal, aquí se agregan las opciones en el main
    main_c = tk.Frame(root)
    main_c.pack(pady=20, anchor="w")

    #----------------- Contenedor -----------------

    #Ver número más probable
    ask_num = tk.Label(main_c, text="Ver número más probable", font=("Arial", 14))
    an_button = tk.Button(main_c, text="Ver número")
    ask_num.grid(row=0, column=0, padx=20, pady=5, sticky="w")
    an_button.grid(row=1, column=0, padx=20, pady=25, sticky="w")

    #Ver probabilidades de un número específico
    ask_num_prob = tk.Label(main_c, text="Ver probabilidades de un número específico", font=("Arial", 14))
    anp_button = tk.Button(main_c, text="Ver probabilidades")
    ask_num_prob.grid(row=2, column=0, padx=20, pady=5, sticky="w")
    anp_button.grid(row=3, column=0, padx=20, pady=25, sticky="w")
    
    #Tabla para mostrar las probabilidades de un número específico
    table_prob = tk.Frame(main_c)
    table_prob.grid(row=2, column=1, rowspan=2, padx=20, pady=5, sticky="w")

    #Ver matrices de transición
    ask_matrix = tk.Label(main_c, text="Ver matrices de transición", font=("Arial", 14))
    am_button = tk.Button(main_c, text="Ver matrices")
    ask_matrix.grid(row=4, column=0, padx=20, pady=5, sticky="w")
    am_button.grid(row=5, column=0, padx=20, pady=25, sticky="w")

    #----------------- Comandos para los botones -----------------
    
    #Caso "Ver número más probable"
    def call_full_number_probability():
        num_predicho = full_number_probability(matrixs, last_result, projection_days)
        print("Generando label con el resultado del número más probable calculado...")
        label_resultado1 = tk.Label(main_c, text=f"El número más probable es: {num_predicho}", font=("Arial", 14,), fg="green")
        label_resultado1.grid(row=0, column=1, rowspan=2, padx=35, pady=5, sticky="w")
    
    #Caso "Ver probabilidades de un número específico"
    def call_specific_probability():
        print("Generando label con el resultado de probabilidades para un número específico...")
        num_consulta = simpledialog.askstring("Número a consultar", "Ingrese el número de 3 dígitos a consultar: ")
        
        #Mostrar número ingresado
        tk.Label(table_prob, text=f"Número ingresado", font=("Arial", 14), fg="green").grid(row=0, column=0, padx=35, pady=5)
        tk.Label(table_prob, text=f"{num_consulta}", font=("Arial", 12), fg="green").grid(row=1, column=0, padx=35, pady=5)
        
        prob_conjunta = 1.0
        for i in range(3):
            m_i = matrixs[f"Digito_{i+1}"]
            est_actual_i = last_result[i]
            digito_obj = num_consulta[i]
            
            p_i = number_n_day_probability(m_i, digito_obj, est_actual_i, projection_days)
            prob_conjunta *= p_i
            
            #Generar labels para cada dígito y su probabilidad
            tk.Label(table_prob, text=f"{list_enumeracion[i]} ({digito_obj}):", font=("Arial", 14)).grid(row=0, column=i+1, padx=5, pady=5, sticky="w")
            tk.Label(table_prob, text=f"Probabilidad: {p_i:.4f}", font=("Arial", 12)).grid(row=1, column=i+1, padx=5, pady=5, sticky="w")
        
        #Mostrar probabilidad conjunta
        tk.Label(table_prob, text="Probabilidad conjunta", font=("Arial", 14), fg="blue").grid(row=0, column=5, padx=35, pady=5)
        tk.Label(table_prob, text=f"{prob_conjunta:.8f}", font=("Arial", 12), fg="blue").grid(row=1, column=5, padx=35, pady=5)

    #Caso "Ver matrices de transición"
    def call_show_matrix():
        print("Mostrando matrices de transición...")
        ventana_matrices = tk.Toplevel(root)
        ventana_matrices.title("Matrices de Transición - Markov")
        ventana_matrices.geometry("600x500")

        # Añadir un scrollbar por si las matrices son grandes
        scrollbar = tk.Scrollbar(ventana_matrices)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Widget de texto para mostrar las matrices
        texto_area = tk.Text(ventana_matrices, font=("Courier New", 10), 
                             yscrollcommand=scrollbar.set, padx=10, pady=10)
        texto_area.pack(expand=True, fill="both")
        scrollbar.config(command=texto_area.yview)

        # Insertar los datos de las matrices
        for nombre, matriz in matrixs.items():
            df = pd.DataFrame(matriz)
            texto_area.insert(tk.END, f"--- MATRIZ: {nombre} ---\n")
            texto_area.insert(tk.END, f"{df.to_string()}\n\n")
            
    #------------ Configurar comandos de los botones -----------------
    
    an_button.config(command=call_full_number_probability)
    anp_button.config(command=call_specific_probability)
    am_button.config(command=call_show_matrix)
    
    #Cerrar correctamente la interfaz
    
    root.protocol("WM_DELETE_WINDOW", root.quit())
    root.mainloop()
    print("Interfaz cerrada correctamente, finalizando programa...")
