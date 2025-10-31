
# Documento del Menú en Consola

#### 1) Tema, problema y solución
👉 **Tema:** Optimización de la estrategia comercial mediante el análisis de ventas por ciudad.  
El objetivo es identificar zonas con alto y bajo rendimiento para tomar decisiones informadas que impulsen los ingresos.  

❗ **Problema:** Actualmente no contamos con una visión clara sobre qué ciudades generan más ingresos y cuáles tienen bajo rendimiento comercial.  
Esta falta de información limita la capacidad de rediseñar estrategias específicas para mejorar las ventas en zonas menos activas.  

✅ **Solución:** Utilizaremos Python y pandas para realizar un análisis de ventas por ciudad.  

---

#### 2) Dataset de referencia

##### Tabla: Ventas
| Campo          | Tipo de dato   | Escala    |
|----------------|----------------|-----------|
| id_venta       | int            | Razón     |
| fecha          | datetime.date  | Intervalo |
| id_cliente     | int            | Razón     |
| nombre_cliente | str            | Nominal   |
| email          | str            | Nominal   |
| medio_pago     | str            | Nominal   |

##### Tabla: Productos
| Campo           | Tipo de dato | Escala   |
|-----------------|--------------|----------|
| id_producto     | int          | Razón    |
| nombre_producto | str          | Nominal  |
| categoria       | str          | Nominal  |
| precio_unitario | float        | Razón    |

##### Tabla: Detalle de venta
| Campo           | Tipo de dato | Escala   |
|-----------------|--------------|----------|
| id_venta        | int          | Razón    |
| id_producto     | int          | Razón    |
| nombre_producto | str          | Nominal  |
| cantidad        | int          | Razón    |
| precio_unitario | float        | Razón    |
| importe         | float        | Razón    |

##### Tabla: Clientes
| Campo          | Tipo de dato   | Escala    |
|----------------|----------------|-----------|
| id_cliente     | int            | Razón     |
| nombre_cliente | str            | Nominal   |
| email          | str            | Nominal   |
| ciudad         | str            | Nominal   |
| fecha_alta     | datetime.date  | Intervalo |

---

#### 3) Información, pasos, pseudocódigo y diagrama

##### 3.1 Información
1. Tema, problema y solución.  
2. Dataset de referencia.  
3. Estructura por tabla.  
4. Escalas de medición.  
5. Sugerencias y mejoras.  
6. Salir.  

##### 3.2 Pasos
1. Definir el objetivo del programa.  
2. Diseñar el menú (interfaz en consola).  
3. Elegir el mecanismo de repetición.  
4. Capturar y procesar la opción elegida.  
5. Escribir las acciones de cada opción.  
6. Control de errores.  
7. Cerrar el programa correctamente.  
8. Organizar el código en funciones.  

##### 3.3 Pseudocódigo
```
INICIO

FUNCIÓN mostrar_menu:
    IMPRIMIR "=== Menú de secciones ==="
    IMPRIMIR "1) Tema, problema y solución"
    IMPRIMIR "2) Dataset de referencia"
    IMPRIMIR "3) Información, pasos pseudocódigo y diagrama"
    IMPRIMIR "4) Sugerencias y mejoras"
    IMPRIMIR "0) Salir"

FUNCIÓN main:
    DEFINIR opcion ← NULO

    MIENTRAS opcion ≠ "0" HACER:
        LLAMAR mostrar_menu
        LEER opcion

        SI opcion = "1":
            IMPRIMIR "Tema, problema y solución..."
        SI opcion = "2":
            IMPRIMIR "Dataset de referencia..."
        SI opcion = "3":
            IMPRIMIR "Información, pasos, pseudocódigo y diagrama..."
        SI opcion = "4":
            IMPRIMIR "Sugerencias y mejoras..."
        SI opcion = "0":
            IMPRIMIR "Salir"

FIN FUNCIÓN

LLAMAR main

FIN
```

