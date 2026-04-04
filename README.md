# Markov Lottery Predictor (Lab 2)

## Overview
This system uses **Markov Chains** to predict 3-digit lottery numbers. It processes 15+ years of data to identify the most probable numbers and transition states.

## Key Features
* **Three-Digit Analysis**: Independent Markov Chains for each digit.
* **Statistical Validation**: Tests for randomness and independence.
* **Predictions**: Calculates the most likely number to appear in a given timeframe.
* **High Precision**: Implemented with maximum significant figures for better accuracy.

# 🔬 MATEMÁTICA DE MARKOV: GUÍA VISUAL DETALLADA

## 📐 EJEMPLO PASO A PASO CON NÚMEROS REALES

Vamos a simular un ejemplo completo del primer dígito para entender exactamente cómo funciona.

---

## PASO 1: DATOS HISTÓRICOS (Simplificado)

Supongamos que tenemos estos últimos 20 números de la lotería:

```
Día  | Número | Dígito 1
-----|--------|----------
1    | 234    | 2
2    | 567    | 5
3    | 789    | 7
4    | 234    | 2
5    | 345    | 3
6    | 456    | 4
7    | 567    | 5
8    | 678    | 6
9    | 789    | 7
10   | 890    | 8
11   | 901    | 9
12   | 012    | 0
13   | 123    | 1
14   | 234    | 2
15   | 345    | 3
16   | 456    | 4
17   | 567    | 5
18   | 678    | 6
19   | 789    | 7
20   | 234    | 2
```

---

## PASO 2: CONTAR TRANSICIONES

Una **transición** es cuando un dígito cambia a otro dígito el día siguiente.

### Transiciones del dígito 1:

```
De 2 → 5: 2 veces (día 1→2, día 14→15)
De 2 → 3: 1 vez (día 4→5)
De 2 → ?:  (no hay más transiciones desde 2 en nuestros datos)

De 5 → 7: 1 vez (día 2→3)
De 5 → 6: 2 veces (día 7→8, día 17→18)

De 7 → 2: 2 veces (día 3→4, día 9→10)
De 7 → 8: 1 vez (día 19→20)
...
```

### Tabla completa de frecuencias (matriz de conteo):

```
      A 0  1  2  3  4  5  6  7  8  9
Desde ↓
0     0  1  0  0  0  0  0  0  0  0
1     0  0  1  0  0  0  0  0  0  0
2     0  0  0  1  0  2  0  0  0  0
3     0  0  0  0  2  0  0  0  0  0
4     0  0  0  0  0  2  0  0  0  0
5     0  0  0  0  0  0  2  1  0  0
6     0  0  0  0  0  0  0  2  0  0
7     1  0  2  0  0  0  0  0  1  0
8     0  0  0  0  0  0  0  0  0  1
9     1  0  0  0  0  0  0  0  0  0
```

**Interpretación:**
- Fila 2, Columna 5: El dígito 2 fue seguido por 5 en 2 ocasiones
- Fila 7, Columna 2: El dígito 7 fue seguido por 2 en 2 ocasiones

---

## PASO 3: CALCULAR PROBABILIDADES (Normalización)

Dividimos cada fila por la suma de esa fila para obtener probabilidades.

### Ejemplo para la fila 2:

```
Suma de la fila 2: 0+0+0+1+0+2+0+0+0+0 = 3

P[2→0] = 0/3 = 0.000
P[2→1] = 0/3 = 0.000
P[2→2] = 0/3 = 0.000
P[2→3] = 1/3 = 0.333
P[2→4] = 0/3 = 0.000
P[2→5] = 2/3 = 0.667
P[2→6] = 0/3 = 0.000
P[2→7] = 0/3 = 0.000
P[2→8] = 0/3 = 0.000
P[2→9] = 0/3 = 0.000
         -----
         1.000 ✓ (suma 100%)
```

### Matriz de Transición P (probabilidades):

```
      A 0     1     2     3     4     5     6     7     8     9     SUMA
Desde ↓
0    0.00  1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00   1.00
1    0.00  0.00  1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00   1.00
2    0.00  0.00  0.00  0.33  0.00  0.67  0.00  0.00  0.00  0.00   1.00
3    0.00  0.00  0.00  0.00  1.00  0.00  0.00  0.00  0.00  0.00   1.00
4    0.00  0.00  0.00  0.00  0.00  1.00  0.00  0.00  0.00  0.00   1.00
5    0.00  0.00  0.00  0.00  0.00  0.00  0.67  0.33  0.00  0.00   1.00
6    0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.00  0.00  0.00   1.00
7    0.25  0.00  0.50  0.00  0.00  0.00  0.00  0.00  0.25  0.00   1.00
8    0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.00   1.00
9    1.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00   1.00
```

**¡Esta es nuestra Matriz de Transición P!**

