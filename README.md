# 🐍 Curso de Python

**Centro de Formación Profesional N° 404**  
**Alumno:** David Hernan Bravo  

---

Este repositorio contiene las actividades prácticas correspondientes a la Clase 2 del curso. El objetivo principal de este script es la aplicación de estructuras de control de flujo, operadores lógicos y la correcta modularización del código en Python.

## 🧠 Conceptos Aprendidos y Aplicados

En el archivo `main.py` se implementaron los siguientes conceptos técnicos:

* **Variables y Tipos de Datos:** Declaración y asignación de variables enteras (`int`), cadenas de texto (`str`) y booleanos (`bool`).
  
* **Estructuras Condicionales (`if`, `elif`, `else`):** Control del flujo de ejecución basado en múltiples condiciones y bifurcaciones lógicas.
  
* **Operadores Lógicos y Relacionales:** Evaluación de expresiones combinadas utilizando `and`, `not`, y comparadores relacionales (`>=`, `>`).
  
* **Bucles Iterativos (`for`):** Generación de secuencias numéricas utilizando la función `range(start, stop, step)`, controlando el inicio, el límite y el incremento (saltos lógicos de a 3).
  
* **Modularización (Funciones):** Definición de bloques de código reutilizables mediante `def`. Se separó eficientemente la lógica de validación (`permiso_entrada`) de la lógica de iteración matemática (`numeros_en_rango`).
  
* **Interpolación de Cadenas:** Uso de *f-strings* (`f"..."`) para integrar variables dentro de cadenas de texto de manera limpia y eficiente.
  
* **Punto de Entrada del Script:** Implementación de la guarda `if __name__ == "__main__":`. Esta es una práctica clave de arquitectura para aislar la ejecución principal y permitir que el archivo pueda ser importado como módulo en el futuro sin ejecutar código de más.
  
* **Manejo de Encoding:** Configuración del flujo de salida (`sys.stdout.reconfigure`) para forzar la compatibilidad con UTF-8 y evitar problemas de renderizado en terminales al imprimir caracteres especiales o emojis.

## ⚙️ Ejecución del Proyecto

Para correr el script en tu entorno local, abrí una terminal en el directorio del proyecto y ejecutá:

```bash
python main.py