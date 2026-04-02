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