##### 3.4 Diagrama de flujo
📂 (Archivo en carpeta)

---

#### 4) Sugerencias y mejoras
1. Agregar comentarios en el código.  
2. Validar entrada del usuario con manejo de excepciones.  
3. Separar la lógica en funciones.  
4. Uso de diccionario para mapear opciones a funciones.  
5. Agregar opción de volver al menú después de cada acción.  
6. Internacionalización (soporte a varios idiomas).  
7. Documentar el código con docstrings.  
8. Agregar pruebas unitarias para asegurar el correcto funcionamiento. 
#### Sugerencias Aceptadas
Aplica separar la logica en funciones 


#### Estadísticas descriptivas básicas calculadas
 ## 🧮 5) Estadísticas Descriptivas y Análisis de Ventas por Ciudad

Para optimizar la **estrategia comercial**, es crucial no solo identificar el rendimiento general de las ventas por ciudad, sino también **entender la distribución y variabilidad de los ingresos**.  

Una vez consolidados los datos de ventas por ciudad (agrupando los ingresos totales por cada una), se calcularán las siguientes **estadísticas descriptivas básicas**, que permitirán obtener una visión más profunda del comportamiento de las ventas en diferentes ubicaciones geográficas, **facilitando la toma de decisiones estratégicas**.

---

### 📊 Estadísticas Descriptivas Clave y su Interpretación

#### **1. Media (Promedio) de Ingresos por Ciudad**
- **Definición:** Representa la suma de los ingresos totales de todas las ciudades dividida por el número total de ciudades.  
- **Importancia:** Ofrece una medida de tendencia central que indica el *ingreso típico* o promedio que genera una ciudad.  
- **Uso:** Permite identificar rápidamente qué ciudades están generando ingresos **por encima o por debajo del promedio global**.

---

#### **2. Mediana de Ingresos por Ciudad**
- **Definición:** Es el valor central en el conjunto de ingresos por ciudad una vez ordenados de menor a mayor.  
  El 50% de las ciudades tendrán ingresos inferiores a la mediana, y el otro 50% superiores.  
- **Importancia:** A diferencia de la media, la mediana es **menos sensible a valores extremos**, proporcionando una medida más robusta cuando la distribución es asimétrica.  
- **Uso:** Ofrece un **punto medio representativo** del rendimiento general, útil para entender dónde se sitúa la mitad de las ciudades en términos de ingresos.

---

#### **3. Moda (Categoría o Cantidad más Frecuente)**
- **Definición:** Es el valor que aparece con mayor frecuencia en un conjunto de datos.  
- **Importancia:** Aunque la moda puede tener **poca relevancia** en ingresos totales (ya que es raro que dos ciudades tengan el mismo total), resulta valiosa en **variables categóricas**.  
- **Uso:**  
  - Identificar la **categoría de producto más vendida** en la mayoría de las ciudades.  
  - Detectar el **medio de pago más frecuente**.  
  - Analizar **preferencias dominantes** en diferentes zonas.

---

#### **4. Desviación Estándar de Ingresos por Ciudad**
- **Definición:** Mide la **dispersión o variabilidad** de los ingresos respecto a la media.  
  - Una **desviación baja** indica ingresos consistentes y cercanos al promedio.  
  - Una **desviación alta** sugiere una gran disparidad entre las ciudades.  
- **Importancia:** Es esencial para entender la **uniformidad o desigualdad** en el rendimiento geográfico de ventas.  
- **Uso:**  
  - 📈 **Baja desviación estándar:** rendimiento homogéneo entre ciudades.  
  - 📉 **Alta desviación estándar:** presencia de *“ciudades estrella”* con ventas altas y *“ciudades rezagadas”* con ventas bajas — áreas clave para intervención estratégica.

---

### 🔍 Conclusión
Estas estadísticas se calcularán una vez consolidada la base de datos, permitiendo un **análisis estadístico inicial** que refleje las **fortalezas y debilidades geográficas** de la estrategia comercial.
