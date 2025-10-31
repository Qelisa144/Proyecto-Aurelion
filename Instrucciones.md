# Instrucciones para GitHub Copilot

## Estilo general
- Escribe código **simple, claro y fácil de entender**.
- Usa nombres de variables descriptivos y en inglés (por ejemplo: `userCount`, `totalPrice`).
- Prefiere soluciones **nativas del lenguaje**, sin librerías innecesarias.
- Mantén el código **modular**, usando funciones pequeñas y específicas.
- Comenta solo lo necesario, explicando el **porqué**, no el **qué**.
- Evita sobreoptimizar: prioriza la legibilidad sobre la velocidad.
- Sigue las **convenciones estándar del lenguaje** (por ejemplo, PEP8 en Python, o el estilo ESLint recomendado en JavaScript).
- No uses código experimental ni dependencias inestables.

## Estructura del código
- Organiza el código en secciones lógicas.
- Incluye ejemplos o funciones de prueba simples si es útil.
- Si generas un script, empieza con una breve descripción en comentarios.
- Si generas un programa grande, separa responsabilidades en módulos.

## Buenas prácticas
- Maneja errores con mensajes simples y claros.
- Evita duplicar código.
- Prefiere estructuras condicionales simples y bucles claros.
- Documenta las funciones con docstrings o comentarios breves.

## Interacción con el usuario
- Si el programa requiere entrada del usuario, valida los datos de forma sencilla.
- Proporciona mensajes de consola amigables y en español.

## Ejemplo de estilo esperado
```python
def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

resultado = sumar(3, 5)
print(f"El resultado es {resultado}")