Cada fila suma 1.0 (100% de probabilidad).

---

## PASO 4: PREDECIR 1 DÍA EN EL FUTURO

**Situación:** El último número fue **234**, queremos predecir el primer dígito mañana.

Último dígito 1: **2**

### Vector de estado inicial (v0):

```
v0 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
      ↑     ↑
    pos 0  pos 2 (estamos en estado 2)
```

### Multiplicación v0 × P:

```
Resultado día 1 = v0 × P
                = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] × P
                = fila 2 de P
                = [0.00, 0.00, 0.00, 0.33, 0.00, 0.67, 0.00, 0.00, 0.00, 0.00]
```

**Interpretación:**
- P(dígito 0) = 0.00%
- P(dígito 1) = 0.00%
- P(dígito 2) = 0.00%
- P(dígito 3) = 33.3%
- P(dígito 4) = 0.00%
- P(dígito 5) = 66.7% ← **MÁS PROBABLE**
- P(dígito 6) = 0.00%
- P(dígito 7) = 0.00%
- P(dígito 8) = 0.00%
- P(dígito 9) = 0.00%

**Predicción para mañana:** El dígito más probable es **5**

---

## PASO 5: PREDECIR 2 DÍAS EN EL FUTURO

Ahora queremos predecir el dígito en 2 días.

### Cálculo de P²:

```
P² = P × P
```

Calculamos elemento por elemento. Por ejemplo, P²[2][0]:

```
P²[2][0] = P[2][0]×P[0][0] + P[2][1]×P[1][0] + ... + P[2][9]×P[9][0]
         = 0.00×0.00 + 0.00×0.00 + 0.00×0.00 + 0.33×0.00 + 0.00×0.00
           + 0.67×0.00 + 0.00×0.00 + 0.00×0.00 + 0.00×0.00 + 0.00×1.00
         = 0.00
```

Calculando toda la matriz (esto es pesado, por eso usamos NumPy):

```
      A 0     1     2     3     4     5     6     7     8     9
Desde ↓
2    0.00  0.00  0.00  0.00  0.33  0.00  0.45  0.22  0.00  0.00
```

### Predicción para 2 días:

```
v0 × P² = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] × P²
        = fila 2 de P²
        = [0.00, 0.00, 0.00, 0.00, 0.33, 0.00, 0.45, 0.22, 0.00, 0.00]
```

**Dígito más probable en 2 días:** **6** (45% de probabilidad)

---

## PASO 6: PREDECIR N DÍAS EN EL FUTURO (Generalización)

### Fórmula:

```
Distribución en n días = v0 × P^n

donde P^n = P × P × P × ... × P (n veces)
```

### En código Python (del proyecto):

```python
def matrix_generator_n_day(matriz_transicion, estado, dias):
    # Vector de estado inicial
    v0 = np.zeros(10)
    v0[int(estado)] = 1
    
    # Elevar matriz a la potencia n
    Pn = np.linalg.matrix_power(matriz_transicion, dias)
    
    # Multiplicar v0 × P^n
    return np.dot(v0, Pn)
```

### Ejemplo para 7 días:

```
P^7 = P × P × P × P × P × P × P

v0 × P^7 = distribución de probabilidad en 7 días
```

Si P^7[2][4] = 0.087, significa:
- "Si hoy el dígito es 2, en 7 días hay 8.7% de probabilidad de que sea 4"

---

## PASO 7: PREDICCIÓN DEL NÚMERO COMPLETO

El código hace este proceso **3 veces** (una por dígito):

### Datos:
```
Último número: 234
Días a predecir: 7
```

### Proceso:

#### Dígito 1 (partiendo de 2):
```
v0_1 = [0,0,1,0,0,0,0,0,0,0]
P1^7 = matriz del dígito 1 elevada a 7
π1_7 = v0_1 × P1^7 = [0.08, 0.11, 0.09, 0.13, 0.10, 0.12, 0.08, 0.11, 0.09, 0.09]
                       ↑                     ↑
                     pos 0                 pos 3 = MÁXIMO

Dígito predicho 1: 3
```

#### Dígito 2 (partiendo de 3):
```
v0_2 = [0,0,0,1,0,0,0,0,0,0]
P2^7 = matriz del dígito 2 elevada a 7
π2_7 = v0_2 × P2^7 = [0.09, 0.10, 0.08, 0.11, 0.09, 0.10, 0.12, 0.11, 0.10, 0.10]
                                                              ↑
                                                            pos 6 = MÁXIMO

Dígito predicho 2: 6
```

#### Dígito 3 (partiendo de 4):
```
v0_3 = [0,0,0,0,1,0,0,0,0,0]
P3^7 = matriz del dígito 3 elevada a 7
π3_7 = v0_3 × P3^7 = [0.10, 0.09, 0.11, 0.10, 0.09, 0.08, 0.10, 0.13, 0.11, 0.09]
                                                                      ↑
                                                                    pos 7 = MÁXIMO

Dígito predicho 3: 7
```

