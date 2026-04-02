import tkinter as tk
import pandas as pd
from src.model.matrix_generator import generar_matriz_transicion
from src.usecases.show_matrix import show_matrix
##from src.usecases.probabilities import  number_n_day_probability
from src.usecases.max_number import full_number_probability



def startInterface():
    matrices = generar_matriz_transicion() 
    ultimo_resultado = 0
    dias_proyeccion = 0
    num_predicho = 0

    def get_num_predicho(entry):
        nonlocal num_predicho
        num_predicho = entry.get()
        num_predicho = str(num_predicho)
        print(f"Numero elegido a ver su probabilidad capturado: {num_predicho}")
    
    def get_ultimo_resultado(entry):
        nonlocal ultimo_resultado
        ultimo_resultado = entry.get()
        ultimo_resultado = str(ultimo_resultado)
        print(f"Numero capturado: {ultimo_resultado}")

    def get_dias_proyeccion(entry):
        nonlocal dias_proyeccion
        dias_proyeccion = entry.get()
        dias_proyeccion = int(dias_proyeccion) 
        print(f"Dias capturado: {dias_proyeccion}")

    def call_full_number_probability():
        result = full_number_probability(matrices, ultimo_resultado, dias_proyeccion)
        label_resultado1.config(text=f"El valor es: {result}")
    
    def call_specific_probability():
        print("Logica a arreglar hola arturo")

    def call_show_matrix():
        print("Logica de showmatrix")
        # Crear ventana secundaria
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
        for nombre, matriz in matrices.items():
            df = pd.DataFrame(matriz)
            texto_area.insert(tk.END, f"--- MATRIZ: {nombre} ---\n")
            texto_area.insert(tk.END, f"{df.to_string()}\n\n")
        
        # Bloquear el texto para que sea solo lectura
        texto_area.config(state=tk.DISABLED)



    root = tk.Tk()
    root.state('zoomed')
    root.title("Analisis Loteria Uso de Markov")


    titulo = tk.Label(root, text="Analisis Loteria Uso de Markov", font=("Arial", 20, "bold"))
    titulo.grid(row=1, column=0, padx=20 ,pady=20)
    

    # Fila 1 
    label_ask1 = tk.Label(root, text="Último número (3 dígitos):", font=("Arial", 12))
    label_ask1.grid(row=2, column=0, padx=10, pady=10) 

    entry_ask1 = tk.Entry(root)
    entry_ask1.grid(row=2, column=1, padx=10, pady=10)

    boton_ask1 = tk.Button(root, text="Enviar", command=lambda: get_ultimo_resultado(entry_ask1))
    boton_ask1.grid(row=2, column=2, padx=10, pady=10)

    # Fila 2 
    label_ask2 = tk.Label(root, text="Días para la predicción:", font=("Arial", 12))
    label_ask2.grid(row=2, column=3, padx=10, pady=10)

    entry_ask2 = tk.Entry(root)
    entry_ask2.grid(row=2, column=4, padx=10, pady=10)

    boton_ask2 = tk.Button(root, text="Enviar", command=lambda: get_dias_proyeccion(entry_ask2))
    boton_ask2.grid(row=2, column=5, padx=10, pady=10)

    # Opciones a ejecutar
    opciones = tk.Label(root, text="Seleccione una opcion ", font=("Arial", 20, "bold"))
    opciones.grid(row=3, column=0, padx=20 ,pady=20)

    # Opcion 1: Numero más Probable
    boton_op1 = tk.Button(root, text="Ver número más probable", command=call_full_number_probability)
    boton_op1.grid(row=4, column=0, padx=10, pady=10)

    label_resultado1 = tk.Label(root, text="Resultado 1 aqui", font=("Arial", 12))
    label_resultado1.grid(row=5, column=0, padx=10, pady=10)

    # Opcion 2: Ver probabilidades de un número específico"
    boton_op2 = tk.Button(root, text="Ver probabilidades de un número específico", command=call_specific_probability) #Cambiar la funcion por la nueva funcion a generar arturo te invoco
    boton_op2.grid(row=4, column=1, padx=10, pady=10)

    entry_op2 = tk.Entry(root)
    entry_op2.grid(row=5, column=1, padx=10, pady=10)

    boton_op2 = tk.Button(root, text="Enviar", command=lambda: get_num_predicho(entry_op2))
    boton_op2.grid(row=5, column=2, padx=10, pady=10)

    label_resultado2 = tk.Label(root, text="Resultado 2 aqui", font=("Arial", 12))
    label_resultado2.grid(row=6, column=1, padx=10, pady=10)

    #Opcion 3: Ver matrices de transición
    boton_op3 = tk.Button(root, text="Ver matrices de transición", command=call_show_matrix) #Cambiar la funcion por la nueva funcion a generar arturo te invoco
    boton_op3.grid(row=4, column=3, padx=10, pady=10)



    
    root.mainloop()
