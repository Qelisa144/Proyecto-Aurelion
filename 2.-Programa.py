
def mostrar_menu():
    print("\n=== Menú de secciones ===")
    print("1) Tema, problema y solución")
    print("2) Dataset de referencia")
    print("3) Información, pasos, pseudocódigo y diagrama")
    print("4) Sugerencias y mejoras")
    print("0) Salir")

def mostrar_tema_problema_solucion():
    print("\n👉 Tema, problema y solución:")
    print("🎯 Tema: Optimización de la estrategia comercial mediante el análisis de ventas por ciudad. "
          "El objetivo es identificar zonas con alto y bajo rendimiento para tomar decisiones "
          "informadas que impulsen los ingresos.")
    print("❗ Problema: Actualmente no contamos con una visión clara sobre qué ciudades generan más "
          "ingresos y cuáles tienen bajo rendimiento comercial. Esta falta de información limita "
          "la capacidad de rediseñar estrategias específicas para mejorar las ventas en zonas menos activas.")
    print("✅ Solución: Utilizaremos Python y pandas para realizar un análisis de ventas por ciudad.")

def mostrar_dataset_referencia():
    print("\n👉 Dataset de referencia:")
    print("""
### Tabla: Ventas
| Campo          | Tipo de dato | Escala    |
|----------------|--------------|-----------|
| id_venta       | int          | Razón     |
| fecha          | datetime.date| Intervalo |
| id_cliente     | int          | Razón     |
| nombre_cliente | str          | Nominal   |
| email          | str          | Nominal   |
| medio_pago     | str          | Nominal   |

---

### Tabla: Productos
| Campo           | Tipo de dato | Escala   |
|-----------------|--------------|----------|
| id_producto     | int          | Razón    |
| nombre_producto | str          | Nominal  |
| categoria       | str          | Nominal  |
| precio_unitario | float        | Razón    |

---

### Tabla: Detalle de venta
| Campo           | Tipo de dato | Escala   |
|-----------------|--------------|----------|
| id_venta        | int          | Razón    |
| id_producto     | int          | Razón    |
| nombre_producto | str          | Nominal  |
| cantidad        | int          | Razón    |
| precio_unitario | float        | Razón    |
| importe         | float        | Razón    |

---

### Tabla: Clientes
| Campo          | Tipo de dato | Escala    |
|----------------|--------------|-----------|
| id_cliente     | int          | Razón     |
| nombre_cliente | str          | Nominal   |
| email          | str          | Nominal   |
| ciudad         | str          | Nominal   |
| fecha_alta     | datetime.date| Intervalo |
            """)