### Resultado final:

```
Número predicho en 7 días: 367
```

---

## PASO 8: PROBABILIDAD CONJUNTA (BONUS)

Si queremos saber la probabilidad de un número específico (ej: 367):

```python
# Dígito 1 = 3
p1 = π1_7[3] = 0.13

# Dígito 2 = 6  
p2 = π2_7[6] = 0.12

# Dígito 3 = 7
p3 = π3_7[7] = 0.13

# Probabilidad conjunta (asumiendo independencia)
P(367) = p1 × p2 × p3
       = 0.13 × 0.12 × 0.13
       = 0.002028
       = 0.2028%
```

**Interpretación:**
Hay aproximadamente **0.2%** de probabilidad de que el número **367** salga en 7 días, dado que el último número fue **234**.

---

## 📊 VISUALIZACIÓN DEL FLUJO

```
┌─────────────────────────────────────────────────────────────┐
│                    DATOS HISTÓRICOS                         │
│  (8,849 registros de lotería de 24 años)                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  DÍGITO 1   │    │  DÍGITO 2   │    │  DÍGITO 3   │
│  (0-9)      │    │  (0-9)      │    │  (0-9)      │
└─────────────┘    └─────────────┘    └─────────────┘
        ↓                   ↓                   ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Contar      │    │ Contar      │    │ Contar      │
│ Transiciones│    │ Transiciones│    │ Transiciones│
└─────────────┘    └─────────────┘    └─────────────┘
        ↓                   ↓                   ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Matriz P1   │    │ Matriz P2   │    │ Matriz P3   │
│   10x10     │    │   10x10     │    │   10x10     │
└─────────────┘    └─────────────┘    └─────────────┘
        ↓                   ↓                   ↓
        └───────────────────┼───────────────────┘
                            ↓
            ┌───────────────────────────────┐
            │ USUARIO INGRESA:              │
            │ - Último número: 234          │
            │ - Días: 7                     │
            └───────────────────────────────┘
                            ↓
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ v0 = [0..1] │    │ v0 = [0..1] │    │ v0 = [0..1] │
│ (estado 2)  │    │ (estado 3)  │    │ (estado 4)  │
└─────────────┘    └─────────────┘    └─────────────┘
        ↓                   ↓                   ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ P1^7        │    │ P2^7        │    │ P3^7        │
│ (potencia)  │    │ (potencia)  │    │ (potencia)  │
└─────────────┘    └─────────────┘    └─────────────┘
        ↓                   ↓                   ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ v0 × P1^7   │    │ v0 × P2^7   │    │ v0 × P3^7   │
│ = π1(7)     │    │ = π2(7)     │    │ = π3(7)     │
└─────────────┘    └─────────────┘    └─────────────┘
        ↓                   ↓                   ↓
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ argmax(π1)  │    │ argmax(π2)  │    │ argmax(π3)  │
│ = 3         │    │ = 6         │    │ = 7         │
└─────────────┘    └─────────────┘    └─────────────┘
        ↓                   ↓                   ↓
        └───────────────────┼───────────────────┘
                            ↓
            ┌───────────────────────────────┐
            │ NÚMERO PREDICHO: 367          │
            │ Probabilidad: 0.2%            │
            └───────────────────────────────┘
```

---

## 🧮 FÓRMULAS MATEMÁTICAS CLAVE

### 1. Matriz de Transición:
```
P[i][j] = Nᵢⱼ / Σₖ Nᵢₖ

donde:
- Nᵢⱼ = número de veces que i fue seguido por j
- Σₖ Nᵢₖ = total de veces que se observó el estado i
```

### 2. Distribución después de n pasos:
```
π(n) = π(0) · P^n

donde:
- π(0) = vector de estado inicial [0,0,...,1,...,0]
- π(n) = vector de probabilidades en el paso n
- P^n = matriz de transición elevada a la n
```

### 3. Probabilidad de estado específico:
```
P(estado j en n días | estado i hoy) = (P^n)[i][j]
```

### 4. Dígito más probable:
```
d* = argmax π(n)
    = argmax [π₀(n), π₁(n), ..., π₉(n)]
```

### 5. Probabilidad conjunta (3 dígitos):
```
P(d₁d₂d₃) = P(d₁) × P(d₂) × P(d₃)

Asumiendo independencia entre dígitos.
```

---

## 🎓 PROPIEDADES DE LA MATRIZ DE TRANSICIÓN

### 1. **Matriz Estocástica:**
```
∀i: Σⱼ P[i][j] = 1

Cada fila suma 1 (100% de probabilidad)
```

