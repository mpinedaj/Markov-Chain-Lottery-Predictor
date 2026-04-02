import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
from src.model.matrix_generator import generar_matriz_transicion
from src.usecases.max_number import full_number_probability
from src.usecases.probabilities import number_n_day_probability

list_enumeracion = ["Primer Dígito", "Segundo Dígito", "Tercer Dígito"]

def initValues():
    matrices = generar_matriz_transicion()
    ultimo_resultado = simpledialog.askstring("Ultimo resultado de la lotería", "Ingrese el último número de la lotería (3 dígitos): ")
    if len(ultimo_resultado) != 3 or not ultimo_resultado.isdigit():
        raise ValueError("El último resultado debe ser un número de 3 dígitos.")
    dias_proyeccion = simpledialog.askinteger("Días de proyección", "¿A cuántos días quiere calcular la predicción?: ")
    if dias_proyeccion is None or dias_proyeccion <= 0:
        raise ValueError("El número de días de proyección debe ser un entero positivo.")
    return matrices, ultimo_resultado, dias_proyeccion

def startInterface():
    matrixs, last_result, projection_days = initValues()

    root = tk.Tk()
    root.title("Markov Chain Lottery Predictor")
    root.geometry("1000x650")
    root.resizable(True, True)
    root.configure(bg="#ecf0f1")

    # ==================== SIDEBAR MENU ====================
    sidebar = tk.Frame(root, bg="#34495e", width=250)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    
    # Logo/Title en sidebar
    logo_frame = tk.Frame(sidebar, bg="#2c3e50", height=120)
    logo_frame.pack(fill="x")
    logo_frame.pack_propagate(False)
    
    tk.Label(logo_frame, text="MARKOV\nLOTTERY", font=("Arial", 18, "bold"), 
             bg="#2c3e50", fg="white").pack(pady=20)
    tk.Label(logo_frame, text="Predictor", font=("Arial", 10), 
             bg="#2c3e50", fg="#95a5a6").pack()
    
    # Info panel
    info_panel = tk.Frame(sidebar, bg="#2c3e50")
    info_panel.pack(fill="x", pady=20, padx=10)
    
    tk.Label(info_panel, text="Configuración", font=("Arial", 10, "bold"), 
             bg="#2c3e50", fg="#bdc3c7").pack(pady=(5, 10))
    
    tk.Label(info_panel, text=f"Último resultado:", font=("Arial", 9), 
             bg="#2c3e50", fg="#95a5a6").pack()
    tk.Label(info_panel, text=f"{last_result}", font=("Arial", 12, "bold"), 
             bg="#2c3e50", fg="#3498db").pack(pady=(0, 10))
    
    tk.Label(info_panel, text=f"Días proyección:", font=("Arial", 9), 
             bg="#2c3e50", fg="#95a5a6").pack()
    tk.Label(info_panel, text=f"{projection_days}", font=("Arial", 12, "bold"), 
             bg="#2c3e50", fg="#e74c3c").pack()
    
    # Separador
    tk.Frame(sidebar, bg="#7f8c8d", height=1).pack(fill="x", pady=20)
    
    # ==================== CONTENT AREA ====================
    content_area = tk.Frame(root, bg="#ecf0f1")
    content_area.pack(side="right", fill="both", expand=True)
    
    # Header del content area
    header = tk.Frame(content_area, bg="white", height=80)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    header_title = tk.Label(header, text="Seleccione una opción del menú", 
                            font=("Arial", 20, "bold"), bg="white", fg="#2c3e50")
    header_title.pack(side="left", padx=30, pady=25)
    
    # Container para los diferentes paneles
    panels_container = tk.Frame(content_area, bg="#ecf0f1")
    panels_container.pack(fill="both", expand=True, padx=20, pady=20)
    
    # ==================== PANEL 1: Número Más Probable ====================
    panel1 = tk.Frame(panels_container, bg="white")
    
    tk.Label(panel1, text="Ver Número Más Probable", font=("Arial", 18, "bold"), 
             bg="white", fg="#2c3e50").pack(pady=30)
    
    tk.Frame(panel1, bg="#bdc3c7", height=2).pack(fill="x", padx=50)
    
    desc1 = tk.Label(panel1, text="Esta opción calcula el número de 3 dígitos con mayor probabilidad\n"
                     "de aparecer en los próximos días especificados.\n\n"
                     "Utiliza las matrices de transición de Markov para determinar\n"
                     "la probabilidad de cada dígito en cada posición.",
                     font=("Arial", 11), bg="white", fg="#7f8c8d", justify="center")
    desc1.pack(pady=30)
    
    result1_frame = tk.Frame(panel1, bg="#ecf0f1", relief="solid", bd=1)
    result1_frame.pack(pady=20, padx=50, fill="x")
    
    tk.Label(result1_frame, text="Número más probable:", font=("Arial", 10), 
             bg="#ecf0f1", fg="#7f8c8d").pack(pady=(15, 5))
    
    result1_label = tk.Label(result1_frame, text="---", font=("Arial", 32, "bold"), 
                             bg="#ecf0f1", fg="#27ae60")
    result1_label.pack(pady=(5, 20))
    
    def call_full_number_probability():
        num_predicho = full_number_probability(matrixs, last_result, projection_days)
        print("Generando resultado del número más probable calculado...")
        result1_label.config(text=f"{num_predicho}")
    
    tk.Button(panel1, text="Calcular Número", command=call_full_number_probability,
              font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
              padx=50, pady=15, cursor="hand2", relief="flat").pack(pady=20)
    
    # ==================== PANEL 2: Probabilidades Específicas ====================
    panel2 = tk.Frame(panels_container, bg="white")
    
    tk.Label(panel2, text="Probabilidades de Número Específico", font=("Arial", 18, "bold"), 
             bg="white", fg="#2c3e50").pack(pady=30)
    
    tk.Frame(panel2, bg="#bdc3c7", height=2).pack(fill="x", padx=50)
    
    desc2 = tk.Label(panel2, text="Consulta las probabilidades individuales de cada dígito\n"
                     "y la probabilidad conjunta de un número completo.\n\n"
                     "Ingrese el número de 3 dígitos que desea analizar.",
                     font=("Arial", 11), bg="white", fg="#7f8c8d", justify="center")
    desc2.pack(pady=30)
    
    tk.Button(panel2, text="Ingresar Número a Consultar", command=lambda: call_specific_probability(),
              font=("Arial", 12, "bold"), bg="#3498db", fg="white",
              padx=50, pady=15, cursor="hand2", relief="flat").pack(pady=(0, 20))
    
    result2_container = tk.Frame(panel2, bg="white")
    result2_container.pack(pady=20, fill="both", expand=True, padx=50)
    
    def call_specific_probability():
        print("Generando resultado de probabilidades para un número específico...")
        num_consulta = simpledialog.askstring("Número a consultar", "Ingrese el número de 3 dígitos a consultar: ")
        
        if not num_consulta:
            messagebox.showerror("Entrada vacía", "No se ingresó ningún número. Por favor, ingrese un número de 3 dígitos.")
            return
        
        if len(num_consulta) > 3: 
            messagebox.showwarning("Número inválido", "El número es superior a 3 dígitos. Se utilizaran solo los 3 primeros dígitos ingresados")
            num_consulta = num_consulta[:3]
            
        elif len(num_consulta) < 3 or not num_consulta.isdigit():
            messagebox.showerror("Número inválido", "El valor ingresado debe ser un número de 3 dígitos. Por favor, intente nuevamente.")
            return
        
        # Limpiar resultados anteriores
        for widget in result2_container.winfo_children():
            widget.destroy()
        
        # Frame principal de resultados
        results_frame = tk.Frame(result2_container, bg="#ecf0f1", relief="solid", bd=1)
        results_frame.pack(fill="both", expand=True)
        
        # Número consultado
        tk.Label(results_frame, text=f"Número consultado: {num_consulta}", 
                font=("Arial", 14, "bold"), fg="#2c3e50", bg="#ecf0f1").pack(pady=(10, 0))
        
        # Grid de dígitos
        digits_grid = tk.Frame(results_frame, bg="#ecf0f1")
        digits_grid.pack(pady=10)
        
        prob_conjunta = 1.0
        
        for i in range(3):
            m_i = matrixs[f"Digito_{i+1}"]
            est_actual_i = last_result[i]
            digito_obj = num_consulta[i]
            
            p_i = number_n_day_probability(m_i, digito_obj, est_actual_i, projection_days)
            prob_conjunta *= p_i
            
            digit_card = tk.Frame(digits_grid, bg="white", relief="solid", bd=1, width=150)
            digit_card.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
            
            tk.Label(digit_card, text=list_enumeracion[i], 
                    font=("Arial", 9), bg="white", fg="#7f8c8d").pack(pady=(10, 5))
            tk.Label(digit_card, text=f"{digito_obj}", 
                    font=("Arial", 24, "bold"), bg="white", fg="#2c3e50").pack(pady=5)
            tk.Label(digit_card, text="Probabilidad", 
                    font=("Arial", 8), bg="white", fg="#7f8c8d").pack(pady=(10, 2))
            tk.Label(digit_card, text=f"{p_i:.4f}", 
                    font=("Arial", 12, "bold"), bg="white", fg="#e74c3c").pack(pady=(2, 10))
        
        # Probabilidad conjunta
        tk.Frame(results_frame, bg="#bdc3c7", height=1).pack(fill="x", padx=20, pady=15)
        
        joint_frame = tk.Frame(results_frame, bg="#ecf0f1")
        joint_frame.pack(pady=10)
        
        tk.Label(joint_frame, text=f"Probabilidad Conjunta: {prob_conjunta:.8f}", 
                font=("Arial", 12, "bold"), fg="#3498db", bg="#ecf0f1").pack(fill="x")
    
    # ==================== PANEL 3: Matrices ====================
    panel3 = tk.Frame(panels_container, bg="white")
    
    tk.Label(panel3, text="Matrices de Transición", font=("Arial", 18, "bold"), 
             bg="white", fg="#2c3e50").pack(pady=30)
    
    tk.Frame(panel3, bg="#bdc3c7", height=2).pack(fill="x", padx=50)
    
    desc3 = tk.Label(panel3, text="Visualiza las matrices de probabilidad de transición\n"
                     "utilizadas en el modelo de Markov.\n\n"
                     "Cada matriz representa las probabilidades de transición\n"
                     "entre estados para cada posición del número (dígito 1, 2 y 3).",
                     font=("Arial", 11), bg="white", fg="#7f8c8d", justify="center")
    desc3.pack(pady=30)
    
    def call_show_matrix():
        print("Mostrando matrices de transición...")
        ventana_matrices = tk.Toplevel(root)
        ventana_matrices.title("Matrices de Transición - Markov")
        ventana_matrices.geometry("1000x800")

        scrollbar = tk.Scrollbar(ventana_matrices)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        texto_area = tk.Text(ventana_matrices, font=("Courier New", 10), 
                             yscrollcommand=scrollbar.set, padx=10, pady=10)
        texto_area.pack(expand=True, fill="both")
        scrollbar.config(command=texto_area.yview)

        for nombre, matriz in matrixs.items():
            df = pd.DataFrame(matriz)
            texto_area.insert(tk.END, f"--- MATRIZ: {nombre} ---\n")
            texto_area.insert(tk.END, f"{df.to_string()}\n\n")
    
    tk.Button(panel3, text="Abrir Visualizador de Matrices", command=call_show_matrix,
              font=("Arial", 12, "bold"), bg="#9b59b6", fg="white",
              padx=50, pady=15, cursor="hand2", relief="flat").pack(pady=20)
    
    # Información adicional
    info_matrices = tk.Frame(panel3, bg="#ecf0f1", relief="solid", bd=1)
    info_matrices.pack(pady=20, padx=50, fill="x")
    
    tk.Label(info_matrices, text="📊 Las matrices se mostrarán en una ventana nueva",
             font=("Arial", 10), bg="#ecf0f1", fg="#7f8c8d").pack(pady=15)
    
    # ==================== MENU BUTTONS ====================
    current_panel = {"value": None}
    menu_buttons = []
    
    def show_panel(panel, button_index):
        # Ocultar todos los paneles
        panel1.pack_forget()
        panel2.pack_forget()
        panel3.pack_forget()
        
        # Mostrar el panel seleccionado
        panel.pack(fill="both", expand=True)
        current_panel["value"] = panel
        
        # Actualizar estilos de botones
        titles = ["Número Más Probable", "Consultar Número", "Matrices de Transición"]
        header_title.config(text=titles[button_index])
        
        for i, btn in enumerate(menu_buttons):
            if i == button_index:
                btn.config(bg="#3498db", fg="white")
            else:
                btn.config(bg="#34495e", fg="#bdc3c7")
    
    # Crear botones del menú
    menu_data = [
        ("1", "Número Más\nProbable", panel1),
        ("2", "Consultar\nNúmero", panel2),
        ("3", "Matrices de\nTransición", panel3)
    ]
    
    for idx, (num, text, panel) in enumerate(menu_data):
        btn_frame = tk.Frame(sidebar, bg="#34495e")
        btn_frame.pack(fill="x", pady=2)
        
        btn = tk.Button(btn_frame, text=f"{num}. {text}", 
                       font=("Arial", 11, "bold"), bg="#34495e", fg="#bdc3c7",
                       anchor="w", padx=20, pady=15, relief="flat", cursor="hand2",
                       command=lambda p=panel, i=idx: show_panel(p, i))
        btn.pack(fill="x")
        menu_buttons.append(btn)
    
    # Mostrar panel inicial
    show_panel(panel1, 0)

    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
    print("Interfaz cerrada correctamente, finalizando programa...")