def mostrar_info_pasos_pseudocodigo_diagrama():
    print("\n👉 Información, pasos, pseudocódigo y diagrama:")
    print("""
### 3.1 Información
1. **Tema, problema y solución.**
2. **Dataset de referencia.** Resumen de fuente y definición.
3. **Estructura por tabla.** Columnas, tipo y escala de medición.
4. **Escalas de medición.** Descripción y ejemplos.
5. **Sugerencias y mejoras con copilot.**      
6. **Salir.**  

### 3.2 Pasos  
📝 Pasos para diseñar el programa

1. Definir el objetivo del programa
Antes de escribir código, tienes que tener claro qué hará el programa.
 En este caso:
 👉 Mostrar un menú en consola con varias opciones y repetirlo hasta que el usuario elija "Salir".

2. Diseñar el menú (interfaz en consola)
Piensa en las secciones que quieres mostrar.
Escribes cómo debería verse el menú en pantalla, por ejemplo:
=== Menú de secciones ===
1) Tema, problema y solución
2) Dataset de referencia
3) Información, pasos pseudocódigo y diagrama
4) Sugerencias y mejoras
0) Salir
Esto se convierte en la función mostrar_menu().

3. Elegir el mecanismo de repetición
Necesitamos que el menú se repita mientras el usuario no elija "0".
Para eso usamos un bucle while que termina solo si opcion == "0".
while opcion != "0":
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

4. Capturar y procesar la opción elegida
El usuario ingresa un número (input() devuelve siempre un string).
Usamos una estructura condicional if/elif/else para responder a cada opción:
if opcion == "1":
    # Acción para opción 1
elif opcion == "2":
    # Acción para opción 2
...
Esto se llama control de flujo: dependiendo de la opción, se ejecuta un bloque de código distinto.

5. Escribir las acciones de cada opción
Para cada número del menú defines lo que debe mostrar o hacer.
 Ejemplo en la opción 1:
print("👉 Tema, problema y solución:")
print("Tema: ...")
print("❗ Problema: ...")
print("✅ Solución: ...")

6. Control de errores
Si el usuario escribe algo que no corresponde (ejemplo: "abc" o "9"), el programa no debe fallar.
Para eso usamos un else al final:
else:
    print("⚠️ Opción no válida. Intenta nuevamente.")

7. Cerrar el programa correctamente
Cuando el usuario elige "0", mostramos un mensaje de salida y terminamos el bucle.
elif opcion == "0":
    print("👋 Saliendo del programa...")

8. Organizar el código en funciones
Aunque podrías escribir todo en una sola función, es mejor modularizar.
Por eso usamos:
mostrar_menu() para solo imprimir el menú.
main() para manejar la lógica principal.
Esto hace que el código sea más limpio y fácil de mantener.

### 3.3 Pseudocódigo

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
        LEER opcion (entrada del usuario)

        SI opcion = "1" ENTONCES:
            IMPRIMIR "👉 Tema, problema y solución"
            IMPRIMIR "Tema: ..."
            IMPRIMIR "❗ Problema: ..."
            IMPRIMIR "✅ Solución: ..."
        
        SINO SI opcion = "2" ENTONCES:
            IMPRIMIR "👉 Dataset de referencia"
            IMPRIMIR "Detalles del dataset"

        SINO SI opcion = "3" ENTONCES:
            IMPRIMIR "👉 Información, pasos pseudocódigo y diagrama"
            IMPRIMIR "Explicación lógica, pseudocódigo y diagrama"

        SINO SI opcion = "4" ENTONCES:
            IMPRIMIR "👉 Sugerencias y mejoras"
            IMPRIMIR "Ideas de mejora"

        SINO SI opcion = "0" ENTONCES:
            IMPRIMIR "👋 Saliendo del programa..."

        SINO:
            IMPRIMIR "⚠️ Opción no válida. Intenta nuevamente."

FIN FUNCIÓN

LLAMAR main

FIN

### 3.4 Diagrama de flujo
EN CARPETA
            """)

def mostrar_sugerencias_mejoras():
    print("\n👉 Sugerencias y mejoras:")
    print("""
1. Agregar comentarios: Explica la función de cada bloque para facilitar el mantenimiento.
2. Validar entrada del usuario: Usa manejo de excepciones para evitar errores si el usuario ingresa algo inesperado.
3. Separar lógica en funciones: Crea funciones para cada sección del menú, así el código será más modular y fácil de ampliar.
4. Uso de diccionario para el menú: Puedes mapear las opciones a funciones usando un diccionario, lo que simplifica el flujo.
5. Agregar opción de volver al menú: Permite al usuario regresar al menú principal después de cada acción.
6. Internacionalización: Si el programa se usará en otros idiomas, considera separar los textos en variables o archivos de recursos.
7. Documentar el código: Agrega docstrings a las funciones principales.
8. Agregar pruebas unitarias: Para asegurar que cada función se comporta correctamente.
            """)

def salir():
    print("\n👋 Saliendo del programa...")

def opcion_no_valida():
    print("\n⚠️ Opción no válida. Intenta nuevamente.")


def main():
    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_tema_problema_solucion()
        elif opcion == "2":
            mostrar_dataset_referencia()
        elif opcion == "3":
            mostrar_info_pasos_pseudocodigo_diagrama()
        elif opcion == "4":
            mostrar_sugerencias_mejoras()
        elif opcion == "0":
            salir()
        else:
            opcion_no_valida()

if __name__ == "__main__":
    main()