### 2. **No Negativa:**
```
∀i,j: P[i][j] ≥ 0

Todas las probabilidades son ≥ 0
```

### 3. **Chapman-Kolmogorov:**
```
P^(m+n) = P^m × P^n

La probabilidad de transición en m+n pasos es el producto
de las probabilidades en m pasos y n pasos
```

### 4. **Distribución Estacionaria (si existe):**
```
π = π · P

Distribución que no cambia con el tiempo
```

**Nota:** En este proyecto, es poco probable que exista una distribución estacionaria verdadera debido a la aleatoriedad de la lotería.

---

## 🔍 VALIDACIÓN MATEMÁTICA

### ¿Cómo verificar que el código es correcto?

#### Test 1: Suma de filas = 1
```python
for i in range(10):
    suma_fila = sum(P[i])
    assert abs(suma_fila - 1.0) < 1e-10, f"Fila {i} no suma 1"
```

#### Test 2: Valores no negativos
```python
for i in range(10):
    for j in range(10):
        assert P[i][j] >= 0, f"P[{i}][{j}] es negativo"
```

#### Test 3: Probabilidad después de 0 días = estado actual
```python
v0 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]  # Estado 2
P0 = np.linalg.matrix_power(P, 0)    # Matriz identidad
resultado = np.dot(v0, P0)
# Resultado debe ser [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
```

#### Test 4: Distribución después de 1 día = fila de la matriz
```python
v0 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]  # Estado 2
P1 = P  # 1 día
resultado = np.dot(v0, P1)
# Resultado debe ser igual a P[2] (fila 2)
```

---

## 💡 INTUICIÓN DETRÁS DE MARKOV

### Pregunta: ¿Por qué elevar la matriz a una potencia?

**Respuesta intuitiva:**

Imagina que vas dando pasos en un tablero:
- P^1 = ¿Dónde puedes estar en 1 paso?
- P^2 = ¿Dónde puedes estar en 2 pasos?
- P^7 = ¿Dónde puedes estar en 7 pasos?

Cada multiplicación de matriz "compone" las probabilidades:
```
P[2][5] × P[5][7] = probabilidad de ir de 2→5→7
```

Al multiplicar la matriz consigo misma, estamos sumando todas las posibles rutas de longitud n.

### Ejemplo visual:

```
Día 0: Estamos en 2
Día 1: Podemos estar en 3 (33%) o 5 (67%)
Día 2: Desde 3 podemos ir a 4 (100%)
       Desde 5 podemos ir a 6 (67%) o 7 (33%)
       
Probabilidades combinadas:
- 2→3→4: 0.33 × 1.00 = 0.33
- 2→5→6: 0.67 × 0.67 = 0.45
- 2→5→7: 0.67 × 0.33 = 0.22

P²[2] = [0, 0, 0, 0, 0.33, 0, 0.45, 0.22, 0, 0]
```

---

## 🎯 RESUMEN CONCEPTUAL

### ¿Qué hace el código?

1. **Lee datos históricos** → 8,849 números de lotería
2. **Cuenta patrones** → ¿Cuántas veces 5 fue seguido por 7?
3. **Calcula probabilidades** → P(5→7) = veces(5→7) / veces(5→X)
4. **Construye 3 matrices** → Una por cada dígito (10x10)
5. **Usuario da entrada** → Último número + días a predecir
6. **Eleva matrices** → P^n para predecir n días adelante
7. **Multiplica vectores** → v0 × P^n = distribución futura
8. **Encuentra máximo** → El dígito de mayor probabilidad
9. **Combina dígitos** → Forma el número de 3 dígitos

### ¿Por qué funciona?

Porque asume que:
- El futuro depende del presente (propiedad de Markov)
- Los patrones históricos se repetirán
- Cada dígito es independiente

### ¿Cuándo falla?

Cuando:
- La lotería cambia su mecanismo
- Los datos no son suficientes
- Hay sesgo en los datos
- La aleatoriedad perfecta hace que no haya patrones

---

## 📚 BIBLIOGRAFÍA MATEMÁTICA

### Conceptos usados:
1. **Cadenas de Markov:** Procesos estocásticos sin memoria
2. **Matrices Estocásticas:** Matrices con filas que suman 1
3. **Álgebra Lineal:** Multiplicación de matrices y vectores
4. **Teoría de Probabilidad:** Distribuciones y eventos independientes
5. **Chapman-Kolmogorov:** Composición de probabilidades

### Referencias:
- Sheldon Ross, "Introduction to Probability Models"
- Norris, "Markov Chains"
- Grinstead & Snell, "Introduction to Probability"

---

**Conclusión:** El proyecto implementa correctamente la teoría de Cadenas de Markov para predecir números de lotería, usando matemática rigurosa y código eficiente. La predicción es probabilística, no determinística, y su efectividad depende de la aleatoriedad real de los datos de la lotería.

